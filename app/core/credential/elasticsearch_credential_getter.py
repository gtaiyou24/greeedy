import os
from typing import List


class ElasticsearchCredentialGetter:
    def get_hosts(self) -> List[str]:
        return list(os.environ.get("ELASTICSEARCH_HOSTNAME").split(","))

    def get_username(self) -> str:
        return os.environ.get("ELASTICSEARCH_USERNAME")

    def get_password(self) -> str:
        return os.environ.get("ELASTICSEARCH_PASSWORD")
