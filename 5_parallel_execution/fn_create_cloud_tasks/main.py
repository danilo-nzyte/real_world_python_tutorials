import os
import math
from dataclasses import dataclass
from multiprocessing import Pool
from functools import partial

import functions_framework
import flask

from tasks import create_task


@dataclass
class Request:
    project: str
    region: str
    service_account: str
    number_of_iterations: int
    function_url: str
    queue: str
    task_request: dict


def _run_partial_func(function):
    return function()


@functions_framework.http
def generate_tasks(request: flask.Request) -> str:
    """
    Create a single Google Cloud Task for each `number_of_iterations` with a `task_request` as the payload.

    The `request` is a flask.Request object that contains a `data` record in the following format:
    {
        ...,
        data: {
            project: str,
            region: str,
            service_account: str,
            number_of_iterations: int,
            function_url: str,
            queue: str,
            task_request: {
                data: {
                    ...
                }
            }
    }
    """
    print(f"Incoming Request: {request.get_json()}")
    try:
        data = request.get_json().get("data")
        args = Request(**data)
    except TypeError:
        print(f'Invalid request. No "data" supplied in request.')
    tasks = []
    for iteration in range(1, args.number_of_iterations + 1):
        task_request = args.task_request
        task_request["data"] = {**task_request["data"], "iteration": iteration}
        in_seconds = math.floor(iteration / 10) * 30  # 30 second delay every 10 tasks.

        tasks.append(
            partial(
                create_task,
                args.project,
                args.queue,
                args.region,
                args.function_url,
                args.service_account,
                dict(args.task_request),
                in_seconds,
            )
        )

    with Pool(len(os.sched_getaffinity(0))) as p:
        p.map(_run_partial_func, tasks)

    return "DONE"
