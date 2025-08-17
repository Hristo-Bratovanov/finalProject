import os
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions

AZURE_ACCOUNT_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = os.environ.get("AZURE_CONTAINER", "media")

def generate_sas_url(blob_name, expiry_minutes=60):
    sas_token = generate_blob_sas(
        account_name=AZURE_ACCOUNT_NAME,
        container_name=AZURE_CONTAINER,
        blob_name=blob_name,
        account_key=AZURE_ACCOUNT_KEY,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(minutes=expiry_minutes)
    )
    return f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/{blob_name}?{sas_token}"

