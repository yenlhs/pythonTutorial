import mysql.connector
import configDB as cf
from mysql.connector import errorcode



def createConn():
    #try:
    #cnx = mysql.connector.connect(user=cf.username,password=cf.password,host=cf.host,database=cf.db)
    cnx = mysql.connector.connect(user=cf.username,password=cf.password,host=cf.host,database=cf.db)
    return cnx
        # cur = cnx.cursor()
        # cur.execute("select * from test")
        # for col1,col2 in cur:
        #     print(col1,col2)

    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your username and password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    # else:
    #     cnx.close()

a = createConn()
cur = a.cursor()
cur.execute("select * from test")        
for col1,col2 in cur:
    print(col1,col2)

cur.close()
createConn().close









