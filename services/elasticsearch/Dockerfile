FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.1

# プラグインをインストールする
RUN elasticsearch-plugin install analysis-kuromoji && \
    elasticsearch-plugin install analysis-icu
