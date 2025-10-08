from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):  # < BaseModel
    driver: str = 'postgresql'
    host: str = 'localhost'
    port: int
    database: str = 'temp_database'
    user: str = 'postgres'
    password: SecretStr
    model_config = SettingsConfigDict(
        env_prefix='db_',
    )

    @property
    def url(self):
        print(f'{type(self.port)=}')  # Автоматическая конвертация типов
        return f'{self.driver}://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.database}'

    model_config = SettingsConfigDict(
        env_file='.env.example',
        env_file_encoding='utf-8',
        env_prefix='db_',
    )


class Settings(BaseSettings):  # < BaseSettings
    db: DatabaseSettings
    debug: bool
    defval: str = 'value1'

    model_config = SettingsConfigDict(
        env_file='.env.example',
        env_file_encoding='utf-8',
        env_prefix='app_',
        env_nested_delimiter='__',
    )


settings = Settings()

print(f'{settings.db.url=}')
print(f'{settings.debug=}')
print(f'{settings.defval=}')
