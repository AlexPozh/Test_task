from fastapi import APIRouter

from find_estate.utills import external_server

from find_estate.shemas import QueryModel

from db.queries import create_data, get_data



router = APIRouter(prefix="")


@router.get("/query")
async def get_estate_by_cadastral_num(cadastral_num: str, latitude: str | None = None, longitude: str | None = None):
    
    # Эмуляция работы сервера
    server_answer: bool = await external_server()

    await post_result_cadastral_num(QueryModel(cadastral_num=cadastral_num, latitude=latitude, longitude=longitude), server_answer)

    return {
        "server_answer": server_answer
    }


@router.get("/ping")
async def check_server():
    return {
        "message": "Server is active."
    }


@router.post("/result")
async def post_result_cadastral_num(query: QueryModel, answer_server: bool):
    await create_data(
        query, 
        answer_server
    )


@router.get("/history")
async def get_requests_history(cadastral_num: str | None = None):
    
    # Эмуляция работы сервера
    # await external_server()

    result = await get_data(cadastral_num)
    print(result)
    return result
        
 
