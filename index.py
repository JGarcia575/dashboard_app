import streamlit as st

st.set_page_config(layout="wide")

st.title(":rainbow[DASHBOARD APP]", text_alignment='center')

st.subheader(":violet[**Descripción del proyecto**]", divider="rainbow")

st.html(
    '''
    <div>
        <p>El proyecto es la continuación de los desafíos <strong>Telecom X Latinoamérica parte 1</strong> y <strong>parte 2</strong>. Aquí tomamos el análisis y modelado predictivo de los dos proyectos mencionados y los ponemos en una aplicación web que consiste de un dasboard interativo hecho con la tecnología Streamlit.</p>

        <p>La empresa de telecomunicaciones <strong>Telecom X Latinoamérica</strong> está enfrentando una alta tasa de cancelación y necesita, en primer lugar, comprender los factores que llevan a la pérdida de clientes y, en segundo lugar, anticiparse al problema de la cancelación.</p> 
        
        <p> El <strong>challenge parte 1</strong> consistió en recopilar, procesar y analizar los datos con el objetivo de identificar los factores que influyen en la baja de clientes.  
            Una vez indentificados los patrones o tendencias que llevan a las personas a cancelar los servicios de la empresa, <strong>en la parte 2</strong> desarrollamos modelos de clasificación capaces de prever qué clientes tienen mayor probabilidad de cancelar sus servicios. 
        </p>

        <p>El proyecto responde a la necesidad de poner las soluciones encontradas en los desafíos anteriores en una aplicación web que sea de fácil acceso.
        
        <p> La Dashboard App tiene dos servicios principales</p>

        <ul>
            <li> Análisis exploratorio de evasión de clientes.</li>
            <li> Predicción de evasión.</li>
        </ul>

        <p>Si querés consultar el código de alguno de los desafíos podes consultar los siguientes enlaces</p>
        
        <a href="https://github.com/JGarcia575/challenge_telecomX.git" >Telecom X Latinoamérica parte_1</a>
        <a href="https://github.com/JGarcia575/challenge_telecomX_parte_2.git" >Telecom X Latinoamérica parte_2</a>


    </div>

    '''
)

st.divider()
