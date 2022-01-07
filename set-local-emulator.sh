#!/usr/bin/env sh


gcloud config configurations create emulator &&
gcloud config set auth/disable_credentials true &&
gcloud config set project spanner-project-product &&
gcloud config set api_endpoint_overrides/spanner http://localhost:9020/ &&
gcloud config set auth/disable_credentials true &&
gcloud spanner instances create spanner-instance-product --config=emulator-config --description=Emulator --nodes=1
gcloud spanner databases create spanner-database-product --instance=spanner-instance-product
