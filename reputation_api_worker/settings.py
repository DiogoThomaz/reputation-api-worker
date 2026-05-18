import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    broker_url: str | None
    database_url: str | None
    redis_url: str | None
    sentry_dsn: str | None


def get_settings() -> Settings:
    # Defaults seguros; segredos vêm de variáveis de ambiente via runtime/CI
    return Settings(
        environment=os.getenv("ENVIRONMENT", "development"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        broker_url=os.getenv("BROKER_URL"),
        database_url=os.getenv("DATABASE_URL"),
        redis_url=os.getenv("REDIS_URL"),
        sentry_dsn=os.getenv("SENTRY_DSN"),
    )