from elasticsearch import Elasticsearch
from injector import inject

from core.credential import ElasticsearchCredentialGetter


class ElasticsearchConfig:
    @inject
    def __init__(self, credential: ElasticsearchCredentialGetter):
        self.__credential = credential
        self.__engine = Elasticsearch(
            self.__credential.get_hosts(),
            http_auth=(self.__credential.get_username(), self.__credential.get_password())
        )

    def engine(self) -> Elasticsearch:
        return self.__engine
