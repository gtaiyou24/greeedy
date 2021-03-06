from elasticsearch import Elasticsearch
from injector import inject

from config.credential import ElasticsearchCredentialGetter


class ElasticsearchConfig:
    @inject
    def __init__(self, credential: ElasticsearchCredentialGetter):
        self.__credential = credential
        self.__engine = Elasticsearch(
            self.__credential.get_host(),
            http_auth=(self.__credential.get_username(), self.__credential.get_password())
        )

    def engine(self) -> Elasticsearch:
        return self.__engine
