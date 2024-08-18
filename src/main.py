from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from find_estate.router import router as find_estate_router

# from admin.admin_panel import router as admin_router
from fastadmin import fastapi_app as admin_app

from db.db_helper import db_helper
from db.models import User, Base, Estate

from fastadmin import SqlAlchemyModelAdmin

from fastadmin import register

from sqlalchemy import select


@register(User, sqlalchemy_sessionmaker=db_helper.session_maker)
class UserModelAdmin(SqlAlchemyModelAdmin):
    list_display = ("id", "username", "is_superuser")
    list_display_links = ("id", "username")

    async def authenticate(self, username, password):
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            query = select(self.model_cls).filter_by(username=username, password=password, is_superuser=True)
            result = await session.scalars(query)
            obj = result.first()
           
            if not obj:
                return None
            return obj.id



@register(Estate, sqlalchemy_sessionmaker=db_helper.session_maker)
class EstateModelAdmin(SqlAlchemyModelAdmin):
    list_display = ("id", "cadastral_num", "latitude", "longitude", "server_answer")
    list_display_links = ("cadastral_num")





async def init_db():
    async with db_helper.engine.begin() as c:
        await c.run_sync(Base.metadata.drop_all)
        await c.run_sync(Base.metadata.create_all)


async def create_superuser():
    async with db_helper.session_maker() as s:
        user = User(
            username="admin",
            password="admin",
            is_superuser=True,
        )
        s.add(user)
        await s.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await create_superuser()
    yield



app = FastAPI(lifespan=lifespan)


app.include_router(find_estate_router)
# app.include_router(admin_router)

app.mount("/admin", admin_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
