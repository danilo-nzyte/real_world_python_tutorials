resource "google_bigquery_dataset" "rick_and_morty" {
  dataset_id = "rick_and_morty"
  location   = "EU"
  depends_on = [google_project_service.api_services]
}