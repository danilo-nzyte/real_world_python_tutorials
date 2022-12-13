## Summary

We need to break the existing code out into two separate functions based on their unique responsibilities.

1. Calling the API and collecting data
2. Loading the data into BigQuery

## Testing

fn_get_api_data: `functions-framework --target send_api_request --debug`</br>
fn_load_to_bq: `functions-framework --target create_load_job --debug`

## Deploying

Prerequisites:
- Need to enable a few API's in Google Cloud:</br>
	Artifact Registry API</br>
	Cloud Build API</br>
	Cloud Run Admin API</br>
	Cloud Functions API