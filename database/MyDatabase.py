import mysql.connector
from mysql.connector import errorcode
import configDB as cf

class MyDB:
    _db_connection = None
    _db_cur = None

    def __init__(self):
        try:
            self._db_connection = mysql.connector.connect(user=cf.username,password=cf.password,host=cf.host,database=cf.db)
            self._db_cur = self._db_connection.cursor()
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username and password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        # else:
        #     self._db_connection.close()


    def query(self, query):
        return self._db_cur.execute(query)

    def getalldata(self):
        return self._db_cur.fetchall()

    # def listColumns(self):
    #     return self._db_cur.column_names()

    def __del__(self):
        self._db_connection.close()