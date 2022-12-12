from typing import List
from dataclasses import asdict
import json
import datetime

import functions_framework
import flask

from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema


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


def default(obj):
    """Create custom default function for json.dumps() method"""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()


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
    }
    """
    data = request.get_json().get("data")
    params = ApiParameters(data.get("api_params"))
    response = get_endpoint(data.get("endpoint"), params)
    results = get_all_paginated_results(data.get("endpoint"), response.info.pages, params)
    results = [asdict(result) for result in results]

    return json.dumps(results, default=default)
