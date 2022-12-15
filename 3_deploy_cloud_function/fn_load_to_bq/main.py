from typing import List, Tuple
import io

import pandas as pd
from google.cloud import bigquery
from google.cloud.bigquery.schema import SchemaField
import functions_framework
import flask

from transforms import transform_dataframe


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


def prepare_data(data: List[dict]) -> Tuple[str, List[SchemaField]]:
    df = pd.json_normalize(data)
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


@functions_framework.http
def create_load_job(request: flask.Request) -> str:
    """
    The request is a flask.Request object that contains a `data` record in the following format:
    {
        ...,
        data: {
            dataset: str,
            table: str,
            results: List[dict]
    }
    """
    request_parameters = request.get_json().get("data")
    results = request_parameters["results"]
    dataset = request_parameters["dataset"]
    table = request_parameters["table"]
    json_records, schema = prepare_data(results)

    bigquery_client = bigquery.Client()
    load_config = bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_TRUNCATE",
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )
    table_id = f"{dataset}.{table}"
    num_rows = load_data_to_bq(bigquery_client, json_records, table_id, load_config)
    print(f"Successfully loaded {num_rows} to {table_id}")
    return "DONE"
