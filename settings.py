import os

MEMCACHE_SERVER = os.getenv("MEMCACHE_SERVER", "localhost")
MEMCACHE_PORT = os.getenv("MEMCACHE_PORT", "11211")

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "sql12345")
DB_URL = os.getenv("DB_URL", "localhost:5432/postgres")
