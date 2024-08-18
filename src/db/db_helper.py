from config import DatabaseConfig

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(
                            url=DatabaseConfig().dsn
                            )
        self.session_maker = async_sessionmaker(self.engine, expire_on_commit=False)
    

db_helper = DatabaseHelper()