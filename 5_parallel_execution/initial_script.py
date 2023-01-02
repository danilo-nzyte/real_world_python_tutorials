import json

import requests


BASE_URL = "https://rickandmortyapi.com/api"
CLOUD_TASK_FUNCTION_URL = "INSERT_FUNCTION_URL"

def get_pages(endpoint: str):
    response = requests.get(url=f"{BASE_URL}/{endpoint}")
    response.raise_for_status()
    response = response.json()
    pages = response.get("info").get("pages")
    return pages


def start_process(pages: int):
    task_request = {
        "data" : {
            "endpoint": "character",
            "api_params": {}
            }
        }
    data = {
        "data" : {
            "project": "INSERT_PROJECT",
            "region": "INSERT_REGION",
            "service_account" : "INSERT_SERVICE_ACCOUNT",
            "number_of_iterations" : pages,
            "function_url" : "INSERT_FUNCTION_URL",
            "queue" : "fn-ram-api-request",
            "task_request" : task_request
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(CLOUD_TASK_FUNCTION_URL, data=json.dumps(data), headers=headers)
    response.raise_for_status()
    return "DONE"

if __name__ == "__main__":
    pages = get_pages("character")
    start_process(pages)