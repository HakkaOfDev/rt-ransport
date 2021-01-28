import psycopg2
from psycopg2 import errors

"""
Util class for PostgreSQL usage
Author: [Alestrio, Hakka]
Version: 0.1
"""
class SQLService:
    sql = None

    """Constructor"""
    def __init__(self) -> None:
        database_user = "postgres"
        database_password = "alex&flo"
        database_host = "localhost"
        database_port = "5432"
        database_dbname = "rtransport"

        if self.sql is None:
            self.sql = psycopg2.connect(database=database_dbname,
                                        user=database_user,
                                        host=database_host,
                                        password=database_password,
                                        port=database_port)
        super().__init__()

    """Update method for send updatable queries (UPDATE/ DELETE)"""
    def update(self, query):
        cursor = self.sql.cursor()
        cursor.execute(query)
        cursor.commit()

    """Rows method returns fetchall"""
    def getRows(self, query):
        cursor = self.sql.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    """Destructor"""
    def __del__(self):
        try:
            self.sql.close()
        except errors.ConnectionException as err:
            print(type(err))
