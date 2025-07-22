from pathlib import Path

from pydantic import conint, StrictStr, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="allow",
    )
    # database settings
    POSTGRES__HOST: StrictStr
    POSTGRES__PORT: conint(gt=1023, le=65535)
    POSTGRES__USER: StrictStr
    POSTGRES__PASSWORD: SecretStr
    POSTGRES__DATABASE_NAME: StrictStr
    POSTGRES__VOLUME_PATH: SecretStr
    POSTGRES__ECHO: bool = False

    # API settings
    API_V1_PREFIX: StrictStr = "/api/v1"

    # File settings
    BASE_DIR: Path = Path(__file__).parent.parent


SETTINGS = Settings()
