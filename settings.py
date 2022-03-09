import os

MEMCACHE_SERVER = os.getenv("MEMCACHE_SERVER", "localhost")
MEMCACHE_PORT = os.getenv("MEMCACHE_PORT", "11211")
