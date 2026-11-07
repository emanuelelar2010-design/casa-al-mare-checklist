import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Checklist Ibiza", 
    page_icon="📐", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Stile CSS per trasformare i pulsanti in card interattive che cambiano colore
st.markdown("""
    <style>
    /* Sfondo nero assoluto */
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

    /* Stile personalizzato per i pulsanti-card della checklist */
    .stButton button {
        width: 100%;
        background-color: #0D1117 !important;
        color: #E6EDF3 !important;
        border: 1px solid #30363D !important;
        border-radius: 12px !important;
        padding: 20px 15px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        font-family: 'Courier New', monospace !important;
        transition: all 0.2s ease !important;
        text-align: left !important;
    }
    .stButton button:hover {
        border-color: #58A6FF !important;
        background-color: #11161D !important;
    }

    /* Immagini piantine */
    img {
        border-radius: 10px;
        border: 1px solid #30363D;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Inizializzazione dello stato della memoria (memorizza i click)
if 'pt_states' not in st.session_state:
    st.session_state.pt_states = [False, False, False, False, False]
if 'pp_states' not in st.session_state:
    st.session_state.pp_states = [False, False, False, False, False]
if 'piano_corrente' not in st.session_state:
    st.session_state.piano_corrente = "Piano Terra"

# Titolo
st.title("CHECKLIST // IBIZA")
st.caption("Protocollo di sicurezza e chiusura")

st.markdown("---")

# Selettore piano a pulsanti orizzontali (pulito e immediato)
col_nav1, col_nav2 = st.columns(2)
with col_nav1:
    if st.button("📍 Piano Terra", type="secondary" if st.session_state.piano_corrente != "Piano Terra" else "primary"):
        st.session_state.piano_corrente = "Piano Terra"
        st.rerun()
with col_nav2:
    if st.button("📍 Primo Piano", type="secondary" if st.session_state.piano_corrente != "Primo Piano" else "primary"):
        st.session_state.piano_corrente = "Primo Piano"
        st.rerun()

st.markdown("")

# --- PIANO TERRA ---
if st.session_state.piano_corrente == "Piano Terra":
    st.subheader("PIANO TERRA")
    
    # Gestione piantina dinamica
    try:
        if all(st.session_state.pt_states):
            st.image("piano_terra_completo.png", caption="Blueprint - Piano Terra [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("piano_terra.png", caption="Blueprint - Piano Terra", use_container_width=True)
    except:
        st.warning("⚠️ Metti l'immagine 'piano_terra.png' nella cartella del progetto.")

    st.markdown("### Verifica Elementi:")
    
    voci_pt = [
        "🚰 Contatore Acqua",
        "💡 Linea Luci 1",
        "🔦 Linea Luci 2",
        "🏮 Linea Luci 3",
        "🪜 Vano Scale"
    ]

    col1, col2 = st.columns(2)
    for i, voce in enumerate(voci_pt):
        # Scegliamo la colonna
        current_col = col1 if i % 2 == 0 else col2
        
        # Testo e colore dinamico in base allo stato
        completato = st.session_state.pt_states[i]
        etichetta = f"✅ {voce} [COMPLETATO]" if completato else f"⬜ {voce}"
        
        with current_col:
            if st.button(etichetta, key=f"pt_btn_{i}"):
                st.session_state.pt_states[i] = not completato
                st.rerun()

    completati = sum(st.session_state.pt_states)
    st.progress(completati / 5)

    if completati == 5:
        st.success("Piano Terra completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati}/5 controlli completati")

# --- PRIMO PIANO ---
else:
    st.subheader("PRIMO PIANO")
    
    try:
        if all(st.session_state.pp_states):
            st.image("primo_piano_completo.png", caption="Blueprint - Primo Piano [IN SICUREZZA]", use_container_width=True)
        else:
            st.image("primo_piano.png", caption="Blueprint - Primo Piano", use_container_width=True)
    except:
        st.warning("⚠️ Metti l'immagine 'primo_piano.png' nella cartella del progetto.")

    st.markdown("### Verifica Elementi:")
    
    voci_pp = [
        "⚡ Contatore Elettrico",
        "🔥 Valvola Gas",
        "🔌 Prese TV / Frigo",
        "⛺ Tende Esterne",
        "🪟 Finestre"
    ]

    col1, col2 = st.columns(2)
    for i, voce in enumerate(voci_pp):
        current_col = col1 if i % 2 == 0 else col2
        
        completato = st.session_state.pp_states[i]
        etichetta = f"✅ {voce} [COMPLETATO]" if completato else f"⬜ {voce}"
        
        with current_col:
            if st.button(etichetta, key=f"pp_btn_{i}"):
                st.session_state.pp_states[i] = not completato
                st.rerun()

    completati_p1 = sum(st.session_state.pp_states)
    st.progress(completati_p1 / 5)

    if completati_p1 == 5:
        st.success("Primo Piano completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati_p1}/5 controlli completati")
        
