resource "google_service_account" "real-world-python" {
  account_id   = "real-world-python"
  display_name = "real-world-python"
  description  = "Service Account for Real World Python Project"
  depends_on   = [google_project_service.api_services]
}

resource "google_project_iam_member" "real-world-python-service-account-iam" {
  for_each = toset([
    "roles/iam.serviceAccountUser",
    "roles/bigquery.dataEditor",
    "roles/bigquery.jobUser",
    "roles/cloudfunctions.admin",
    "roles/storage.admin",
    "roles/run.developer",
    "roles/logging.logWriter"
  ])
  role    = each.value
  project = var.project_id
  member  = "serviceAccount:${google_service_account.real-world-python.email}"
}

resource "google_service_account" "prefect" {
  account_id   = "prefect"
  display_name = "prefect"
  description  = "Authorisation to use with Prefect Cloud and Prefect Agent"
  depends_on   = [google_project_service.api_services]
}

resource "google_project_iam_member" "prefect-service-account-iam" {
  for_each = toset([
    "roles/iam.serviceAccountUser",
    "roles/run.admin",
    "roles/logging.admin"
  ])
  role       = each.value
  project    = var.project_id
  member     = "serviceAccount:${google_service_account.prefect.email}"
  depends_on = [google_project_service.api_services]
}

resource "google_service_account_key" "prefect_service_account_key" {
  service_account_id = google_service_account.prefect.name
  public_key_type    = "TYPE_X509_PEM_FILE"
  depends_on         = [google_project_service.api_services]
}

resource "google_service_account_iam_member" "real-world-python-cloud-build-default" {

  service_account_id = "projects/${var.project_id}/serviceAccounts/${data.google_project.project.number}-compute@developer.gserviceaccount.com"
  for_each = toset([
    "roles/iam.serviceAccountUser",
  ])
  role   = each.value
  member = "serviceAccount:${google_service_account.real-world-python.email}"
}
