import psycopg2
from psycopg2 import errors
import os

"""
Util class for PostgreSQL usage
Author: [Alestrio, Hakka]
Version: 0.1
"""
class SQLService:
    sql = None

    database_user = os.getenv('DATABASE_USER')
    database_password = os.getenv('DATABASE_PASSWORD')
    database_host = os.getenv('DATABASE_HOST')
    database_port = os.getenv('DATABASE_PORT')
    database_dbname = os.getenv('DATABASE_DBNAME')

    """Constructor"""
    def __init__(self) -> None:
        if self.sql is None:
            self.sql = psycopg2.connect(database=self.database_dbname,
                                        user=self.database_user,
                                        host=self.database_host,
                                        password=self.database_password,
                                        port=self.database_port)
        super().__init__()

    """Update method for send updatable queries (UPDATE/ DELETE)"""
    def update(self, query):
        cursor = self.sql.execute(query)
        cursor.commit()

    """Rows method returns fetchall"""
    def getRows(self, query):
        cursor = self.sql.execute(query)
        return cursor.fetchall()

    """Destructor"""
    def __del__(self):
        try:
            self.sql.close()
        except errors.ConnectionException as err:
            print(type(err))
