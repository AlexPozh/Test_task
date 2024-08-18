from sqlalchemy import Boolean, DateTime,Integer, String,func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(length=255), nullable=False)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    async def __str__(self):
        return self.username
    
    @classmethod
    def get_model_name(cls):
        return f"sqlalchemy.{cls.__name__}"


class Estate(Base):
    __tablename__ = "estate"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    cadastral_num: Mapped[str] = mapped_column(String(length=32), nullable=False)
    latitude: Mapped[str] = mapped_column(String(length=32), nullable=True)
    longitude: Mapped[str] = mapped_column(String(length=32), nullable=True)
    server_answer: Mapped[bool] = mapped_column(Boolean)

    async def __str__(self):
        return self.cadastral_num

    @classmethod
    def get_model_name(cls):
        return f"sqlalchemy.{cls.__name__}"