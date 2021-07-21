from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql://postgres:1q2w3e@localhost/pet'
    server_host: str = '127.0.0.1'
    server_port: int = 8000


settings = Settings(
    # _env_file='.env',
    # _env_file_encoding='utf-8'
)
