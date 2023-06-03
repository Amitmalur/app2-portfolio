import streamlit as st
from send_email import email_send

st.header("Contact Us")

with st.form(key="myForm"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message Here")
    message = f"""\
Subject: New email from {user_email}

from: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        email_send(message)
        st.info("Yor email was sent successfully!")
