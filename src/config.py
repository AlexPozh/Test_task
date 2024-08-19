from environs import Env

from dataclasses import dataclass

env = Env()

env.read_env()

@dataclass
class DatabaseConfig:
    __name_db: str = env("DB_NAME")
    __user_db: str = env("DB_USER")
    __password_db: str = env("DB_PASSWORD")
    __port_db: int = env("DB_PORT")
    __host_db: str = env("DB_HOST")

    @property
    def dsn(self):
        return f"postgresql+asyncpg://{self.__user_db}:{self.__password_db}@postgres_db:{self.__port_db}/{self.__name_db}"