gcloud alpha functions deploy create-cloud-tasks \
--gen2 \
--region=europe-west2 \
--runtime=python38 \
--source=. \
--entry-point=generate_tasks \
--trigger-http \
--max-instances=5 \
--service-account=<INSERT_SERVICE_ACCOUNT> \
--allow-unauthenticated