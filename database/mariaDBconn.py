from MyDatabase import MyDB
sqlline = """select * from employees"""
a = MyDB()

insert_new_salary = (
  "INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) "
  "VALUES (1804, 'Li-Hung-Shun', 'Adrian', 'x1234', 'yenlhs@gmail.com', '4', '1102', 'Sales Rep')")

a.query(insert_new_salary)
a.dbcommit()

#this is going to delete the database object
a.__del__
