import streamlit as st

#take a user input\
name=st.text_input("Enter your name")

st.title("Take the input")

if st.button("Submit"):
  st.write(f"Print the name: {name}")
