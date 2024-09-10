import mysql.connector as mq
try:
    obj=mq.connect(user='root',password='Franky@2003',host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')

myc=obj.cursor()
myc.execute('CREATE DATABASE base2')
myc.close()
obj.close()