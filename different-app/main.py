from google.cloud import secretmanager_v1

def sample_access_secret_version():
    # Create a client
    client = secretmanager_v1.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager_v1.AccessSecretVersionRequest(
        name="projects/35212339715/secrets/sftp-secret/versions/latest",
    )

    # Make the request
    response = client.access_secret_version(request=request)

    # Handle the response
    print(response)
    #change
