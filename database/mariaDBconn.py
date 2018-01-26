from MyDatabase import MyDB
sqlline = """select * from employees"""
a = MyDB()

a.query(sqlline)

# result = a.listColumns()
# for column in result:
#     print(column)


#returns all the data from the execution of the query above
result = a.getalldata()

for row in result:
    print(row)


#this is going to delete the database object
a.__del__
