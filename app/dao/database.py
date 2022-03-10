from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DB_USER, DB_PASS, DB_URL

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}".format(DB_USER, DB_PASS, DB_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
