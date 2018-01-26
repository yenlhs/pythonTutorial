import cx_Oracle as cO
import configDB as cf

class MyDB:
    _db_connection = None
    _db_cur = None

    def __init__(self):
        
        self._db_connection = cO.connect('yen/Service1@node1/eprog)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        return self._db_cur.execute(query)

    def getalldata(self):
        return self._db_cur.fetchall()

    def listColumns(self):
        return self._db_cur.column_names()

    def dbcommit(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()