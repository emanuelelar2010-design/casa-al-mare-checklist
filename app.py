import base64
import os
from PIL import Image
import streamlit as st


# --- FUNZIONE TRUCCO PER L'ICONA SU SMARTPHONE ---
def inject_pwa_meta():
    try:
        with open("icona.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()

        pwa_meta_html = f"""
            <link rel="apple-touch-icon" sizes="180x180" href="data:image/png;base64,{encoded_string}">
            <link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{encoded_string}">
            <link rel="icon" type="image/png" sizes="16x16" href="data:image/png;base64,{encoded_string}">
            <meta name="apple-mobile-web-app-title" content="Ibiza">
            <meta name="apple-mobile-web-app-capable" content="yes">
            <meta name="apple-mobile-web-app-status-bar-style" content="black">
        """
        st.markdown(pwa_meta_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass


# --- INIZIO APP ---

st.set_page_config(
    page_title="Checklist Ibiza",
    page_icon="icona.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_pwa_meta()

# Stile CSS Midnight Minimal
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 600px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🏡 Gestione Villa - Ibiza")

# Selettore del Piano
piano = st.radio(
    "Seleziona il Piano:",
    ["Piano Terra", "Primo Piano"],
    horizontal=True,
    key="piano_selector",
)

st.markdown("---")

# ==========================================
# PIANO TERRA
# ==========================================
if piano == "Piano Terra":
    # 4 Voci (Luci 1 e 2 unificate)
    pt_items = [
        {"label": "Contatore Acqua", "file": "pt_layer_0.png"},
        {"label": "Linea Luci 1 & 2 (Unificate)", "file": "pt_layer_1.png"},
        {"label": "Linea Luci 3", "file": "pt_layer_2.png"},
        {"label": "Vano Scale", "file": "pt_layer_3.png"},
    ]

    # Inizializzazione session_state se non presente
    if "pt_states" not in st.session_state:
        st.session_state.pt_states = [False] * len(pt_items)

    # --- COMPOSIZIONE DINAMICA DELL'IMMAGINE ---
    base_path = "piano_terra.png"

    if os.path.exists(base_path):
        base_img = Image.open(base_path).convert("RGBA")

        # Canvas trasparente su cui incollare i layer attivi
        canvas = Image.new("RGBA", base_img.size, (0, 0, 0, 0))

        # Sovrapponiamo solo i layer spuntati
        for i, item in enumerate(pt_items):
            if st.session_state.pt_states[i]:
                layer_path = item["file"]
                if os.path.exists(layer_path):
                    layer_img = Image.open(layer_path).convert("RGBA")
                    canvas.alpha_composite(layer_img)

        # Mettiamo la piantina base sopra i cerchietti
        final_img = Image.alpha_composite(canvas, base_img)

        completati = sum(st.session_state.pt_states)
        caption_text = (
            "Blueprint - Piano Terra [IN SICUREZZA]"
            if completati == len(pt_items)
            else "Blueprint - Piano Terra"
        )

        st.image(final_img, caption=caption_text, use_container_width=True)
    else:
        st.warning("⚠️ Metti l'immagine 'piano_terra.png' nel repository.")

    st.markdown("### Verifica Elementi:")

    # Render Checkbox
    for i, item in enumerate(pt_items):
        st.session_state.pt_states[i] = st.checkbox(
            item["label"],
            value=st.session_state.pt_states[i],
            key=f"pt_check_{i}",
        )

    completati = sum(st.session_state.pt_states)
    if completati == len(pt_items):
        st.success("Piano Terra completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati}/{len(pt_items)} controlli completati")

# ==========================================
# PRIMO PIANO
# ==========================================
else:
    pp_items = [
        "Linea Luci Camere",
        "Climatizzatori",
        "Terrazza",
        "Scaldabagno",
        "Finestre/Imposte",
    ]

    if "pp_states" not in st.session_state:
        st.session_state.pp_states = [False] * len(pp_items)

    completati_p1 = sum(st.session_state.pp_states)

    try:
        caption_text_p1 = (
            "Blueprint - Primo Piano [IN SICUREZZA]"
            if completati_p1 == len(pp_items)
            else "Blueprint - Primo Piano"
        )
        st.image(
            "primo_piano.png", caption=caption_text_p1, use_container_width=True
        )
    except Exception:
        st.warning("⚠️ Metti l'immagine 'primo_piano.png' nel repository.")

    st.markdown("### Verifica Elementi:")

    for i, label in enumerate(pp_items):
        st.session_state.pp_states[i] = st.checkbox(
            label, value=st.session_state.pp_states[i], key=f"pp_check_{i}"
        )

    completati_p1 = sum(st.session_state.pp_states)
    if completati_p1 == len(pp_items):
        st.success("Primo Piano completato e in sicurezza.")
    else:
        st.info(f"Stato: {completati_p1}/{len(pp_items)} controlli completati")
