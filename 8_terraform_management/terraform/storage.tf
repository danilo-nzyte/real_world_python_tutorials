resource "google_storage_bucket" "prefect-deployments" {
  name          = "${var.project_id}-prefect-deployments"
  location      = "EU"
  storage_class = "STANDARD"
}

resource "google_storage_bucket_iam_member" "prefect-deployments-prefect-service-account" {
  for_each = toset([
    "roles/storage.objectAdmin",
  ])
  role       = each.value
  bucket     = google_storage_bucket.prefect-deployments.name
  member     = "serviceAccount:${google_service_account.prefect.email}"
  depends_on = [google_project_service.api_services]
}
