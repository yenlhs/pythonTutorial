import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='yen',password='Service1',host='10.1.1.9',database='eprog')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username and password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()