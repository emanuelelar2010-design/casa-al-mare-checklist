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

# --- 1. SELETTORE DEL PIANO ---
piano_selezionato = st.selectbox(
    "Seleziona il Piano", ["Piano Terra", "Primo Piano (Prossimamente)"]
)

st.markdown("---")

# --- 2. CONFIGURAZIONE ELEMENTI E LAYER PER IL PIANO TERRA ---
if piano_selezionato == "Piano Terra":
    st.subheader("📍 Piano Terra - Check interruttori e utenze")

    # I 4 layer creati per il piano terra (con Luci 1 & 2 unificate)
    checklist_items = [
        {"label": "Contatore Acqua", "file": "pt_layer_0.png"},
        {"label": "Linea Luci 1 & 2", "file": "pt_layer_1.png"},
        {"label": "Linea Luci 3", "file": "pt_layer_2.png"},
        {"label": "Vano Scale", "file": "pt_layer_3.png"},
    ]

    base_image_path = "piano_terra.png"
else:
    # Spazio riservato per quando aggiungerai il primo piano
    st.info(
        "🚧 Il Primo Piano sarà configurato non appena preparerai le relative immagini!"
    )
    st.stop()

# --- 3. INTERFACCIA UTENTE (Checkbox) ---
selected_states = []
for i, item in enumerate(checklist_items):
    is_checked = st.checkbox(item["label"], key=f"pt_item_{i}")
    selected_states.append(is_checked)

# --- 4. LOGICA DI COMPOSIZIONE PIL (Con la piantina SOPRA) ---
try:
    # Carica la piantina di base
    base_img = Image.open(base_image_path).convert("RGBA")

    # Creiamo un'immagine trasparente delle stesse dimensioni della piantina
    # dove andremo prima a incollare i cerchietti attivi
    canvas = Image.new("RGBA", base_img.size, (0, 0, 0, 0))

    # Incolla sul canvas trasparente solo i layer delle voci spuntate
    for i, is_checked in enumerate(selected_states):
        if is_checked:
            layer_file = checklist_items[i]["file"]
            if os.path.exists(layer_file):
                overlay_img = Image.open(layer_file).convert("RGBA")
                canvas.alpha_composite(overlay_img)

    # ORA UNIAMO LA PIANTINA SOPRA:
    # Mettiamo la piantina di base (base_img) SOPRA al canvas dei cerchietti
    final_img = Image.alpha_composite(canvas, base_img)

    # Mostra l'immagine finale risultante
    st.markdown("---")
    st.subheader("📊 Visualizzazione Piantina")
    st.image(final_img, use_container_width=True)

except FileNotFoundError:
    st.error(
        f"❌ Errore: Assicurati che l'immagine di base '{base_image_path}' e i file dei layer siano nella cartella del progetto."
    )
