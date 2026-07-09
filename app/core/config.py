from pydantic_settings import BaseSettings, SettingsCongigDict


class Settings(BaseSettings):
    app_name: str = "Task API"
    database_url: str = "sqlite:///tasks.db"

    model_config = SettingsCongigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()