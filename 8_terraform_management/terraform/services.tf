resource "google_project_service" "api_services" {
  project = var.project_id
  for_each = toset(
    [
      "iam.googleapis.com",
      "compute.googleapis.com",
      "bigquery.googleapis.com",
      "run.googleapis.com",
      "cloudfunctions.googleapis.com",
      "artifactregistry.googleapis.com",
      "cloudbuild.googleapis.com",
      "cloudtasks.googleapis.com",
      "cloudresourcemanager.googleapis.com",
    ]
  )
  service                    = each.key
  disable_on_destroy         = false
  disable_dependent_services = true
}
