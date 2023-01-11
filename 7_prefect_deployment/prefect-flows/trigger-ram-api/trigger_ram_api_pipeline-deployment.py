from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule
from prefect.filesystems import GCS
from prefect_gcp.cloud_run import CloudRunJob

from trigger_ram_api import trigger_ram_api_pipeline

storage = GCS.load("dev")
cloud_run_block = CloudRunJob.load("cloud-run-infrastructure")

deployment = Deployment.build_from_flow(
    flow=trigger_ram_api_pipeline,
    name="trigger-ram-api-pipeline-deployment",
    version=1,
    work_queue_name="main",
    schedule=RRuleSchedule(rrule="RRULE:FREQ=DAILY"),
    storage=storage,
    infrastructure=cloud_run_block,
    parameters={
        "model": {
            "project": "INSERT_PROJECT_ID",
            "region": "INSERT_REGION",
            "service_account": "INSERT_SERVICE_ACCOUNT",
            "function_url": "INSERT_FUNCTION_URL",
            "task_queue": "INSERT_TASK_QUEUE_NAME", 
            "endpoint": "character",
        }
    },
)

deployment.apply()
