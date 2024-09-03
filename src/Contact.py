import streamlit as st

def render_contact():
    st.header("Contact Me :email:")
    st.write("If you'd like to get in touch with me, please fill out the form below:")

    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            st.write("Thank you for your message! I will get back to you soon.")
