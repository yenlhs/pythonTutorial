import cx_Oracle
import config as cf

connstr='scott/tiger'
cursor = cx_Oracle.Cursor(connstr)

cursor.execute(cf.sql)