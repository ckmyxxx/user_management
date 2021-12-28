import boto3
import os
from base64 import b64decode

# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container
DECRYPTED = {}


def decrypto(key):
    if DECRYPTED.get(key):
        return DECRYPTED[key]
    else:
        encode = os.environ[key]
        DECRYPTED[key] = boto3.client('kms', region_name='us-east-2').decrypt(
            CiphertextBlob=b64decode(encode),
            EncryptionContext={
                'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
        )['Plaintext'].decode('utf-8')
        return DECRYPTED[key]


def lambda_handler(event, context):
    # TODO handle the event here
    pass
