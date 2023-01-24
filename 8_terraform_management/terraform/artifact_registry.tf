resource "google_artifact_registry_repository" "prefect-flows-docker" {
  provider      = google-beta
  location      = var.region
  repository_id = "prefect-flows-docker"
  description   = "Docker repository for Prefect flows"
  format        = "DOCKER"
  depends_on    = [google_project_service.api_services]
}