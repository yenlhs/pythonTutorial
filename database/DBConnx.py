import mysql.connector
import configDB as cf

class DBConnx:

    cnx = ''

    def __init__(self):
        self.cnx = mysql.connector

    def createConnx(self):
        self.cnx = mysql.connector.connect(user=cf.username,password=cf.password,host=cf.host,database=cf.db)
        return self.cnx

    def closeConnx(self):
        self.cnx.close()


    
