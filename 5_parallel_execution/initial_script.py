import json

import requests


BASE_URL = "https://rickandmortyapi.com/api"
CLOUD_TASK_FUNCTION_URL = "https://create-cloud-tasks-psmosvfuya-nw.a.run.app"

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
            "project": "nzyte-272212",
            "region": "europe-west2",
            "service_account" : "real-world-python@nzyte-272212.iam.gserviceaccount.com",
            "number_of_iterations" : pages,
            "function_url" : "https://ram-api-request-psmosvfuya-nw.a.run.app",
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