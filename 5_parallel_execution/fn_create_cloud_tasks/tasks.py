import datetime
import json

from google.cloud import tasks_v2
from google.protobuf import duration_pb2, timestamp_pb2

def create_task(project, queue, location, url, service_account, payload=None, in_seconds=None):
    # Create a client.
    client = tasks_v2.CloudTasksClient()
    
    deadline = 900

    # Construct the fully qualified queue name.
    parent = client.queue_path(project, location, queue)

    # Construct the request body.
    task = {
        "http_request": {  # Specify the type of request.
            "http_method": tasks_v2.HttpMethod.POST,
            "url": url,  # The full url path that the task will be sent to.
        "oidc_token": {
            "service_account_email": service_account,
            "audience": url,
        },
        }
    }

    if payload is not None:
        if isinstance(payload, dict):
            # Convert dict to JSON string
            payload = json.dumps(payload)
            # specify http content-type to application/json
            task["http_request"]["headers"] = {"Content-type": "application/json"}

        # The API expects a payload of type bytes.
        converted_payload = payload.encode()

        # Add the payload to the request.
        task["http_request"]["body"] = converted_payload

    if in_seconds is not None:
        # Convert "seconds from now" into an rfc3339 datetime string.
        d = datetime.datetime.utcnow() + datetime.timedelta(seconds=in_seconds)

        # Create Timestamp protobuf.
        timestamp = timestamp_pb2.Timestamp()
        timestamp.FromDatetime(d)

        # Add the timestamp to the tasks.
        task["schedule_time"] = timestamp

    if deadline is not None:
        # Add dispatch deadline for requests sent to the worker.
        duration = duration_pb2.Duration()
        duration.FromSeconds(deadline)
        task["dispatch_deadline"] = duration

    # Use the client to build and send the task.
    response = client.create_task(request={"parent": parent, "task": task})

    print("Created task {}".format(response.name))