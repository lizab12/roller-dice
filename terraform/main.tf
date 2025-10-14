provider "google" {
  project = var.project
  region  = var.region
}

resource "google_artifact_registry_repository" "dice" {
  repository_id = "dice-app"
  location      = var.region
  format        = "DOCKER"
  description   = "Dice Roller Docker repo"
}
