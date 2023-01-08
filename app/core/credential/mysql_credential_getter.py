import os


class MySQLCredentialGetter:
    def get_username(self) -> str:
        return os.getenv("MYSQL_USERNAME", "user")

    def get_password(self) -> str:
        return os.getenv("MYSQL_PASSWORD", "pass")

    def get_hostname(self) -> str:
        return os.getenv("MYSQL_HOSTNAME", "localhost")

    def get_port(self) -> int:
        return os.getenv("MYSQL_PORT", 3306)

    def get_database_name(self) -> str:
        return os.getenv("MYSQL_DATABASE_NAME", "greeedy")
