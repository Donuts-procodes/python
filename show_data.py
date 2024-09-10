import mysql.connector as mq
#from adodbapi.examples.db_table_names import databasename
try:
    obj=mq.connect(user='root',password='Franky@2003',database='base2', host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')
myc=obj.cursor()
s='SELECT * FROM table1'#select all form table
myc.execute(s)
row=myc.fetchall() #to get
for r in row:
    print(r)
myc.close()

obj.close()