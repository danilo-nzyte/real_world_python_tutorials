variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
}

variable "zone" {
  description = "GCP Zone"
  type        = string
}

variable "prefect_api_key" {
  description = "Prefect API Key"
  type        = string
  sensitive   = true
}

variable "prefect_workspace" {
  description = "Prefect Workspace ID"
  type        = string
  sensitive   = true
}