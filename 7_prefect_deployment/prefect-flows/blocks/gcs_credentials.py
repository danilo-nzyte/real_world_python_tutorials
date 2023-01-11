from prefect_gcp import GcpCredentials

with open("service_account.json") as f:
    service_account = f.read()

block = GcpCredentials(
    service_account_info=service_account,
    project="INSERT_PROJECT_ID"
)

block.save("default-credentials")