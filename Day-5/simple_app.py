import streamlit as st
st.title("My first streamlit App!!!")
st.write("Welcome to my AI application!")
st.header("CHATBOT")
st.subheader("Siimple_app")
name = st.text_input("Enter your name: ")
if st.button("Sumbit"):
    st.write("Hello", name)