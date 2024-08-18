from sqlalchemy import select, insert, column


from db.db_helper import db_helper
from db.models import Estate

from find_estate.shemas import QueryModel


async def get_data(cadastral_num: str | None = None):

    try:
        async with db_helper.session_maker() as session:
            if cadastral_num is None:
                stmt = select(Estate)
                result = await session.execute(stmt)
                # data = [row for row in result ]
                # print(data)
                return result.scalars().all()
            # Выбираем все записи с указанным кадастровым номером
            else:
                stmt = select(Estate).where(Estate.cadastral_num == cadastral_num)
                result = await session.execute(stmt)
                # data = [row for row in result ]
                return result.scalars().all()

    except Exception as error:
        print(error)


async def create_data(query: QueryModel, server_answer: bool):
    try:
        new_estate = Estate(
            cadastral_num=query.cadastral_num,
            latitude=query.latitude,
            longitude=query.longitude,
            server_answer=server_answer
        )
        
        async with db_helper.session_maker() as session:
            session.add(new_estate)
            await session.commit()

    except Exception as error:
        print(error)