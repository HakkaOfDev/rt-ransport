import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from tools.Keys import DEBUG

username = (os.getenv("DB_USERNAME"), "postgres")[DEBUG]
password = (os.getenv("DB_PASSWORD"), "admin")[DEBUG]
host = (os.getenv("DB_HOST"), "localhost")[DEBUG]
port = (os.getenv("DB_PORT"), 5432)[DEBUG]
dbname = (os.getenv("DB_NAME"), "rt-ransport")[DEBUG]
address = f'postgresql://{username}:{password}@{host}:{port}/{dbname}'

try:
    engine = create_engine(address, isolation_level='AUTOCOMMIT')
    Session = sessionmaker(bind=engine)
    Base = declarative_base()
except:
    print("Error during database connection..")
