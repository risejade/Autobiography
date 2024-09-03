import streamlit as st
from PIL import Image

st.set_page_config(page_title="About Me", page_icon=":camera:", layout="wide")

def render_about_me():
    img_aboutme1 = Image.open("images/aboutme1.jpg")
    img_aboutme2 = Image.open("images/aboutme2.jpg")
    img_aboutme3 = Image.open("images/aboutme3.jpg")
    img_aboutme4 = Image.open("images/aboutme4.jpg")
    img_friends1 = Image.open("images/friends1.jpg")
    img_friends2 = Image.open("images/friends2.jpg")
    
    st.markdown(
        """
        <div style="padding: 20px; text-align: center; margin-top: -30px;">
            <h1 style="
                font-size: 50px; 
                font-weight: bold; 
                color: white; 
                font-family: 'Poppins', sans-serif; 
                margin-bottom: 10px;
                text-transform: uppercase;
                ">
                About Me
            </h1>
            <p style="
                font-size: 20px; 
                line-height: 1.8; 
                color: white; 
                font-family: 'Poppins', sans-serif; 
                margin: 0 auto;
                max-width: 500px;
                padding: 0;
                ">
                I am a 4th-year student aiming to be a software developer with a keen interest in software and web development. 
                I enjoy solving complex problems and building projects that have a real-world impact. 
            </p>
            <p style="
                font-size: 20px; 
                line-height: 1.8; 
                color: white; 
                font-family: 'Poppins', sans-serif; 
                margin: 0 auto;
                padding: 0;
                ">
                <em>"Strive not to be a success, but rather to be of value." – Albert Einstein :bulb:</em>
            </p>
            <hr style="border: 1px solid white; margin: 20px auto; width: 100%;"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(4)
    with cols[0]:
        st.image(img_aboutme1, use_column_width=True)
    with cols[1]:
        st.image(img_aboutme2, use_column_width=True)
    with cols[2]:
        st.image(img_aboutme3, use_column_width=True)
    with cols[3]:
        st.image(img_aboutme4, use_column_width=True)
    
    st.markdown(
        """
        <hr style="border: 1px solid white; margin: 20px auto; width: 100%;"/>
        <h2 style="
            font-size: 40px; 
            color: white; 
            font-family: 'Poppins', sans-serif; 
            margin-bottom: 20px;
            ">
            My Friends
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    cols = st.columns(2)
    with cols[0]:
        st.image(img_friends1, use_column_width=True)
    with cols[1]:
        st.image(img_friends2, use_column_width=True)
