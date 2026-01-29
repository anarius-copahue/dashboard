import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Caviahue Dashboard Hub", layout="wide", page_icon="🏔️")

# --- 2. CSS ACTUALIZADO ---
st.markdown("""
    <style>
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    .centered-text {
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        color: #1a1c24;
    }
    
    /* Estilo base de la tarjeta */
    .card-container {
        background-color: #ffffff;
        border: 1px solid #eef0f2;
        border-radius: 16px;
        padding: 25px;
        height: 200px;
        transition: all 0.3s ease;
        margin-bottom: 10px;
        /* Línea sutil de color a la izquierda para dar identidad */
        border-left: 6px solid #ccc; 
    }
    
    .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
    }

    .tag-style {
        font-size: 10px;
        font-weight: bold;
        text-transform: uppercase;
        padding: 4px 8px;
        border-radius: 4px;
        margin-bottom: 10px;
        display: inline-block;
    }

    .stButton button {
        margin-top: -15px;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE LOGIN ---
def login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        _, col_central, _ = st.columns([1.2, 1, 1.2])
        with col_central:
        
            st.markdown("<h2 class='centered-text'>Completa tus credenciales para ingresar</h2>", unsafe_allow_html=True)
            
            user_input = st.text_input("Usuario")
            password_input = st.text_input("Contraseña", type="password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Ingresar", use_container_width=True):
                try:
                    user_upper = user_input.upper()
                    if user_upper in st.secrets and password_input == st.secrets[user_upper]:
                        st.session_state.autenticado = True
                        st.session_state.usuario_actual = user_upper
                        st.rerun()
                    else:
                        st.error("Acceso denegado. Verifica tus datos.")
                except Exception:
                    st.error("Error de configuración en Secrets.")
        return False
    return True

# --- 4. DASHBOARD (HUB) ---
def main():
    st.image("logo.png", width=200)
    
    st.markdown(f"""
        <div style="background-color: #1a1c24; padding: 15px; border-radius: 12px; margin-top: 20px; text-align: center;">
            <h2 style="color: white; margin: 0; font-size: 20px; letter-spacing: 2px;">CAVIAHUE BI HUB</h2>
            <p style="color: #888; margin: 0; font-size: 12px;">Bienvenido, {st.session_state.usuario_actual}</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Definición de tableros con paleta de montaña sobria
    # Colores: Verde Musgo, Azul Glaciar, Celeste Agua, Marrón Arena, Gris Piedra, Azul Profundo
    tableros = [
        {"tag": "Looker Studio", "t": "📊 Análisis de Mercado", "d": "Data de IQVIA: Mercados y territorios.", "url": "https://lookerstudio.google.com/reporting/2852e1de-96fd-4e63-b714-acae9e71cc60", "color": "#7FA998", "bg": "#F1F7F4"},
        {"tag": "Streamlit", "t": "📦Control de Avance", "d": "Ventas y stock en tiempo real.", "url": "https://caviahue-avance.streamlit.app/", "color": "#8BBACC", "bg": "#F2F8FA"},
        {"tag": "Looker Studio", "t": "🛒 Shopify Detail", "d": "Auditoría de órdenes y clientes.", "url": "https://lookerstudio.google.com/reporting/4e154199-d1be-4495-b405-a1a31366ac74", "color": "#A3C6D9", "bg": "#F4F9FC"},
        {"tag": "RRHH", "t": "👥 Naloo Gestión", "d": "Administración integral de Recursos Humanos y nómina.", "url": "https://app.naaloo.com/login", "color": "#B8A891", "bg": "#F9F7F4"},
        {"tag": "CRM", "t": "🌍 Elvis Representantes", "d": "Gestión de representantes y seguimiento de contactos.", "url": "https://sistemaelvis.net/...", "color": "#9EA8B0", "bg": "#F5F6F7"},
        {"tag": "Web", "t": "🗻 Caviahue Oficial", "d": "Acceso directo al sitio institucional y ecommerce.", "url": "https://www.cremascaviahue.com", "color": "#5D7A8C", "bg": "#EFF3F5"}
    ]

    # Renderizado dinámico
    for i in range(0, len(tableros), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(tableros):
                tab = tableros[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div class="card-container" style="border-left-color: {tab['color']};">
                            <span class="tag-style" style="color: {tab['color']}; background-color: {tab['bg']};">
                                {tab['tag']}
                            </span>
                            <h3 style="margin: 5px 0; color: #2C3E50; font-size: 18px;">{tab['t']}</h3>
                            <p style="color: #64748b; font-size: 13px;">{tab['d']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.link_button("Acceder", tab['url'], use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Cerrar Sesión", type="secondary"):
        st.session_state.autenticado = False
        st.rerun()

if login():
    main()