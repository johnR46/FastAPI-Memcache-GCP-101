import json

from pymemcache.client import base

from settings import MEMCACHE_SERVER, MEMCACHE_PORT

client = base.Client((MEMCACHE_SERVER, MEMCACHE_PORT))


def get_value_from_cache(key: str):
    print("get value from cache by key : {}".format(key))
    cache_value = client.get(key)
    if cache_value is None:
        return None
    return json.loads(cache_value)


def set_value_to_cache(key: str, value: any) -> None:
    print("set value to cache by key  : {} and value : {}".format(key, value))
    client.set(key, json.dumps(value), expire=60)
