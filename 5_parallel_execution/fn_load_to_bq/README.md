## Details
There must be a payload sent with the request to trigger the function.

The JSON object must contain a `data` record with the following arguments:

- **dataset**: The BigQuery dataset to use
- **table**: The table name to use
- **results**: A list of dictionaries which represent each row in the table

## Setup
Prepare environment with pipenv.

```shell
pipenv install
pipenv activate
```

## Functions-Framework

```shell
functions-framework --target create_load_job --debug
```

## Deploy Function
```shell
./deploy.sh
```