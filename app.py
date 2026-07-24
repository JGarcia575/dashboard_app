import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.set_page_config(layout="wide")

st.title(":rainbow[DASHBOARD APP]", text_alignment='center')

st.subheader(":violet[**Descripción del proyecto**]", divider="rainbow")

proyecto = '''
El proyecto es la continuación de los desafíos **_Telecom X Latinoamérica parte 1_** y **_parte 2_**. Aquí tomamos el análisis y modelado predictivo de los dos proyectos mencionados y los ponemos en una aplicación web que consiste de un dasboard interativo hecho con la tecnología Streamlit.

La empresa de telecomunicaciones **_Telecom X Latinoamérica_** está enfrentando una alta tasa de cancelación y necesita, en primer lugar, comprender los factores que llevan a la pérdida de clientes y, en segundo lugar, anticiparse al problema de la cancelación. El challenge parte 1 consistió en recopilar, procesar y analizar los datos con el objetivo de identificar los factores que influyen en la baja de clientes. Una vez indentificados los patrones o tendencias que llevan a las personas a cancelar los servicios de la empresa, desarrollamos modelos de clasificación capaces de prever qué clientes tienen mayor probabilidad de cancelar sus servicios. 

El proyecto responde a la necesidad de poner las soluciones encontradas en los desafíos anteriores en una aplicación web que sea de fácil acceso.

La **Dashaboard App** tiene dos partes:
1. Análisis exploratorio de evasión de clientes.
2. Servicio de predicción de evasión.

'''
st.markdown(proyecto)

pages = {
    "Acerca de": [
        st.Page("app.py", title="Dashboard App")
    ],
    "Servicios": [
        st.Page("analisis.py", title="Analisis exploratorio")
    ]
}

pg = st.navigation(pages)

pg.run()
