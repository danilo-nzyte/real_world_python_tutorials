curl -X POST localhost:8080 \
   -H "Content-Type: application/json" \
   -d '{
        "data" : {
            "project": <INSERT_PROJECT>,
            "region": <INSERT_REGION>,
            "service_account" : <INSERT_SERVICE_ACCOUNT>,
            "number_of_iterations" : 42,
            "function_url" : <INSERT_FUNCTION_URL>,
            "queue" : "fn-ram-api-request",
            "task_request" : {
                "data" : {
                    "endpoint": "character",
                    "api_params": {}
                }
            }
        }
    }
'