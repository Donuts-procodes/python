import mysql.connector as mq
import streamlit as st

try:
    obj=mq.connect(user='root',database='base2',password='Franky@2003',host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')
s=('INSERT INTO tabel10(name,age)VALUES("abcd",22),("xyz",23)')
myc=obj.cursor()
myc.execute(s)
obj.commit()