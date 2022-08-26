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
├── di  # DIパッケージ
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
  "producer_name": "epic-bot",
  "event_type": "epic-scraper.ItemCreated.1",
  "body": {
    "name": "ホゲホゲテスト",
    "brand_name": "DHOLIC",
    "price": 100,
    "description": "aaaaaaaaaaaaaaaaaaa",
    "gender": "WOMEN",
    "images": [
      "https://www.dzimg.com/Dahong/202204/1365750_20548339_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548340_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548341_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548342_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548343_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548344_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548345_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548346_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548347_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548348_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548349_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548350_k4.jpg",
      "https://www.dzimg.com/Dahong/202204/1365750_20548359_k4.jpg"
    ],
    "url": "https://www.dholic.co.jp/product/goodview_item.asp?gserial=1365750",
    "meta": {
      "keywords":"キーワード",
      "description": "説明文"
    }
  }
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