import logging

def hello_gcs():
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    
    logging.info('Pankaj 26th Dec 2019=New file- has been uploaded to input bucket')
