import argparse
import json
import time
from datetime import datetime

import boto3
from opensearchpy import OpenSearch

parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="Opensearchのホスト名", type=str)
parser.add_argument("index", help="Opensearchのインデックス名", type=str)
parser.add_argument("username", help="Opensearchのユーザー名", type=str)
parser.add_argument("password", help="Opensearchのパスワード", type=str)
parser.add_argument("-p", "--preview", help="プレビューモードかどうか。デフォルトではFalse", action='store_true')
args = parser.parse_args()

opensearch_hostname = args.hostname
opensearch_index = args.index
opensearch_username = args.username
opensearch_password = args.password
preview = args.preview

sqs = boto3.client("sqs")
client = OpenSearch(hosts=[opensearch_hostname], http_auth=(opensearch_username, opensearch_password), timeout=180)
query = {
    "query": {"match_all": {}},
    "size": 500,
    "sort": [{"_score": {"order": "desc"}, "_id": {"order": "asc"}}]
}
count = client.count(body={"query": {"match_all": {}}}, index=opensearch_index)['count']
i = 0
while True:
    try:
        res = client.search(body=query, index=opensearch_index)
        last_hit = None
        if not res['hits']['hits']:
            break
        for hit in res['hits']['hits']:
            body = {
                "notification_id": 1,
                "event": {
                    "name": hit['_source']['name'],
                    "brand_name": hit['_source']['brand_name'],
                    "colors": [
                        'white',
                        'black',
                        'gray',
                        'brown',
                        'beige',
                        'green',
                        'blue',
                        'purple',
                        'yellow',
                        'pink',
                        'red',
                        'orange'
                    ],
                    "price": hit['_source']['price'],
                    "description": hit['_source'].get('description', ''),
                    "gender": hit['_source']['gender'],
                    "images": [image['url'] for image in hit['_source']['images']],
                    "url": hit['_source']['page'].get('url', ''),
                    "meta": {
                        "keywords": hit['_source']['page'].get('keywords', ''),
                        "description": hit['_source']['page'].get('keywords', '')
                    }
                },
                "occurred_on": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "event_type": "ItemCreated.1",
                "version": 1,
                "producer_name": "epic-bot"
            }
            if not preview:
                sqs.send_message(
                    QueueUrl="https://sqs.ap-northeast-1.amazonaws.com/684886458640/greeedy-queue",
                    MessageBody=json.dumps(body)
                )
            i += 1
            last_hit = hit
    except Exception as e:
        print(last_hit['sort'])
        raise e

    time.sleep(10)
    print(f"progress = {i / count}")
    print(last_hit['sort'])
    query['search_after'] = last_hit['sort']