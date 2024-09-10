import mysql.connector as mq
import streamlit as st

try:
    obj=mq.connect(user='root',database='base2',password='Franky@2003',host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')
s="CREATE TABLE table10(id int auto_increment primary key,name VARCHAR(20),age int)"
myc=obj.cursor()
myc.execute(s)