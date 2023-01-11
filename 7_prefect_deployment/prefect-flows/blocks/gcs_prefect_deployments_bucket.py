from prefect.filesystems import GCS

with open("service_account.json") as f:
    service_account = f.read()

block = GCS(
    bucket_path="prefect-deployments/dev/",
    service_account_info=service_account,
    project="INSERT_PROJECT_ID"
)

block.save("dev")