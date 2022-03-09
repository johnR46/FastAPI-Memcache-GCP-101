from fastapi import APIRouter

from app.cache_util import get_value_from_cache, set_value_to_cache
from app.mock_response import get_todo_all, get_todo_by_id

router = APIRouter(
    prefix="/todo",
    tags=["/have-cache/todos"],
    responses={404: {"message": "Not found"}}
)


@router.get("/find/all")
async def find_all():
    key = "find_all"
    cache_value = get_value_from_cache(key)
    if cache_value is None:
        response = get_todo_all()
        set_value_to_cache(key, response)
        return response
    else:
        return cache_value


@router.get("/find/{todo_id}")
async def find_by_id(todo_id: int):
    key = "find_by_id:{}".format(todo_id)
    cache_value = get_value_from_cache(key)
    if cache_value is None:
        response = get_todo_by_id(todo_id)
        set_value_to_cache(key, response)
        return response
    else:
        return cache_value
