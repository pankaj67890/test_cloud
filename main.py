import logging

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
    event (dict): Event payload.
    context (google.cloud.functions.Context): Metadata for the event.
    """

    file = event
    full_path=event['name']
    pathString = full_path.split('/')
    fileName = pathString[-1]
    logging.info('Pankaj 31st Jan 2020=New file-' + fileName + ' has been uploaded to input bucket')
