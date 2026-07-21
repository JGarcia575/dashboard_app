import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns 

st.set_page_config(layout="wide")

st.title("📡​​:violet[**Telecom X: Análisis de Evasión de Clientes**]")

st.header("🔎 :violet[**Análisis Exploratorio de Datos (EDA)**]​​")

@st.cache_data
def cargar_datos():
    return pd.read_csv("telecom_clientes.csv")

df = cargar_datos()

df = df.drop(columns=["customerID", "Partner", "Dependents", "PaperlessBilling"])

if st.checkbox("Mostrar vista previa del dataset"):
    st.dataframe(df.head())

evasion_no, evasion_yes = df['Churn'].value_counts(normalize=True)

st.subheader(":violet[**Proporción de Clientes Evasores**]")

col1, col2 = st.columns(2)
col1.metric("⚠️​**Se fueron**⚠️", f'{round(evasion_yes * 100)} %', border=True)
col2.metric("💖​ **Se quedaron**",f' {round(evasion_no * 100)} %', border=True)

st.error(f'​🚨​ El porcentaje de clientes que se dieron de baja es aproximadamente **{round(evasion_yes * 100)}%**, una métrica que llama la atención.')

st.divider()

columnas_categoricas = ["Gender", 
                        "SeniorCitizen",
                        "PhoneService",
                        "MultipleLines",
                        "InternetService",
                        "Contract",
                        "PaymentMethod"]

filtro_1 = st.selectbox("Filtrar por categoría", columnas_categoricas)

df_filtrado = df[filtro_1]

tasa_evasion = pd.crosstab(df[filtro_1], df["Churn"], normalize='index')
    
tasa_evasion.sort_values(by='yes', ascending=True, inplace=True)

st.subheader(f"**Evasión por {filtro_1}**")

col_filtro_1, col_filtro_2 = st.columns(2)

with col_filtro_1:
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x=filtro_1, hue='Churn',palette='PiYG_r', ax=ax1)
    ax1.set_title("Cantidad de Clientes por Estado")
    ax1.set_xlabel(f'{filtro_1}')
    ax1.set_ylabel("Cantidad de Clientes")
    ax1.set_ylim(0,3000)
    plt.xticks(rotation=30, ha='right')
    st.pyplot(fig1)

with col_filtro_2:    
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=tasa_evasion, x=filtro_1, y='yes', hue=filtro_1, palette='Reds_d', ax=ax2)
    ax2.set_title(f'Tasa de evasión según {filtro_1}')
    ax2.set_xlabel(f'{filtro_1}')
    ax2.set_ylabel("Tasa de evasión(%)")
    ax2.set_ylim(0,1)
    ax2.axhline(y=evasion_yes, linestyle='dashed', linewidth=1.5, color='red')

    st.pyplot(fig2)

umbral_riesgo = round(evasion_yes,2)

factores_riesgo = []
factores_retencion = []

for categoria in tasa_evasion.index:
    tasa_categoria = tasa_evasion.loc[categoria, 'yes']

    texto_categoria = f"**{categoria}** ({round(tasa_categoria * 100, 1)}%)"
    
    if tasa_categoria > umbral_riesgo:
        factores_riesgo.append(texto_categoria)
    else:
        factores_retencion.append(texto_categoria)

col_diag1, col_diag2 = st.columns(2)

with col_diag1:
    if factores_riesgo:
        st.error("⚠️ **Factores de Alto Riesgo**")
        st.write("Las siguientes opciones superan la media de evasión de la empresa y requieren atención inmediata:")
        for item in factores_riesgo:
            st.markdown(f"- {item}")
    else:
        st.write("No se detectaron factores de riesgo en esta categoría.")

with col_diag2:
    if factores_retencion:
        st.success("💖 **Factores de Retención (Seguros)**")
        st.write("Estas opciones mantienen a los clientes fieles y presentan un comportamiento saludable:")
        for item in factores_retencion:
            st.markdown(f"- {item}")

st.divider()


st.warning(" ⚠️Por favor vaya a la sección recomendaciones⚠️")

st.divider()

columnas_numericas = ["Tenure", "ChargesMonthly", "ChargesTotal"]

col1, _ = st.columns([.5, .5])

with col1:
    filtro_2 = st.selectbox("Filtrar por categoría", columnas_numericas)

    st.subheader(f"**Evasión por {filtro_2}**")

    fig3, ax3 = plt.subplots(figsize=(6,4))

    ax3 = sns.boxplot(df, x='Churn', y=filtro_2, hue='Churn', palette='PiYG_r')
    ax3.set_title(f'Evasión por {filtro_2}', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Cancelación', fontsize=10, fontweight='bold')
    ax3.set_ylabel(f'{filtro_2}', fontsize=10, fontweight='bold')

    ax3.set_ylim(0, df[filtro_2].max())
    ax3.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax3.spines[['top', 'right']].set_visible(False)

    st.pyplot(fig3)

    st.warning("⚠️**Atención**⚠️")
    st.write("- Alertamos la presencia de **valores atípicos** para las variables **'_Tenure_'** y **'_ChargeTotal_'**.")
    st.write("- Hay que elegir un tratamiento para los valores atípicos o tomar como parámetro la mediana.")

st.divider()

#st.subheader(f"**Cantidad de servicios por estado**")


servicios = df[['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
       'TechSupport', 'StreamingTV', 'StreamingMovies']]

servicios_columnas = ['PhoneService', 
                      'MultipleLines', 
                      'OnlineSecurity', 
                      'OnlineBackup', 
                      'DeviceProtection',
                       'TechSupport', 
                       'StreamingTV', 
                       'StreamingMovies']

servicios[servicios_columnas] = np.where(servicios[servicios_columnas] == 'yes', 1, 0)

servicios['InternetService'] = np.where((df['InternetService'] == 'dsl') | (df['InternetService'] == 'fiber optic'), 1, 0)

servicios['Churn'] = np.where(df['Churn'] == 'yes', 1, 0)

servicios_columnas.append('InternetService')

servicios['numero_servicios'] = servicios[servicios_columnas].sum(axis=1)

col2, col3 = st.columns([.5, .5])

with col2:
    st.subheader(f"**Cantidad de servicios por estado**")

    fig4, ax4 = plt.subplots(figsize=(6,4))
    ax4 = sns.boxplot(servicios, x='Churn', y='numero_servicios', hue='Churn', palette='PiYG_r')
    ax4.set_title('Número de servicios por cliente ', fontsize=12, fontweight='bold' )
    ax4.set_xlabel('Baja', fontsize=10, fontweight='bold' )
    ax4.set_ylabel('Cantidad de servicios', fontsize=10, fontweight='bold')

    ax4.set_ylim(0, 10)
    ax4.yaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax4.spines[['top', 'right']].set_visible(False)

    st.pyplot(fig4)

    st.success("Factor de retención", icon="✅")

    st.write("- Los clientes que se fueron y los que se quedaron no difieren \n \
           en el número de servicios")

#st.divider()

#st.subheader("**Número de servicios y evasión**")

churn_servicios = pd.crosstab(servicios['numero_servicios'], servicios['Churn'], normalize='index')

churn_servicios.rename({0:'No', 1:'Yes'}, axis=1, inplace=True)

with col3:
    st.subheader("**Número de servicios y evasión**")

    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=churn_servicios, x=churn_servicios.index, y=churn_servicios['Yes'], hue=churn_servicios['Yes'], palette='Reds_d')
    ax5.axhline(y=evasion_yes, linestyle='dashed', linewidth=1.5, color='red')
    ax5.set_title('Tasa de evasión por número de servicios')
    ax5.set_xlabel('Número de servicios')
    ax5.set_ylabel("Tasa de evasión(%)")
    ax5.set_ylim(0,1)

    st.pyplot(fig5)

    st.error("⚠️**Factores de Alto Riesgo**")
    st.write("- Los clientes que tienen entre **2 a 5 servicios** tienen la mayor tasa de baja.")

st.divider()

servicios['Internet'] = df['InternetService']

sub_servicios = servicios[servicios['Churn'] == 1]

tab_servicios = pd.crosstab(sub_servicios['Internet'], sub_servicios['numero_servicios'], normalize='index')

col4, col5 = st.columns([.5, .5])


with col4:
    st.subheader(f"**Cantidad de servicios por tipo de internet**")

    fig5, ax5 = plt.subplots(figsize=(6,4))
    ax5 = sns.boxplot(sub_servicios, x='Internet', y='numero_servicios', palette='Reds_d')
    ax5.set_title('Distribución de servicios por tipo de internet', fontsize=12, fontweight='bold' )
    ax5.set_xlabel('Internet', fontsize=10, fontweight='bold' )
    ax5.set_ylabel('Cantidad de servicios', fontsize=10, fontweight='bold')

    ax5.set_ylim(0, 10)
    ax5.yaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax5.spines[['top', 'right']].set_visible(False)

    st.pyplot(fig5)

    st.error("⚠️**Factor de fuga**")

    st.write("- Los clientes con el plan de internet '_fibra óptica_' contrataron entre **2 a 6 servicios**.")
    st.write("- Los clientes con el plan '_dls_' contrataron entre **1 a 4 servicios**. ")
    st.write("- Los clientes que no contrataron internet tienen un solo servicio, posiblemente la línea telefónica.\n \
                El dato atípico puede corresponden a un cliente que contrato varias líneas telefónica." )


tenure_internet = df[['Tenure', 'InternetService', 'Churn']]

with col5:
    fig6, ax6 = plt.subplots()
    ax6 = sns.boxplot(tenure_internet, x='InternetService', y='Tenure', hue='Churn', palette='PiYG_r')
    ax6.set_title('Permanencia por servicio de internet', fontsize=12, fontweight='bold' )
    ax6.set_xlabel('Internet', fontsize=10, fontweight='bold' )
    ax6.set_ylabel('Permanencia', fontsize=10, fontweight='bold')

    ax6.set_ylim(0, 80)
    ax6.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    ax6.spines[['top', 'right']].set_visible(False)

    st.pyplot(fig6)

    st.error("⚠️**A tener en cuenta**")
    st.write("- Entre los distintos tipos de servicios de internet, los que optaron " \
     "por el plan fibra óptica se quedaron más tiempo (mediana 15 meses).")
    st.write("- Destacamos la presencia de valores atípicos para los segmentos _'dsl'_ y _'no interner service'_")

st.divider()

st.header("🤔​:violet[**Conclusiones**]")
st.html("<ul style='font-family: roboto; font-weight: bold;'>"
            "<li> ✅ El género no es un factor que influye en la fuga de clientes.</li>"
            "<br>"
            "<li> ❌ Los clientes mayores a 65 años tienen una alta tasa de renuncia(42%) en comparación con los clientes menores de 65 años(24%).</li>"
            "<br>"
            "<li> ❌ El tipo de contrato mensual, el método de pago cheque electrónico y el servicio de fibra óptica tienen tasas de cancelación mayor que el promedio.</li>"
            "<br>"
            "<li> ❓​ Los clientes que renunciaron a los servicios de la empresa pagaron mensualmente más que los clientes que no se fueron. Sin embargo, estos primeros pagaron menos de cargos total que los últimos. Esto se relaciona con el tiempo de permanencia de los clientes, y es que los clientes que se dieron de baja permanecieron menos tiempo que los que no se fueron. En promedio, se quedaron 18 meses.</li>"
            "<br>"
            "<li> ❌ El porcentaje de renuncia en el número de servicios es muy alto, 44% para aquellos clientes que no contrataron servicios adicionales de internet o de teléfono. También, destacan las tasas de baja entre los clientes que tenían entre 2 a 4 servicios, cuyas tasas son 33%, 36% y 31% para clientes con 2 servicios, 3 servicios y 4 servicios, respectivamente.</li>"
            "<br>"
            "<li> ❓​ Los clientes con fibra óptica contrataron desde 1 hasta 8 servicios con porcentajes más alto de contratación para 2, 3, 4 y 5 servicios.</li>"
            "<br>"
            "<li> ❓​Los clientes con el servicio de internet dsl contrataron desde el servicio básico hasta 8 servicios, teniendo las tasas más altas de contratación los clientes con 1, 2 y 3 servicios.</li>"
            "<br>"
            "<li> ❓​ Los clientes que no tenían internet, tenían exclusivamente el servicio telefónico.</li>"
            "<br>"
            "<li> ❌ Los clientes churners con pocos servicios tienden a permanecer menos tiempo en la empresa.</li>"

        "</ul>")

st.divider()

st.header("📖​✍️​:violet[**Implicaciones y recomendaciones**]")
st.html(
    '''
    <style>
        .recomendaciones { 
                    fontsize: 24px;
                    font-family: roboto;
                    font-weight: bold;
        }
    </style>"
    
    <p class="recomendaciones">A partir de los resultados se puede identificar que el problema de la evasión de clientes es un problema multicausal cuyas causas están relacionadas con la satisfacción de cada cliente con el servicio o los servicios contratados.

        En los resultados mencionamos cuales son los factores que se relacionan con la diserción de clientes y en este apartado abordamos que implica cada factor.

        El análisis de datos muestra que existen al menos dos perfiles evasores en relación a los tipos de servicios contratados, la permanencia de los clientes, el pago mensual, el total facturado y el número de servicios contratados. Estos tipos de clientes son:
    </p>
    <ol class="recomendaciones">
        <li>Los usuarios que contrataron fibra óptica y que tienen un paquete de servicios extras.</li>
        <li>Los usuarios que contrataron pocos servicios y de baja permanencia.</li>
        <li>Los primeros adquirieron principalemte entre 2 a 5 servicios extras. Esto indica que son personas con capacidad de pago, dado que los churners son las personas que más pagaron mensualmente. No obstante, se dan de baja porque no se encuentran satisfechos con los servicios contratados, principalmente con la fibra óptica.</li>
    </ol>
    <p class="recomendaciones">
         En los segundos usuarios, destacan aquellos con 0 servicios adicionales contratados, con una tasa de cancelación del 44%. En esta franja de clientes, se encuentran las personas que únicamente tenían internet dsl. Además, tenemos que resaltar los usuarios que cancelaron y que tenían un solo servicio. Aunque la tasa de cencelación no es la más alta, el 91% de estos tenían solo línea de teléfono. Las personas que contrataron dls y servicio de teléfono fueron los que menos tiempo perdudaron. Esto sugiere que la falta de un mayor número de servicios adicionales o una percepción de valor insuficiente en los servicios básicos los hace más vulnerables a la fuga."

         Otro perfil de churn son las personas mayores de 65 años. Estas tienen una tasa de churn que es aproximadamente el doble de la tasa de los menores de 65 años."

         Por último, esta el perfil de churn que se relaciona con las características contractuales. Dentro de este perfil se encuentran aquellos que tenían el tipo de contrato mensual y que pagaban a través de pago electrónico."

         Por lo tanto, hacemos las siguientes recomendaciones para abordar las cancelaciones en función de cada tipo de perfil identificado:

    </p>
    <ul class="recomendaciones">
        <li>Mejorar la calidad del servicio fibra óptica, realizando una investigación sobre la experiencia del cliente con este servicio. Esto puede lograrse a través de encuestas, monitoreo de la velocidad y la eficiencia del soporte técnico.</li>
        <li>Ofrecer promociones atractivas para clientes con muy pocos servicios. Esto puede conseguirse a través de paquetes de servicios, por ejemplo internet + teléfono o internet + servicio de streaming. Al adquirir estos paquetes, también se les puede otorgar bonificaciones a los clientes para que tengan un tiempo de prueba.</li>
        <li>Atención específica al segmento etario mayor de 65 años. Elaborar estrategias comerciales y de servicio técnico exclusivamente para esta porción de demográfica.</li>
        <li>Optimización de métodos de pagos y contratos. Investigar las razones de la alta tasa de cancelaciónes para clientes con contrato mensual y pago por cheque electrónico. Además, se puede incentivar el pago con los otros tipos de pagos a través de bonificaciones. Por ejemplo, un descuento para aquellos clientes que pagan con tarjeta de crédito.</li>
    </ul>
    '''
)
