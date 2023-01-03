import json

import requests
from prefect import flow, task
from pydantic import BaseModel


BASE_URL = "https://rickandmortyapi.com/api"
CLOUD_TASK_FUNCTION_URL = "INSERT_CLOUD_TASK_FUNCTION_URL"


class Model(BaseModel):
    project: str
    region: str
    service_account: str
    function_url: str
    task_queue: str
    endpoint: str


@task()
def get_pages(endpoint: str):
    response = requests.get(url=f"{BASE_URL}/{endpoint}")
    response.raise_for_status()
    response = response.json()
    pages = response.get("info").get("pages")
    return pages


@task(log_prints=True)
def start_process(pages: int, model: Model):
    task_request = {"data": {"endpoint": model.endpoint, "api_params": {}}}
    data = {
        "data": {
            "project": model.project,
            "region": model.region,
            "service_account": model.service_account,
            "number_of_iterations": pages,
            "function_url": model.function_url,
            "queue": model.task_queue,
            "task_request": task_request,
        }
    }
    headers = {"Content-Type": "application/json"}

    print(f"LOGGING: Sending request with data: {json.dumps(data)}")
    response = requests.post(
        CLOUD_TASK_FUNCTION_URL, data=json.dumps(data), headers=headers
    )
    response.raise_for_status()
    return "DONE"


@flow(log_prints=True)
def trigger_ram_api_pipeline(model: Model):
    print("LOGGING: Triggering RAM API Request Pipeline")
    pages = get_pages("character")
    start_process(pages, model)
    return "DONE"


if __name__ == "__main__":
    model = Model(
        project="INSERT_PROJECT",
        region="INSERT_REGION",
        service_account="INSERT_SERVICE_ACCOUNT",
        function_url="INSERT_FUNCTION_URL",
        task_queue="INSERT_TASK_QUEUE_NAME",
        endpoint="character",
    )
    trigger_ram_api_pipeline(model)
