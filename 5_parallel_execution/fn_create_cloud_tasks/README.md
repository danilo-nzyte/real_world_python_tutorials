### Details
There must be a payload sent with the request to trigger the function.

The JSON object must contain a `data` record with the following arguments:

**project**: The GCP project ID

**region**: The GCP region e.g. "europe-west2"

**service_account**: The service account to use to authenticate with Google Cloud Tasks

**number_of_iterations**: How many tasks to create with a different iteration passed along with each task

**function_url**: The GCP Function URL

**queue**: The name of the Cloud Task queue

**task_request**: The payload to send in the task


### Setup
Prepare environment with pipenv.

```shell
pipenv install
pipenv activate
```

### Functions-Framework

```shell
functions-framework --target generate_tasks --debug
```

### Deploy Function
```shell
./deploy.sh
```