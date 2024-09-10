import streamlit as st
from docutils.nodes import option

st.title("my first app")
st.write("hello all")
#st.balloons()
x=st.text_input("which technology you want to learn")
if x=='ai':
    st.write("kindly enroll in python first")
y=st.radio("are you graduate?" ,options=['yes','no'])
if y=='yes':
    st.write("you can enroll")
elif y=="no":
    st.write("you cannot")
a=st.button("show")
if a==1:
    st.write("hello")
z=st.selectbox("select the tecnology",('Python','C++','Java'))
if z=='Python':
    st.write("contact 1")
if z=='C++':
    st.write("contact 2")
if z=='Java':
    st.write("contact 3")