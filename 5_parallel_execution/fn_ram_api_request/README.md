### Details
There must be a payload sent with the request to trigger the function.

The JSON object must contain a `data` record with the following arguments:

**endpoint**: The RAM API endpoint e.g. "character"

**api_params**: Fields defined in `ApiParameters` dataclass

**iteration**: This is provided by the task from Cloud Tasks and represents the page number to call the API for.

There are constants in `main.py` that need to be updated with your relevant values.

```shell
TASK_FUNCTION_URL = "INSERT_CLOUD_TASK_FUNCTION_URL"
PROJECT = "INSERT_PROJECT_ID"
REGION = "INSERT_REGION"
SERVICE_ACCOUNT = "INSERT_SERVICE_ACCOUNT"
LOAD_TO_BQ_FUNCTION = "INSERT_LOAD_TO_BQ_FUNCTION_URL"
LOAD_TO_BQ_QUEUE = "INSERT_QUEUE_NAME"
```

### Setup
Prepare environment with pipenv.

```shell
pipenv install
pipenv activate
```

### Functions-Framework

```shell
functions-framework --target send_api_request --debug
```

### Deploy Function
```shell
./deploy.sh
```