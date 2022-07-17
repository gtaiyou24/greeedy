from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from config.credential import MySQLCredentialGetter


class MySQLConfig:
    @inject
    def __init__(self, credential: MySQLCredentialGetter):
        self.__credential = credential
        self.__engine = create_engine("mysql://{username}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
            username=self.__credential.get_username(),
            password=self.__credential.get_password(),
            host=self.__credential.get_hostname(),
            port=self.__credential.get_port(),
            db_name=self.__credential.get_database_name(),
        ))

    def engine(self) -> Engine:
        return self.__engine
