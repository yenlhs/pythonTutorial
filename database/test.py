from MyDatabase import MyDB

connx = MyDB()

sql='select # from employees'
connx.query(sql)

print(connx.getalldata())

connx.dbclose()
# 