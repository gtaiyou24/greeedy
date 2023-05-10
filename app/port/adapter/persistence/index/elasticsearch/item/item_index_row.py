import os

from elasticsearch_dsl import Document, Text, Integer, Keyword, Nested


class ItemIndexRow(Document):
    name = Text(search_analyzer="ja_kuromoji_search_analyzer",
                analyzer="ja_kuromoji_index_analyzer",
                fields={
                    "ngram": {
                        "type": "text",
                        "search_analyzer": "ja_ngram_search_analyzer",
                        "analyzer": "ja_ngram_index_analyzer"
                    }
                })
    brand_name = Text(search_analyzer="ja_kuromoji_search_analyzer",
                      analyzer="ja_kuromoji_index_analyzer",
                      fields={
                          "ngram": {
                              "type": "text",
                              "search_analyzer": "ja_ngram_search_analyzer",
                              "analyzer": "ja_ngram_index_analyzer"
                          }
                      })
    price = Integer(meta={"currency": "yen"})
    description = Text(search_analyzer="ja_kuromoji_search_analyzer",
                       analyzer="ja_kuromoji_index_analyzer",
                       fields={
                           "ngram": {
                               "type": "text",
                               "search_analyzer": "ja_ngram_search_analyzer",
                               "analyzer": "ja_ngram_index_analyzer"
                           }
                       })
    gender = Keyword()
    images = Nested(properties={
        "type": Keyword(),
        "color": Keyword(),
        "url": Keyword(),
        "thumbnail": Keyword()
    })
    page = Nested(properties={
        "url": Keyword(),
        "keywords": Text(search_analyzer="ja_kuromoji_search_analyzer", analyzer="ja_kuromoji_index_analyzer"),
        "description": Text(search_analyzer="ja_kuromoji_search_analyzer",
                            analyzer="ja_kuromoji_index_analyzer",
                            fields={
                                "ngram": {
                                    "type": "text",
                                    "search_analyzer": "ja_ngram_search_analyzer",
                                    "analyzer": "ja_ngram_index_analyzer"
                                }
                            })
    })

    class Index:
        name = "items_20230509"
        settings = {
            "analysis": {
                # 1. Character filters
                "char_filter": {
                    # 正規化を行う
                    "normalize": {
                        "type": "icu_normalizer",
                        "name": "nfkc",
                        "mode": "compose"
                    }
                },
                # 2. Tokenizer
                "tokenizer": {
                    # 形態素解析
                    "ja_kuromoji_tokenizer": {
                        "mode": "search",
                        "type": "kuromoji_tokenizer",
                        "discard_compound_token": True,
                        "user_dictionary": os.getenv("USER_DICTIONARY_PATH"),
                    },
                    # Nグラム
                    "ja_ngram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 3,
                        "max_gram": 3,
                        "token_chars": [
                            "letter",  # 文字
                            "digit"  # 数字
                        ]
                    }
                },
                # 3. Token filters
                "filter": {
                    # インデックス時の同義語展開
                    "ja_index_synonym": {
                        "type": "synonym",
                        "lenient": False,
                        "synonyms": []
                    },
                    # 検索時の同義語展開
                    "ja_search_synonym": {
                        "type": "synonym_graph",
                        "lenient": False,
                        "synonyms_path": os.getenv("SYNONYMS_PATH"),
                        "updateable": True
                    }
                },
                # Analyzer
                "analyzer": {
                    # インデックス時のkuromojiアナライザー
                    "ja_kuromoji_index_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_kuromoji_tokenizer",
                        "filter": [
                            "kuromoji_baseform",
                            "kuromoji_part_of_speech",
                            "ja_index_synonym",
                            "cjk_width",
                            "ja_stop",
                            "kuromoji_stemmer",
                            "lowercase"
                        ]
                    },
                    # 検索時のkuromojiアナライザー
                    "ja_kuromoji_search_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_kuromoji_tokenizer",
                        "filter": [
                            "kuromoji_baseform",
                            "kuromoji_part_of_speech",
                            "ja_search_synonym",
                            "cjk_width",
                            "ja_stop",
                            "kuromoji_stemmer",
                            "lowercase"
                        ]
                    },
                    # インデックス時のNグラムアナライザー
                    "ja_ngram_index_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_ngram_tokenizer",
                        "filter": [
                            "lowercase"
                        ]
                    },
                    # 検索時のNグラムアナライザー
                    "ja_ngram_search_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_ngram_tokenizer",
                        "filter": [
                            "ja_search_synonym",
                            "lowercase"
                        ]
                    }
                }
            }
        }
