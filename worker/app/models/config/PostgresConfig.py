from dataclasses import dataclass


@dataclass
class PostgresConfig:
    dbname: str
    user: str
    password: str
    host: str
    port: int = 5432