from functools import reduce
from typing import Callable, List
import json

import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


def create_row_hash(df: pd.DataFrame) -> pd.DataFrame:
    """Create unique hash of entire DataFrame row."""
    df.set_index(pd.util.hash_pandas_object(df.astype("str")), drop=False, inplace=True)
    df = df.reset_index(names=["row_hash"])
    return df


def add_current_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df.insert(0, "ingestion_date", pd.to_datetime("now", utc=True))
    return df


def _get_nested_fields(df: pd.DataFrame) -> List[str]:
    """Return a list of nested fields, sorted by the deepest level of nesting first."""
    nested_fields = [*{field.rsplit(".", 1)[0] for field in df.columns if "." in field}]
    nested_fields.sort(key=lambda record: len(record.split(".")), reverse=True)
    return nested_fields


def df_denormalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert a normalised DataFrame into a nested structure.

    Fields separated by '.' are considered part of a nested structure.
    """
    nested_fields = _get_nested_fields(df)
    for field in nested_fields:
        list_of_children = [column for column in df.columns if field in column]
        rename = {
            field_name: field_name.rsplit(".", 1)[1] for field_name in list_of_children
        }
        renamed_fields = df[list_of_children].rename(columns=rename)
        df[field] = json.loads(renamed_fields.to_json(orient="records"))
        df.drop(list_of_children, axis=1, inplace=True)
    return df


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    preprocessor = compose(
        create_row_hash,
        add_current_datetime,
        df_denormalize,
    )

    return preprocessor(df)
