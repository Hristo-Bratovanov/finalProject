from storages.backends.azure_storage import AzureStorage
from decouple import config

class AzureMediaStorage(AzureStorage):
    account_name = config("AZURE_ACCOUNT_NAME")
    account_key = config("AZURE_ACCOUNT_KEY")
    azure_container = config("AZURE_CONTAINER")
    expiration_secs = 3600  # signed URL lifetime (1 hour)
