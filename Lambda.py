
import json
import boto3
import base64
import sagemaker
from sagemaker.serializers import IdentitySerializer

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    key = event["s3_key"]
    bucket = event["s3_bucket"]

    boto3.resource('s3').Bucket(bucket).download_file(key, "/tmp/image.png")

    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }



    import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

ENDPOINT = "image-classification-2025-09-27-18-37-23-527"

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(ENDPOINT)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    inferences = predictor.predict(image)

    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


import json

THRESHOLD = .93


def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event["inferences"]

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(inferences) > THRESHOLD

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }