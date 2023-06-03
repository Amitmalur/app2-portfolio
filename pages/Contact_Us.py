import streamlit as st

st.header("Contact Us")

with st.form(key="myForm"):
    user_name = st.text_input("Your Email Address")
    message = st.text_area("Your Message Here")
    button = st.form_submit_button("Submit")
    if button:
        message = message + user_name
        print("button clicked")
