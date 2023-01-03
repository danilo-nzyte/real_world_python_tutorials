from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule

from trigger_ram_api import trigger_ram_api_pipeline


deployment = Deployment.build_from_flow(
    flow=trigger_ram_api_pipeline,
    name="trigger-ram-api-pipeline-deployment",
    version=1,
    work_queue_name="main",
    schedule=RRuleSchedule(rrule="RRULE:FREQ=DAILY"),
    parameters={
        "model": {
            "project": "INSERT_PROJECT",
            "region": "INSERT_REGION",
            "service_account": "INSERT_SERVICE_ACCOUNT",
            "function_url": "INSERT_FUNCTION_URL",
            "task_queue": "INSERT_TASK_QUEUE_NAME",
            "endpoint": "character",
        }
    },
)

deployment.apply()
