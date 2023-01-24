resource "google_compute_instance" "prefect-agent" {
  name                    = "${var.project_id}-prefect-agent"
  zone                    = var.zone
  machine_type            = "e2-micro"
  metadata_startup_script = file("./sh_scripts/prefect_agent.sh")

  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20230104"
    }
  }
  network_interface {
    network    = "default"
    subnetwork = "default"
    access_config {
      network_tier = "PREMIUM"
    }
  }

  service_account {
    scopes = [
      "cloud-platform",
    ]
    email = google_service_account.prefect.email
  }

  metadata = {
    PREFECT_API_KEY   = var.prefect_api_key
    PREFECT_WORKSPACE = var.prefect_workspace
  }

  depends_on = [google_project_service.api_services]
}
