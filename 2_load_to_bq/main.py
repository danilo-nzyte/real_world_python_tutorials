from typing import List, Tuple
from dataclasses import asdict
import io

import pandas as pd
from google.cloud import bigquery
from google.cloud.bigquery.schema import SchemaField

from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema
from transforms import transform_dataframe


ENDPOINT = "character"


def get_all_paginated_results(
    endpoint: str, pages: int, params: ApiParameters
) -> List[CharacterSchema]:
    results = []
    print(f"Starting loop of {pages} pages")
    for page in range(1, pages + 1):
        params.page = page
        response = get_endpoint(endpoint, params)
        results.extend(response.results)
    print("Completed")
    return results


def _generate_bigquery_schema(df: pd.DataFrame) -> List[SchemaField]:
    TYPE_MAPPING = {
        "i": "INTEGER",
        "u": "NUMERIC",
        "b": "BOOLEAN",
        "f": "FLOAT",
        "O": "STRING",
        "S": "STRING",
        "U": "STRING",
        "M": "TIMESTAMP",
    }
    schema = []
    for column, dtype in df.dtypes.items():
        val = df[column].iloc[0]
        mode = "REPEATED" if isinstance(val, list) else "NULLABLE"

        if isinstance(val, dict) or (mode == "REPEATED" and isinstance(val[0], dict)):
            fields = _generate_bigquery_schema(pd.json_normalize(val))
        else:
            fields = ()

        type = "RECORD" if fields else TYPE_MAPPING.get(dtype.kind)
        schema.append(
            SchemaField(
                name=column,
                field_type=type,
                mode=mode,
                fields=fields,
            )
        )
    return schema


def prepare_data(data: List[CharacterSchema]) -> Tuple[str, List[SchemaField]]:
    df = pd.json_normalize([asdict(x) for x in data], max_level=2)
    df = transform_dataframe(df)
    schema = _generate_bigquery_schema(df)
    json_records = df.to_json(orient="records", lines=True, date_format="iso")
    return json_records, schema


def load_data_to_bq(
    client: bigquery.Client,
    data: str,
    table_id: str,
    load_config: bigquery.LoadJobConfig,
) -> int:
    load_job = client.load_table_from_file(
        io.StringIO(data), table_id, location="EU", job_config=load_config
    )
    load_job.result()  # waits for the job to complete.
    destination_table = client.get_table(table_id)
    num_rows = destination_table.num_rows
    return num_rows


if __name__ == "__main__":
    params = ApiParameters()
    response = get_endpoint(ENDPOINT, params)
    results = get_all_paginated_results(ENDPOINT, response.info.pages, params)
    json_records, schema = prepare_data(results)

    bigquery_client = bigquery.Client()
    load_config = bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_TRUNCATE",
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )
    table_id = f"rick_and_morty.{ENDPOINT}"
    num_rows = load_data_to_bq(bigquery_client, json_records, table_id, load_config)
    print(f"Successfully loaded {num_rows} to {table_id}")
