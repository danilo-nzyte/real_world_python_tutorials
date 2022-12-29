gcloud alpha functions deploy load-bq-data \
--gen2 \
--region=europe-west2 \
--runtime=python38 \
--source=. \
--entry-point=create_load_job \
--trigger-http \
--max-instances=5 \
--allow-unauthenticated