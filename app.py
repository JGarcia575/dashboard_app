import streamlit as st

pages = {
    "Acerca de": [
        st.Page("index.py", title="Dashboard App")
    ],
    "Servicios": [
        st.Page("analisis.py", title="Analisis exploratorio")
    ]
}

pg = st.navigation(pages)

pg.run()
