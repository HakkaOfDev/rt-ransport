import psycopg2
from psycopg2 import errors


class SQLService:
    """
    Util class for PostgreSQL usage
    Author: [Alestrio, Hakka]
    Version: 0.1
    """

    sql = None
    cursor = None

    def __init__(self) -> None:
        """
        Constructor
        """
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
            if self.cursor is None:
                self.cursor = self.sql.cursor()

        super().__init__()

    def update(self, query, params=None):
        """
        Update method for send updatable queries (UPDATE/ DELETE)

        :param query:
        :param params:
        """
        self.cursor.execute(query, params)
        self.sql.commit()

    def getRows(self, query, params=None):
        """
        Rows method returns fetchall

        :param query:
        :param params:
        :return []:
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def get(self, query, params=None):
        """
        Get row from any queries

        :param query:
        :param params:
        :return {}:
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def ifPresent(self, query, params=None):
        """
        Check if data is in any tables

        :param query:
        :param params:
        :return boolean:
        """
        self.cursor.execute(query, params)
        if self.cursor.fetchone():
            return True
        else:
            return False

    def __del__(self):
        """
        Destructor
        """
        try:
            self.cursor.close()
            self.sql.close()
        except errors.ConnectionException as err:
            print(type(err))
