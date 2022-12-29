from typing import List
from dataclasses import asdict
import json
import datetime

import requests
import functions_framework
import flask

from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema


TASK_FUNCTION_URL = "INSERT_CLOUD_TASK_FUNCTION_URL"
PROJECT = "INSERT_PROJECT_ID"
REGION = "INSERT_REGION"
SERVICE_ACCOUNT = "INSERT_SERVICE_ACCOUNT"
LOAD_TO_BQ_FUNCTION = "INSERT_LOAD_TO_BQ_FUNCTION_URL"
LOAD_TO_BQ_QUEUE = "INSERT_QUEUE_NAME"


def _default(obj):
    """Create custom default function for json.dumps() method"""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()


def create_load_bq_data_task(table: str, results: List[CharacterSchema]):
    results = [asdict(result) for result in results]
    task_request = {
        "data": {
            "dataset": "rick_and_morty",
            "table": table,
            "results": results,
        }
    }
    data = {
        "data": {
            "project": PROJECT,
            "region": REGION,
            "service_account": SERVICE_ACCOUNT,
            "number_of_iterations": 1,
            "function_url": LOAD_TO_BQ_FUNCTION,
            "queue": LOAD_TO_BQ_QUEUE,
            "task_request": task_request
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(TASK_FUNCTION_URL, data=json.dumps(data, default=_default), headers=headers)
    print(response.request.body)
    response.raise_for_status()
    return "DONE"


@functions_framework.http
def send_api_request(request: flask.Request) -> str:
    """
    Return a JSON serialised string representing a list of `CharacterSchema` records.

    The request is a flask.Request object that contains a `data` record in the following format:
    {
        ...,
        data: {
            endpoint: str,
            api_params: Fields defined in `ApiParameters` dataclass
            iteration: int
    }
    """
    data = request.get_json().get("data")
    endpoint = data.get("endpoint")
    params = ApiParameters(**data.get("api_params"))
    params.page = data.get("iteration")

    print(f"Calling {endpoint} with {asdict(params)}")
    response = get_endpoint(endpoint, params)
    create_load_bq_data_task(endpoint, response.results)

    return "DONE"
