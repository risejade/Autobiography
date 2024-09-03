import streamlit as st
from PIL import Image

def render_hobbies():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Hobbies 🏍️</h2>
            <p>When I’m not coding, you can find me indulging in my passion for motorcycles. I love exploring new rides and experiencing the thrill of the open road. It’s a great way to unwind and enjoy the journey.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <h3>My Hobbies Include:</h3>
            <ul style="list-style-type:none; padding: 0;">
                <li>Motorcycle Enthusiast🏍️</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


    image_paths = [
        "C:/School/GitHub/sampleStream/images/hobby1.jpg",
        "C:/School/GitHub/sampleStream/images/hobby2.jpg",
        "C:/School/GitHub/sampleStream/images/hobby3.jpg",
        "C:/School/GitHub/sampleStream/images/hobby4.jpg"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        img = Image.open(image_paths[0])
        st.image(img, use_column_width=True)

    with col2:
        img = Image.open(image_paths[1])
        st.image(img, use_column_width=True)

    with col3:
        img = Image.open(image_paths[2])
        st.image(img, use_column_width=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.image(Image.open(image_paths[3]), use_column_width=True)
