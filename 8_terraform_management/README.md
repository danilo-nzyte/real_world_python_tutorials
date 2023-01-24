# Setup
## 1. Install Terraform
Link to Terraform installation article

## 2. Create a project
```bash
gcloud projects create ...
```

## 3. Create a service account
Set the correct project variable
```bash
gcloud config set project real-world-python-tf
```

Create the service account
```bash
gcloud iam service-accounts create terraform \
  --description="Service Account to use with Terraform"
```

Create the key file
```bash
gcloud iam service-accounts keys create service_account.json \
  --iam-account=terraform@real-world-python-tf.iam.gserviceaccount.com
```

Grant the Editor role
```bash
gcloud projects add-iam-policy-binding real-world-python-tf \
  --member=serviceAccount:terraform@real-world-python-tf.iam.gserviceaccount.com \
  --role=roles/editor
```

# Resources
- IAM
- Service Accounts
- Google Cloud Storage
- BigQuery Dataset
- Cloud Run
- Cloud Functions
- Compute Engine
- Artifact Registry
- Cloud Build
- Cloud Tasks

## Notes
- We won't deploy Cloud Functions using Terraform because we have a separate CI/CD pipeline to redeploy functions from our codebase instead.