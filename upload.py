from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    # """Uploads a file to the bucket."""
    # bucket_name = "shehan_billing_bucket"
    # source_file_name = "/home/shane/Pictures/Sprint13.png"
    # destination_blob_name = "test-picture"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
