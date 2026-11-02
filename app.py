import streamlit as st
from footer import render_footer
from header import render_banner

render_banner()

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

render_footer()