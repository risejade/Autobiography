import streamlit as st
from Home import render_home
from AboutMe import render_about_me
from Hobbies import render_hobbies
from Projects import render_projects
from Contact import render_contact
from EducationalBg import render_educationalBg
import pathlib

st.set_page_config(
    page_title="Rise Jade Benavente's Portfolio",
    page_icon=":tada:",
    layout="wide"
)

st.markdown(
    """
    <style>
    .css-1c5r7sm {
        font-size: 30px; /* Adjust the font size of the selectbox */
    }
    .css-1d391kg {
        font-size: 30px; /* Adjust the font size of the selectbox options */
    }
    .css-18e3b3p {
        font-size: 30px; /* Adjust the font size of the selectbox */
    }
    </style>
    """,
    unsafe_allow_html=True
)

option = st.selectbox(
    "Navigate to",
    ["🏠 Home", "👤 About Me", "🏀 Hobbies", "💼 Portfolio", "🎓 Educational Background", "📧 Contact"],
)

if option == "🏠 Home":
    st.session_state.page = "home"
    render_home()
elif option == "👤 About Me":
    st.session_state.page = "about_me"
    render_about_me()
elif option == "🏀 Hobbies":
    st.session_state.page = "hobbies"
    render_hobbies()
elif option == "💼 Portfolio":
    st.session_state.page = "portfolio"
    render_projects()
elif option == "🎓 Educational Background":
    st.session_state.page = "education"
    render_educationalBg()
elif option == "📧 Contact":
    st.session_state.page = "contact"
    render_contact()
