resource "google_cloudbuild_trigger" "fn-ram-api-request" {
  location = "europe-west1"
  name     = "build-fn-ram-api-request"
  filename = "4_continuous_deployment/fn_ram_api_request/ci-cd/cloudbuild.yaml"
  substitutions = {
    _SERVICE_ACCOUNT = google_service_account.real-world-python.email
  }
  github {
    owner = "danilo-nzyte"
    name  = "real_world_python_tutorials"
    push {
      branch = "^main$"
    }
  }
  included_files = [
    "4_continuous_deployment/fn_ram_api_request/**",
  ]
  ignored_files = [
    "*.sh",
  ]
  service_account = google_service_account.real-world-python.id
}

resource "google_cloudbuild_trigger" "fn-load-to-bq" {
  location = "europe-west1"
  name     = "build-fn-load-to-bq"
  filename = "4_continuous_deployment/fn_load_to_bq/ci-cd/cloudbuild.yaml"
  substitutions = {
    _SERVICE_ACCOUNT = google_service_account.real-world-python.email
  }
  github {
    owner = "danilo-nzyte"
    name  = "real_world_python_tutorials"
    push {
      branch = "^main$"
    }
  }
  included_files = [
    "4_continuous_deployment/fn_load_to_bq/**",
  ]
  ignored_files = [
    "*.sh",
  ]
  service_account = google_service_account.real-world-python.id
}