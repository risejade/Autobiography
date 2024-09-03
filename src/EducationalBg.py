import streamlit as st
from PIL import Image

def render_educationalBg():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Educational Background</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    education_data = [
        {
            "level": "Grade School",
            "years": "2008-2014",
            "school": "Basak Community School",
            "image_path": "C:/School/GitHub/sampleStream/images/bcs.jpg"
        },
        {
            "level": "Junior High School",
            "years": "2014-2018",
            "school": "Abellana National School",
            "honors": "With Honors",
            "image_path": "C:/School/GitHub/sampleStream/images/ans.jpg"
        },
        {
            "level": "Senior High School",
            "years": "2018-2020",
            "school": "Abellana National School - TVL Track Major in Automotive",
            "honors": "With Honors",
            "image_path": "C:/School/GitHub/sampleStream/images/ans.jpg"
        },
        {
            "level": "College",
            "years": "2021-Present",
            "school": "Cebu Institute of Technology - University",
            "image_path": "C:/School/GitHub/sampleStream/images/cit-u.png"
        }
    ]

    cols = st.columns(4)

    for i, edu in enumerate(education_data):
        col = cols[i]
        with col:
            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 20px; padding: 10px; border-radius: 8px; background-color: #f0f0f0; color: black;">
                    <h4 style="color: black;">{edu['level']}</h4>
                    <p><strong>Years:</strong> {edu['years']}</p>
                    <p><strong>School:</strong> {edu['school']}</p>
                    {"<p><em>Honors: " + edu['honors'] + "</em></p>" if "honors" in edu else ""}
                </div>
                """,
                unsafe_allow_html=True
            )

            if "image_path" in edu:
                img = Image.open(edu['image_path'])
                st.image(img, width=200)  
