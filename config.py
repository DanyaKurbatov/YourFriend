from pydantic import BaseSettings, PostgresDsn

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql://postgres:1q2w3e@localhost/pet'
    server_host: str = '127.0.0.1'
    server_port: int = 8000


settings = Settings(
    # _env_file='.env',
    # _env_file_encoding='utf-8'
)
