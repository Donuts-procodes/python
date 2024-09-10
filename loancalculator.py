import streamlit as st
#
#from pygments.styles.light import background
st.title("loan calculator")
amt=st.number_input("Amount of loan:")
year=st.number_input("total years:")
x=st.button("calculate")
if x==1:
    st.write("your monthly installments are:",(amt/(year*12))+amt*(12/100))