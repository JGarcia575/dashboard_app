import streamlit as st

def render_footer():
    """Renderiza un footer uniforme al final de todas las páginas."""
    st.markdown("---")  # Línea separadora visual
    
    footer_html = """
    <style>
        .footer-container {
            width: 100%;
            padding: 20px 0 10px 0;
            margin-top: 20px;
            text-align: center;
            font-size: 0.85rem;
            color: #6c757d;
        }
        .footer-links a {
            color: #4B6BFB;
            text-decoration: none;
            margin: 0 10px;
            font-weight: 500;
        }
        .footer-links a:hover {
            text-decoration: underline;
        }
    </style>
    
    <div class="footer-container">
        <p style="margin-bottom: 8px;">
            <b>Telecom Churn Analytics & Prediction System</b> | Desarrollado con Streamlit & Python
        </p>
        <div class="footer-links">
            <a href="https://github.com/tu-usuario/tu-repositorio" target="_blank">Repository</a> •
            <a href="https://linkedin.com/in/tu-perfil" target="_blank">LinkedIn</a> •
            <a href="mailto:tu-email@ejemplo.com">Contacto</a>
        </div>
        <p style="font-size: 0.75rem; color: #9aa0a6; margin-top: 8px;">
            © 2026 Todos los derechos reservados.
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)