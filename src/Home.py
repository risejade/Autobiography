import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def render_home():
    col1, col2, col3 = st.columns([1, 2, 1])  

    with col1:
        left_image_path = "C:/School/GitHub/sampleStream/images/codingGIF.gif"
        left_image = Image.open(left_image_path)

        base_width = 600  
        w_percent = (base_width / float(left_image.size[0]))
        h_size = int((float(left_image.size[1]) * float(w_percent)))
        resized_left_image = left_image.resize((base_width, h_size), Image.LANCZOS)

        left_image_base64 = image_to_base64(resized_left_image)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin: 10px; animation: fadeIn 2s;">
                <img src="data:image/gif;base64,{left_image_base64}" style="
                    max-width: 100%; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.5); 
                    transition: transform 0.3s ease-in-out;
                " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
            </div>
            <style>
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style="padding: 20px; text-align: center;">
                <h1 style="
                    font-size: 50px; 
                    font-weight: bold; 
                    color: #ffcc00; 
                    font-family: 'Poppins', sans-serif; 
                    margin-bottom: 10px;
                    text-transform: uppercase;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    animation: slideIn 2s;
                    text-align: center;
                    ">
                    Welcome to My Portfolio! 👋
                </h1>
            <style>
            @keyframes slideIn {{
                from {{ transform: translateY(-50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            @keyframes fadeInText {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    with col3:
        right_image_path = "C:/School/GitHub/sampleStream/images/uiDevGIF.gif"
        right_image = Image.open(right_image_path)

        base_width = 300 
        w_percent = (base_width / float(right_image.size[0]))
        h_size = int((float(right_image.size[1]) * float(w_percent)))
        resized_right_image = right_image.resize((base_width, h_size), Image.LANCZOS)

        right_image_base64 = image_to_base64(resized_right_image)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin: 10px; animation: fadeIn 2s;">
                <img src="data:image/gif;base64,{right_image_base64}" style="
                    max-width: 100%; 
                    border-radius: 15px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.5); 
                    transition: transform 0.3s ease-in-out;
                " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
            """
                <div style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    margin: 20px;
                ">
                    <p style="
                        font-size: 20px; 
                        line-height: 1.8; 
                        color: white; 
                        font-family: 'Poppins', sans-serif; 
                        max-width: 1000px;
                        background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.4));
                        border-radius: 20px;
                        padding: 20px;
                        margin: 0; /* Reset margin */
                        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
                        animation: fadeInText 2s ease-in;
                        transition: transform 0.3s ease-in-out;
                    ">
                        Hello! I’m Rise Jade Benavente. 
                        I’m excited to share my journey with you. 
                        Explore my skills as a Developer, Designer, 
                        Analyst, and Programmer, and see some of the projects 
                        I’m passionate about. Feel free to reach out if you 
                        have any questions or just want to connect! :star:
                    </p>
                </div>
                <div style="padding: 20px; text-align: center;">
                    <p style="
                        font-size: 20px; 
                        line-height: 1.8; 
                        color: white; 
                        font-family: 'Poppins', sans-serif; 
                        margin: 20px 0;
                        animation: fadeInText 2s ease-in;
                        ">
                        <em>"Strive not to be a success, but rather to be of value." – Albert Einstein</em>
                    </p>
                </div>
            <style>
            @keyframes slideIn {{
                from {{ transform: translateY(-50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            @keyframes fadeInText {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
