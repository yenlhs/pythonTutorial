import cx_Oracle
import configDB as cf


class DBConnx:

    def __init__(self,cnx):
        self.cnx = cnx

    cnx = ''

    def createConnx():
        cnx = mysql.connector.connect(user=cf.username,password=cf.password,host=cf.host,database=cf.db)
        return cnx

    def closeConnx():
        cnx.clo
    
    def getDBData():


    
