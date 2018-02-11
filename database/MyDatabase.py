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
            elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                print("Database is unavailable. It may be down")
            else:
                print("Something went wrong: {}".format(err))

    def query(self, query):
        try:
            return self._db_cur.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_PARSE_ERROR:
                print("Error in SQL statement")
        # except mysql.connector.Error as err:
        #     print(err)
        #     print(err.errno)
            

    def getalldata(self):
        try:
            return self._db_cur.fetchall()
        except:
            print("Unable to get data")

    def listColumns(self):
        return self._db_cur.column_names()

    def dbcommit(self):
        self._db_connection.commit()

    def dbclose(self):
        self._db_connection.close()

    # def __del__(self):
    #     self._db_connection.close()