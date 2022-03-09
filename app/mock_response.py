import time

fake_data = [
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": True
    },
    {
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": False
    }
]


def get_todo_all():
    # mock a time 2 sec wait response
    time.sleep(2)
    return fake_data


def get_todo_by_id(todo_id: int):
    # mock a time 1 sec wait response
    time.sleep(1)
    return [_ for _ in fake_data if todo_id == _.get('id')]
