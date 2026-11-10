import streamlit as st

st.info("🤔​:green[**Conclusiones**]")

with st.container(border=True, width='content', vertical_alignment='center', gap='small'):
    
    st.success("✅ El género no es un factor que influye en la fuga de clientes")

    st.warning(
        """
        ❌ Los clientes mayores a 65 años tienen una alta tasa de renuncia(42%) en comparación con los clientes menores de 65 años(24%).
    """
    )
    st.warning(
        """
        ❌ El tipo de contrato mensual, el método de pago cheque electrónico y el servicio de fibra óptica tienen tasas de cancelación mayor que el promedio.
        """
    )
    st.warning(
        """
        ❓​ Los clientes que renunciaron a los servicios de la empresa pagaron mensualmente más que los clientes que no se fueron.Sin embargo, estos primeros pagaron menos de cargos total que los últimos. Esto se relaciona con el tiempo de permanencia de los clientes, y es que los clientes que se dieron de baja permanecieron menos tiempo que los que no se fueron. En promedio, se quedaron 18 meses.
        """
    )
    st.warning(
        """
        ❓​ Los clientes con fibra óptica contrataron desde 1 hasta 8 servicios.
        """
    )
    st.warning(
        """
        ❓​Los clientes con el servicio de internet dsl contrataron desde el servicio básico hasta 8 servicios.
        """
    )
    st.warning(
        """
        ❓​ Los clientes que no tenían internet, tenían exclusivamente el servicio telefónico.
        """
    )    
    st.warning(
        """
        ❌ Los clientes churners con pocos servicios tienden a permanecer menos tiempo en la empresa.
        """
    )    


st.info("📖​✍️​:green[**Implicaciones y recomendaciones**]")

st.html(
    '''
    <style>
        .recomendaciones { 
                    font-size: 16px;
                    font-family: sans-serif;
                    font-weight: bold;
        }

        .subtitulos {
            color: green;
            font-family: sans-serif;
            font-weight: bold;
        }

        .contenedor-responsive {
            width: 100%; /* Ocupa el ancho disponible */
            max-width: 800px; /* Límite máximo opcional */
            border-radius: 20px; /* Radio fijo para contenedores anchos */
            overflow: hidden; /* Recorta el contenido interno */
            box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Opcional: añade profundidad */
        }   

    </style>

    <div class="contenedor-responsive">
        
        <p class="recomendaciones">
            A partir de los resultados se puede identificar que el problema de la evasión de clientes es un problema multicausal cuyas causas están relacionadas con la satisfacción de cada cliente con el servicio o los servicios contratados.
            <br/>
            En los resultados mencionamos cuales son los factores que se relacionan con la diserción de clientes y en este apartado abordamos que implica cada factor.
            <br/>
            El análisis de datos muestra que existen al menos dos perfiles evasores en relación a los tipos de servicios contratados, la permanencia de los clientes, el pago mensual, el total facturado y el número de servicios contratados. Estos tipos de clientes son:
        </p>
        <ol class="recomendaciones">
            <li>Los usuarios que contrataron fibra óptica y que tienen un paquete de servicios extras.</li>
            <li>Los usuarios que contrataron pocos servicios y de baja permanencia.</li>
        </ol>

        <h2 class="subtitulos"><i>Usuarios con fibra óptica y número de servicios</i></h2>
        <p class="recomendaciones">
            Los primeros adquirieron principalmente entre 2 a 5 servicios extras. Esto indica que son personas con capacidad de pago, dado que los churners son las personas que más pagaron mensualmente. No obstante, se dan de baja porque no se encuentran satisfechos con los servicios contratados, principalmente con la fibra óptica.
        </p>

        <h2 class="subtitulos"><i>Usuarios con pocos servicios y baja permanencia</i></h2>
        <p class="recomendaciones">         
            En los segundos usuarios, destacan aquellos con 0 servicios adicionales contratados, con una tasa de cancelación del 44%. En esta franja de clientes, se encuentran las personas que únicamente tenían internet dsl. Además, tenemos que resaltar los usuarios que cancelaron y que tenían un solo servicio. Aunque la tasa de cencelación no es la más alta, el 91% de estos tenían solo línea de teléfono. Las personas que contrataron dls y servicio de teléfono fueron los que menos tiempo perdudaron. Esto sugiere que la falta de un mayor número de servicios adicionales o una percepción de valor insuficiente en los servicios básicos los hace más vulnerables a la fuga."
            <br/>
            Otro perfil de churn son las personas mayores de 65 años. Estas tienen una tasa de churn que es aproximadamente el doble de la tasa de los menores de 65 años."

            Por último, esta el perfil de churn que se relaciona con las características contractuales. Dentro de este perfil se encuentran aquellos que tenían el tipo de contrato mensual y que pagaban a través de pago electrónico."
            
        </p>
        <h2 class="subtitulos"><i>Recomendaciones</i></h2>
        <p class="recomendaciones">
            Por lo tanto, hacemos las siguientes recomendaciones para abordar las cancelaciones en función de cada tipo de perfil identificado:
        </p>
        <ul class="recomendaciones">
            <li>Mejorar la calidad del servicio fibra óptica, realizando una investigación sobre la experiencia del cliente con este servicio. Esto puede lograrse a través de encuestas, monitoreo de la velocidad y la eficiencia del soporte técnico.</li>
            <li>Ofrecer promociones atractivas para clientes con muy pocos servicios. Esto puede conseguirse a través de paquetes de servicios, por ejemplo internet + teléfono o internet + servicio de streaming. Al adquirir estos paquetes, también se les puede otorgar bonificaciones a los clientes para que tengan un tiempo de prueba.</li>
            <li>Atención específica al segmento etario mayor de 65 años. Elaborar estrategias comerciales y de servicio técnico exclusivamente para esta porción de demográfica.</li>
            <li>Optimización de métodos de pagos y contratos. Investigar las razones de la alta tasa de cancelaciónes para clientes con contrato mensual y pago por cheque electrónico. Además, se puede incentivar el pago con los otros tipos de pagos a través de bonificaciones. Por ejemplo, un descuento para aquellos clientes que pagan con tarjeta de crédito.</li>
        </ul>

    </div>
    '''
)