from di import DIContainer
from sqlalchemy.orm import scoped_session, sessionmaker

from config import MySQLConfig


config = DIContainer.instance().resolve(MySQLConfig)
session_cls = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=config.engine()))
session = session_cls()

__all__ = ['session']
