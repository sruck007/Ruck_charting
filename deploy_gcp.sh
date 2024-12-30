#!/bin/bash

# Authenticate
gcloud auth login

# Deploy Flask app to Cloud Run
gcloud run deploy transcription-app \
    --source . \
    --region us-central1 \
    --platform managed

echo "Deployment complete!"
