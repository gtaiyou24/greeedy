import os

import boto3
import sagemaker
from sagemaker import Predictor

colors = ['white', 'black', 'gray', 'brown', 'beige', 'green', 'blue', 'purple', 'yellow', 'pink', 'red', 'orange']
name = 'ハーフパフスリーブブラウス・t00407'
payload = {
    'mode': 'image_classification',
    'texts': [f'{color} {name}' for color in colors],
    'images': [
        "https://www.dzimg.com/Dahong/202203/1338722_20307385_k1.jpg",
        "https://www.dzimg.com/Dahong/202203/1338722_20307386_k1.jpg"
    ]
}

sagemaker_client = Predictor(
    endpoint_name='fashion-clip',
    sagemaker_session=sagemaker.Session(boto_session=boto3.Session(profile_name=os.environ.get("AWS_PROFILE"))),
    serializer=sagemaker.serializers.JSONSerializer(),
    deserializer=sagemaker.deserializers.JSONDeserializer(),
)
response = sagemaker_client.predict(payload)
for i, labels in enumerate(response):
    k = max(labels, key=labels.get)
    label = k.split(' ')[0]
    print(label)
