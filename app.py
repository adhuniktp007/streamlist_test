import streamlit as st

st.title("Take the input")

#take a user input\
name=st.text_input("Enter your name")

if st.button("Submit"):
  st.write(f"Print the name: {name}")
