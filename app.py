import os
from PIL import Image
import streamlit as st

# Configurazione della pagina (stile Midnight Minimal, full-screen)
st.set_page_config(
    page_title="Ibiza Villa Checklist", page_icon="🏡", layout="centered"
)

# CSS personalizzato per eliminare margini e dare un look immersivo scuro
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    /* Rimuove intestazioni e padding eccessivi per un'esperienza mobile nativa */
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

st.title("🏡 Piano Terra - Controllo Villa")
st.write("Seleziona gli elementi da verificare/spegnere:")

# --- 1. DEFINIZIONE DEGLI ELEMENTI (4 layer totali) ---
# L'ordine corrisponde esattamente ai layer: da 0 a 3
checklist_items = [
    {"label": "Contatore Acqua", "file": "pt_layer_0.png"},
    {
        "label": "Linea Luci 1 & 2 (Unificate)",
        "file": "pt_layer_1.png",
    },  # Accorpate
    {"label": "Linea Luci 3", "file": "pt_layer_2.png"},
    {"label": "Vano Scale", "file": "pt_layer_3.png"},
]

# --- 2. INTERFACCIA UTENTE (Checkbox dinamiche) ---
selected_states = []

for i, item in enumerate(checklist_items):
    # Ogni checkbox restituisce True se spuntata
    is_checked = st.checkbox(item["label"], key=f"pt_item_{i}")
    selected_states.append(is_checked)

# --- 3. LOGICA DI COMPOSIZIONE PIL (Layer-Overlay) ---
base_image_path = "piano_terra.png"

try:
    # Carica la piantina di base
    base_img = Image.open(base_image_path).convert("RGBA")

    # Partiamo dalla copia della base
    combined_img = base_img.copy()

    # Sovrapponi in tempo reale solo i layer corrispondenti alle checkbox spuntate
    for i, is_checked in enumerate(selected_states):
        if is_checked:
            layer_file = checklist_items[i]["file"]
            if os.path.exists(layer_file):
                overlay_img = Image.open(layer_file).convert("RGBA")
                # Incolla il layer trasparente sopra la base usando se stesso come maschera
                combined_img.alpha_composite(overlay_img)
            else:
                st.warning(
                    f"⚠️ Attenzione: Impossibile trovare il file {layer_file}"
                )

    # Mostra l'immagine finale risultante aggiornata in tempo reale
    st.markdown("---")
    st.subheader("📊 Stato Piantina in Tempo Reale")
    st.image(combined_img, use_container_width=True)

except FileNotFoundError:
    st.error(
        f"❌ Errore critico: Assicurati che l'immagine di base '{base_image_path}' e i layer siano nella stessa cartella dello script."
    )
