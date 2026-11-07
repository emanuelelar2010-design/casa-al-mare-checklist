import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Checklist Casa al Mare", 
    page_icon="📐", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Stile CSS Minimal & Blueprint con layout a griglia/card
st.markdown("""
    <style>
    .main { 
        background-color: #07090E; 
        color: #C9D1D9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    h1 { 
        color: #F0F6FC !important; 
        font-family: 'Courier New', monospace; 
        font-weight: 700;
        letter-spacing: -1px;
    }
    h2, h3 { 
        color: #8B949E !important; 
        font-family: 'Courier New', monospace; 
        font-size: 1.1rem !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        background-color: #0D1117;
        border-radius: 8px;
        border: 1px solid #30363D;
        color: #E6EDF3;
    }

    /* Stile card interattive ordinate */
    .stCheckbox {
        background-color: #0D1117;
        padding: 10px 14px;
        border-radius: 8px;
        border: 1px solid #21262D;
        margin-bottom: 6px;
        transition: all 0.2s ease;
    }
    .stCheckbox:hover {
        border-color: #58A6FF;
        background-color: #11161D;
    }
    .stCheckbox label {
        font-size: 14px !important;
        color: #E6EDF3 !important;
        font-weight: 400;
        font-family: 'Courier New', monospace;
    }

    img {
        border-radius: 8px;
        border: 1px solid #30363D;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("CHECKLIST // CASA AL MARE")
st.caption("Protocollo di sicurezza e chiusura")

st.markdown("---")

piano = st.selectbox(
    "Seleziona il livello:", 
    ["Piano Terra", "Primo Piano"]
)

st.markdown("")

if piano == "Piano Terra":
    st.subheader("PIANO TERRA")
    
    # Sezione Controlli in griglia a 2 colonne
    col1, col2 = st.columns(2)
    with col1:
        c1 = st.checkbox("🚰 Contatore Acqua")
        c2 = st.checkbox("💡 Linea Luci 1")
        c3 = st.checkbox("🔦 Linea Luci 2")
    with col2:
        c4 = st.checkbox("🏮 Linea Luci 3")
        c5 = st.checkbox("🪜 Vano Scale")

    completati = sum([c1, c2, c3, c4, c5])
    
    # DINAMICA PIANTINA: Se completato al 100%, mostra la versione evidenziata/colorata
    try:
        if completati == 5:
            st.image("piano_terra_completo.png", caption="Blueprint - Piano Terra [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("piano_terra.png", caption="Blueprint - Piano Terra", use_container_width=True)
    except:
        # Fallback se non carichi la versione _completo.png
        try:
            st.image("piano_terra.png", caption="Blueprint - Piano Terra", use_container_width=True)
        except:
            st.warning("⚠️ Metti l'immagine 'piano_terra.png' nella cartella del progetto.")

    st.progress(completati / 5)

    if completati == 5:
        st.success("Piano Terra completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati}/5 controlli completati")

else:
    st.subheader("PRIMO PIANO")
    
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.checkbox("⚡ Contatore Elettrico")
        p2 = st.checkbox("🔥 Valvola Gas")
        p3 = st.checkbox("🔌 Prese TV / Frigo")
    with col2:
        p4 = st.checkbox("⛺ Tende Esterne")
        p5 = st.checkbox("🪟 Finestre")

    completati_p1 = sum([p1, p2, p3, p4, p5])
    
    # DINAMICA PIANTINA PRIMO PIANO
    try:
        if completati_p1 == 5:
            st.image("primo_piano_completo.png", caption="Blueprint - Primo Piano [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("primo_piano.png", caption="Blueprint - Primo Piano", use_container_width=True)
    except:
        try:
            st.image("primo_piano.png", caption="Blueprint - Primo Piano", use_container_width=True)
        except:
            st.warning("⚠️ Metti l'immagine 'primo_piano.png' nella cartella del progetto.")

    st.progress(completati_p1 / 5)

    if completati_p1 == 5:
        st.success("Primo Piano completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati_p1}/5 controlli completati")
        st.info(f"Stato: {completati_p1}/5 controlli completati")
