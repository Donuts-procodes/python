import mysql.connector as mq
#from adodbapi.examples.db_table_names import databasename

try:
    obj=mq.connect(user='root',password='Franky@2003',database='base2', host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')
s='INSERT INTO table1(name,id,salary) VALUES("aman",1223,500300)'
myc=obj.cursor()
myc.execute(s)
obj.commit() #save changes
myc.close()
obj.close()