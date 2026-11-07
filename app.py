import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Checklist Ibiza", 
    page_icon="📐", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Stile CSS Minimal & Blueprint: Sfondo nero universale e checkbox extra-large
st.markdown("""
    <style>
    /* Sfondo nero assoluto su qualsiasi dispositivo/browser */
    .stApp, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #07090E !important;
        color: #C9D1D9 !important;
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

    /* Menù a tendina pulito in alto a sinistra (etichetta nascosta per massima pulizia) */
    div[data-testid="stSelectbox"] label {
        display: none !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #0D1117;
        border-radius: 10px;
        border: 1px solid #30363D;
        color: #E6EDF3;
        font-size: 16px;
    }

    /* Checkbox extra-large, super comode e spaziose per il touch da mobile */
    .stCheckbox {
        background-color: #0D1117;
        padding: 20px 18px;
        border-radius: 12px;
        border: 1px solid #21262D;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }
    .stCheckbox:hover {
        border-color: #58A6FF;
        background-color: #11161D;
    }
    .stCheckbox label {
        font-size: 17px !important;
        color: #E6EDF3 !important;
        font-weight: 600 !important;
        font-family: 'Courier New', monospace;
    }

    /* Immagini piantine in alto */
    img {
        border-radius: 10px;
        border: 1px solid #30363D;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Intestazione richiesta
st.title("CHECKLIST // IBIZA")
st.caption("Protocollo di sicurezza e chiusura")

st.markdown("---")

# Menù a tendina pulito (senza etichette fastidiose)
piano = st.selectbox(
    "piano", 
    ["Piano Terra", "Primo Piano"],
    label_visibility="collapsed"
)

st.markdown("")

if piano == "Piano Terra":
    st.subheader("PIANO TERRA")
    
    # Piantina in alto
    try:
        if 'c1' in locals() and c1 and 'c2' in locals() and c2 and 'c3' in locals() and c3 and 'c4' in locals() and c4 and 'c5' in locals() and c5:
            st.image("piano_terra_completo.png", caption="Blueprint - Piano Terra [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("piano_terra.png", caption="Blueprint - Piano Terra", use_container_width=True)
    except:
        try:
            st.image("piano_terra.png", caption="Blueprint - Piano Terra", use_container_width=True)
        except:
            st.warning("⚠️ Metti l'immagine 'piano_terra.png' nella cartella del progetto.")

    st.markdown("### Verifica Elementi:")
    
    # Checkbox grandi a due colonne
    col1, col2 = st.columns(2)
    with col1:
        c1 = st.checkbox("🚰 Contatore Acqua")
        c2 = st.checkbox("💡 Linea Luci 1")
        c3 = st.checkbox("🔦 Linea Luci 2")
    with col2:
        c4 = st.checkbox("🏮 Linea Luci 3")
        c5 = st.checkbox("🪜 Vano Scale")

    completati = sum([c1, c2, c3, c4, c5])
    st.progress(completati / 5)

    if completati == 5:
        st.success("Piano Terra completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati}/5 controlli completati")

else:
    st.subheader("PRIMO PIANO")
    
    # Piantina in alto
    try:
        if 'p1' in locals() and p1 and 'p2' in locals() and p2 and 'p3' in locals() and p3 and 'p4' in locals() and p4 and 'p5' in locals() and p5:
            st.image("primo_piano_completo.png", caption="Blueprint - Primo Piano [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("primo_piano.png", caption="Blueprint - Primo Piano", use_container_width=True)
    except:
        try:
            st.image("primo_piano.png", caption="Blueprint - Primo Piano", use_container_width=True)
        except:
            st.warning("⚠️ Metti l'immagine 'primo_piano.png' nella cartella del progetto.")

    st.markdown("### Verifica Elementi:")
    
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.checkbox("⚡ Contatore Elettrico")
        p2 = st.checkbox("🔥 Valvola Gas")
        p3 = st.checkbox("🔌 Prese TV / Frigo")
    with col2:
        p4 = st.checkbox("⛺ Tende Esterne")
        p5 = st.checkbox("🪟 Finestre")

    completati_p1 = sum([p1, p2, p3, p4, p5])
    st.progress(completati_p1 / 5)

    if completati_p1 == 5:
        st.success("Primo Piano completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati_p1}/5 controlli completati")
        
