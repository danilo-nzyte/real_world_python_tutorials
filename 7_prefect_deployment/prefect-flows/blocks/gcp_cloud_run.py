from prefect_gcp.cloud_run import CloudRunJob
from prefect_gcp import GcpCredentials

credentials = GcpCredentials.load("default-credentials")

block = CloudRunJob(
    credentials=credentials,
    project="<INSERT_PROJECT_ID>",
    image="<INSERT_REGISTRY_ADDRESS>/ram-api-flow:2.7.7-python3.8",
    region="<INSERT_REGION>"
)

block.save("cloud-run-infrastructure")