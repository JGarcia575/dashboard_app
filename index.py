import streamlit as st

st.title("​📊:rainbow[**DASHBOARD APP**]", text_alignment='center')

st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 1.2rem;'>Sistema Integral de Análisis y Predicción de Churn</p>", 
    unsafe_allow_html=True
)

st.subheader("📌 Descripción del Proyecto", divider="rainbow")

st.markdown(
    """
    Este proyecto es la continuación y evolución de los desafíos **Telecom X Latinoamérica (Parte 1 y Parte 2)**. 
    Aquí unimos el análisis exploratorio de datos y el modelado predictivo en una aplicación web interactiva 
    desarrollada con **Streamlit**.
    """
)

# Uso de columnas para organizar visualmente el contexto
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("### 🏢 El Reto de Negocio")
    st.markdown(
        """
        La empresa de telecomunicaciones **Telecom X Latinoamérica** enfrenta una alta tasa de cancelación (*churn*). 
        El objetivo principal es doble:
        1. **Comprender** en profundidad los factores que impulsan la baja de clientes.
        2. **Anticiparse** al problema mediante modelos predictivos de Machine Learning.
        """
    )

with col2:
    st.markdown("### 🛠️ Fases del Desarrollo")
    st.markdown(
        """
        * **Challenge Parte 1 (EDA):** Recopilación, limpieza y análisis de patrones de comportamiento para identificar tendencias de cancelación.
        * **Challenge Parte 2 (ML):** Entrenamiento y evaluación de modelos de clasificación para prever riesgos futuros de pérdida de clientes.
        """
    )

st.markdown("---")
st.subheader("🚀 Servicios Disponibles en la App")

# Tarjetas visuales para los dos servicios principales
col_s1, col_s2 = st.columns(2)
with col_s1:
    st.info("📈 **Análisis Exploratorio de Evasión**\n\nVisualizaciones interactivas y métricas clave sobre el comportamiento histórico de los clientes de telecomunicaciones.")
with col_s2:
    st.success("⚡ **Servicio de Predicción**\n\nInterfaz orientada al usuario para consultar la probabilidad de cancelación de clientes utilizando el modelo entrenado.")

st.markdown("---")
st.subheader("🔗 Enlaces a los Repositorios del Código Fuente")

# Botones modernos para los enlaces de GitHub
col_l1, col_l2, _ = st.columns([1, 1, 2])
with col_l1:
    st.link_button("📂 Telecom X Parte 1 (EDA)", "https://github.com/JGarcia575/challenge_telecomX.git.git", use_container_width=True)
with col_l2:
    st.link_button("📂 Telecom X Parte 2 (ML)", "https://github.com/JGarcia575/challenge_telecomX_parte_2.git", use_container_width=True)