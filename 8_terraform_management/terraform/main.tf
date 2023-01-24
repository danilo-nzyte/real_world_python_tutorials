terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.49.0"
    }
  }
}

provider "google" {
  credentials = file("service_account.json")

  project = "real-world-python-tf"
  region  = "europe-west2"
  zone    = "europe-west2-b"
}

provider "google-beta" {
  credentials = file("service_account.json")

  project = "real-world-python-tf"
  region  = "europe-west2"
  zone    = "europe-west2-b"
}

data "google_project" "project" {
}