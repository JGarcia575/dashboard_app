<div style="display:flex; justify-content: center; align-items: center;">

<img src="assets/banner.jpg" height=300 width=1000>

</div>

---

<div align="center">

<h1 align="center" style="font-family:roboto; font-weight:bold;">DASHBOARD APP</h1>

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-3.0.3-violet?logo=pandas)
![Seaborn](https://img.shields.io/badge/seaborn-0.13.2-blue?logo=seaborn)
![Streamlit](https://img.shields.io/badge/streamlit-1.58.0-red?logo=streamlit)
![Status](https://img.shields.io/badge/status-active-success)

</div>

## **Sobre el proyecto**

El proyecto es la continuación de los desafíos **_Telecom X Latinoamérica parte 1_** y **_parte 2_**. Aquí tomamos el análisis y modelado predictivo de los dos proyectos mencionados y los ponemos en una aplicación web que consiste de un dasboard interativo hecho con la tecnología Streamlit.

La empresa de telecomunicaciones **_Telecom X Latinoamérica_** está enfrentando una alta tasa de cancelación y necesita, en primer lugar, comprender los factores que llevan a la pérdida de clientes y, en segundo lugar, anticiparse al problema de la cancelación. El challenge parte 1 consistió en recopilar, procesar y analizar los datos con el objetivo de identificar los factores que influyen en la baja de clientes. Una vez indentificados los patrones o tendencias que llevan a las personas a cancelar los servicios de la empresa, desarrollamos modelos de clasificación capaces de prever qué clientes tienen mayor probabilidad de cancelar sus servicios. 

El proyecto responde a la necesidad de poner las soluciones encontradas en los desafíos anteriores en una aplicación web que sea de fácil acceso.

La **Dashaboard App** tiene dos partes:
1. Análisis exploratorio de evasión de clientes.
2. Servicio de predicción de evasión.

## **Stack Tecnológico**

- Python.
- Streamlit.
- Matplotlib.
- Seaborn.
- Pandas.
- Scki-learn.

## **Estructura del proyecto**
```
proyecto/
│
├── app.py
├── index.py
├── analisis.py
├── modelo.py #próximamente
├── servicio_prediccion.py #proximamente
└── assets/               
|    └── banner.jpg
|___ requirements.txt    
```
## **Instalación y ejecución del proyecto**

1. En una terminal ejecute el siguiente comando para cloner el repositorio.

    ```bash
    git clone dashboard_app.git
    ```
2. En la misma carpeta donde descargo el repositorio, volver abrir una terminal y ejecutar el siguiente
comando para instalar las dependencias del proyecto.

    **En Windows**

    ```bash
    pip install -r requirements.txt
    ```

    **En Linux**
    ```bash
    pip3 install -r requirements.txt
    ```

3. Luego, para correr la aplicación ejecute lo siguiente.

    ```bash
    streamlit run app.py
    ```

## **Funcionalidades**

Las funcionalidades del proyecto son las siguientes:

- Filtración interactiva por factor de la tasa de evasión de clientes.
- Reporte de patrones de evasión y recomendaciones para mitigar el problema.
- Servicio de predicción de evasión.

## **Live Demo**

_Próximamente_

## **Autores**

Jimena García

