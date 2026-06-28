from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

# 设置 配置字典
class Settings(BaseSettings):
    HOST: str = Field(default="127.0.0.1")
    PORT: int = Field(default=8091)
    LOG_PATH: str | None = None
    DATABASE_PG_URL: str = Field(default="未定义")
    BASE_URL_ALI: str | None = None
    MODEL: str | None = None
    API_KEY_ALI: str | None = None
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
