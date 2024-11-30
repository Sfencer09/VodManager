from dataclasses import dataclass
from app.models.config.PostgresConfig import PostgresConfig

@dataclass
class VodmConfigOptions:
    postgres_config: PostgresConfig
    