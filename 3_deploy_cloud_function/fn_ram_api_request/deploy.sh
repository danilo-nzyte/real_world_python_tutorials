gcloud alpha functions deploy ram-api-request \
--gen2 \
--region=europe-west2 \
--runtime=python38 \
--source=. \
--entry-point=send_api_request \
--trigger-http \
--max-instances=5 \
--allow-unauthenticated