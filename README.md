# Greeedy
ファッションアイテムに特化した検索エンジン「Greeedy」

## Structure
<details><summary>システム構成</summary>

本システムは、ファッションブランドとファッションアイテムの管理と検索を可能にするためのコンテキストです。
検索エンジンには、Amazon Opensearch Serviceを採用し、データベースには[PlanetScale](https://planetscale.com)のMySQLを採用しています。

![](./doc/システム構成図.png)

</details>

<details><summary>アーキテクチャとパッケージ構成</summary>

このアプリケーションのアーキテクチャには、エンドユーザー、管理ユーザー、外部コンテキストとAPIやMQなど様々な入出力方法を用いてやりとりするため、
ヘキサゴナルアーキテクチャ(ポートアンドアダプター)を採用しています。 
このアーキテクチャは、外部と対話するポートとアダプターを容易に追加したり、変更しやすいうえにテストもしやすい特徴があります。

![](./doc/アーキテクチャ.png)

パッケージ構成は以下の通りです。

```shell
app
├── application  # アプリケーション層
├── config  # 設定パッケージ
├── domain  # ドメイン層
│   └── model
├── exception  # 例外パッケージ
└── port
    └── adapter  # ポート・アダプター層
```

</details>

## How to

<details><summary>起動方法</summary>

```bash
$ cd ~/path/to/greeedy

# .envファイルをコピーして、適切な値に書き換える
$ cp ./elasticsearch/.env.sample ./elasticsearch/.env

# コンテナの起動
$ docker-compose up --build

$ docker-compose run --rm \
  -p 8000:8000 \
  app \
  uvicorn start_app:app --host 0.0.0.0 --reload

$ mysql -h 127.0.0.1 -P 3306 -u user -p
```

 - [Greeedy API - Swagger UI](http://0.0.0.0:8000/docs)

</details>

<details><summary>メッセージを購読</summary>

あらかじめ「コンテナの起動方法」に従ってコンテナを起動してください。起動したら、別ターミナルで下記を実行します。
```bash
# キューの一覧を表示
$ aws sqs list-queues --endpoint-url http://localhost:4566

# メッセージを作成
$ aws sqs send-message \
    --queue-url http://localhost:4566/000000000000/greeedy-queue \
    --endpoint-url http://localhost:4566 \
    --message-body '{
  "notification_id": 1,
  "event": {
    "name": "レースパンチングブラウス・全2色・b71916",
    "brand_name": "DHOLIC",
    "price": 2570,
    "description": "[DESIGN]\n\n総レースがフェミニンなブラウスです。\nカラーネックが端正で中央のボタンが開閉できます。\n肩と裾はスカラップレースでムードUP↑\n\nレースは肩をやや覆うデザインです。\nフロントはバイアス状に、バックは縦のパンチングで\nコントラストをつけました。\nコーデの主役になるのでデニムに着流すだけでも◎\n\n\n※素材の特性上、多少透け感がございます。\nスキントーンの下着とお召しいただくと安心です。\n\n\n※製造過程上、パターンにずれが生じる\n場合がありますが不備ではございません。",
    "gender": "WOMEN",
    "images": [
      "https://www.dzimg.com/Dahong/202203/1353897_20465618_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465619_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465620_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465621_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465622_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465623_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465624_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465625_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465626_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465627_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465628_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465629_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465630_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465631_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465632_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465633_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465634_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465635_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465636_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20465637_k1.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444554_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444555_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444556_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444557_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444558_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444559_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444560_k2.jpg",
      "https://www.dzimg.com/Dahong/202203/1353897_20444561_k2.jpg"
    ],
    "url": "https://m.dholic.co.jp/product/goodview_item.asp?gserial=1353897",
    "meta": {
      "keywords": "レースパンチングブラウス・全2色・b71916,ブラウス,ノースリーブブラウス, 通販,ファッション,レディース,DHOLIC,ディーホリック,コスメ,コスメ通販,韓国コスメ,韓国コスメ通販,韓国ファッション,韓国通販,韓国ファッション通販, 韓国レディース通販",
      "description": "レディースファッションショッピングモールDHOLICの[レースパンチングブラウス・全2色・b71916]ページです。毎日たくさんの新商品が登録されており、即日配送商品とセール商品と割引クーポンGETのチャンスもお見逃しなく。"
    }
  },
  "occurred_on": "2022-09-01 08:41:49",
  "event_type": "ItemCreated.1",
  "version": 1,
  "producer_name": "epic-bot"
}'

# キューイングされたメッセージを表示
$ aws sqs receive-message \
    --queue-url http://localhost:4566/000000000000/greeedy-queue \
    --endpoint-url http://localhost:4566
```

</details>

<details><summary>UT実行方法</summary>

```bash
$ pytest -v .
```

</details>

<details><summary>デプロイ手順</summary>

```bash
sh build_and_push.sh taiyou24 greeedy-lightsail ./app/Dockerfile
```
</details>