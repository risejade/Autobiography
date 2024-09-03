import streamlit as st
from PIL import Image

def render_projects():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Portfolio</h2>
            <p>Here are some of the projects I've worked on:</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    projects = {
        "Project 1: ClassConnect 💻": {
            "description": """
            Developed a bot using Puppeteer that logs into an AIMS (Academic Information Management System)
            and scrapes necessary information for integration with other systems.
            """,
            "image_path": "C:/School/GitHub/sampleStream/images/classconnect.png"
        },
        "Project 2: CampusCompass 💻": {
            "description": """
            CampusCompass simplifies navigating CIT-U by eliminating the need to ask for directions. 
            It features a real-time tracker to show your current location, making campus navigation seamless.
            """,
            "image_path": "C:/School/GitHub/sampleStream/images/campuscompass.png"
        },
        "Project 3: Bus Reservation System 💻": {
            "description": """
            Created a bus reservation system to streamline the booking process. The system allows users to reserve seats on buses 
            and manage their bookings efficiently.
            """,
            "image_path": "C:/School/GitHub/sampleStream/images/BRS.png"
        }
    }

    for title, details in projects.items():
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h3>{title} </h3>
                <p>{details['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        img = Image.open(details['image_path'])
        st.image(img, use_column_width=True)

    st.markdown(
        """
        <div style="text-align: center;">
            <p>Explore the projects on GitHub:</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("View System Integration Bot on GitHub"):
            st.write("[GitHub Repository](https://github.com/gabrielrago/ClassConnect)")

    with col2:
        if st.button("View CampusCompass on GitHub"):
            st.write("[GitHub Repository](https://github.com/risejade/CampusCompassFrontend)")

    with col3:
        if st.button("View Bus Reservation System on GitHub"):
            st.write("[GitHub Repository](https://github.com/risejade/BusReservationSystem)")
