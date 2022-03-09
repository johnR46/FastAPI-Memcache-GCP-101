import os

MEMCACHE_SERVER = os.getenv("_MEMCACHE_SERVER", "localhost")
MEMCACHE_PORT = os.getenv("_MEMCACHE_PORT", "11211")
