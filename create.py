import mysql.connector as mq
#from adodbapi.examples.db_table_names import databasename

try:
    obj=mq.connect(user='root',password='Franky@2003',database='base2', host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')

s='CREATE TABLE table2(empid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),id INT,salary FLOAT,father VARCHAR(20))'
myc=obj.cursor()
myc.execute(s)
myc.close()
obj.close()