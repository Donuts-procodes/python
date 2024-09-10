import mysql.connector as mq
import streamlit as st
import pandas as pd

try:
    obj = mq.connect(user='root',database="base2", password='Franky@2003', host='localhost', port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')

myc = obj.cursor()
myc.execute("SELECT * FROM table3")
data = myc.fetchall()
for i in data:
    print(i)

st.title("MySQL database")
df = pd.DataFrame(data)
st.write(df)

def main():
    st.title("Operations With MySQL")
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        age=st.number_input("Enter age")
        if st.button("Create"):
            sql= "insert into table3(name,age) values(%s,%s)"
            val= (name,age)
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Created Successfully!!!")
    elif option=="Read":
        st.subheader("read the record")
        myc.execute("SELECT * FROM table3")
        data = myc.fetchall()
        for i in data:
            st.write(i)
    elif option == "Update":
        st.subheader("Update a Record")

        old_name = st.text_input("Enter Old Name")  # Input for the old name
        new_name = st.text_input("Enter New Name")  # Input for the new name

        if st.button("Update"):
            sql = "UPDATE table3 SET name=%s WHERE name=%s"
            val = (new_name, old_name)  # Use both old and new names in the query
            myc.execute(sql, val)
            obj.commit()
            st.success("Record Updated Successfully!!!")

    elif option == "Delete":
        age = st.number_input("Enter age", min_value=1)
        if st.button("Delete"):
            sql = "DELETE FROM table3 WHERE age=%s"
            val = (age,)
            myc.execute(sql, val)
            obj.commit()
            st.success("Record Deleted Successfully!")

if __name__ == "__main__":
    main()
    # obj.close()
    # myc.close()