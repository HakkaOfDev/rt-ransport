from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "guser"
password = "banane1"
host = "10.59.63.32"
port = 5432
dbname = "rtransport"
address = f'postgresql://{username}:{password}@{host}:{port}/{dbname}'

try:
    engine = create_engine(address, isolation_level='AUTOCOMMIT') # moteur de connection à la bdd
    Session = sessionmaker(bind=engine) # création de la session principale
    Base = declarative_base() # déclaration de la base (link les ORM)
except:
    print("Error during database connection..")
