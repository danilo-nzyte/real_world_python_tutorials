resource "google_cloud_tasks_queue" "fn-ram-api-request" {
  name     = "fn-ram-api-request"
  location = var.region
  rate_limits {
    max_dispatches_per_second = 500
  }
  retry_config {
    max_attempts  = -1
    min_backoff   = "0.100s"
    max_backoff   = "3600s"
    max_doublings = 16
  }
  depends_on = [google_project_service.api_services]
}

resource "google_cloud_tasks_queue" "fn-load-bq-data" {
  name     = "fn-load-bq-data"
  location = var.region
  rate_limits {
    max_dispatches_per_second = 500
  }
  retry_config {
    max_attempts  = -1
    min_backoff   = "0.100s"
    max_backoff   = "3600s"
    max_doublings = 16
  }
  depends_on = [google_project_service.api_services]
}