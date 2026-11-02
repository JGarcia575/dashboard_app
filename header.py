import streamlit as st

def render_banner():
    banner_html = """        
        <style>
            .banner-container {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                margin-bottom: 20px;
            }
            .banner-container img {
                max-width: 100%;
                height: auto;
                max-height: 600px; /* Ajusta esta altura máxima según tu preferencia */
                object-fit: cover;
                border-radius: 8px; /* Opcional: le da un toque más moderno con esquinas redondeadas */
            }
        </style>
        
        <div class="banner-container">
            <img src="https://raw.githubusercontent.com/JGarcia575/dashboard_app/refs/heads/main/src/header.jpg" alt="Banner del Proyecto">
        </div>
        """

    st.markdown(banner_html, unsafe_allow_html=True)
    