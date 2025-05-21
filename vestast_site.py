import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image
from io import BytesIO
import base64

# === Configurații generale ale paginii ===
st.set_page_config(layout="centered", page_title="Analiză VESTAS", page_icon="📈")

# === Afișare banner + siglă liceu ===
def get_sigla_base64(path):
    img = Image.open(path)
    img.thumbnail((100, 100))
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

sigla_path = "sigla_liceu.png"
sigla_base64 = get_sigla_base64(sigla_path)

banner_html = f"""
<div style='display: flex; align-items: center; justify-content: center; background-color: #dbeafe; padding: 10px; border-radius: 10px; margin-bottom: 20px;'>
    <img src="data:image/png;base64,{sigla_base64}" style='height: 60px; margin-right: 15px;' />
    <div style='font-weight: bold; font-size: 18px; color: #1e40af;'>📘 Proiect realizat de echipa <u>eEconomic</u></div>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

st.title("🌬️ Analiză Investiție: VESTAS WIND SYSTEMS A/S")
st.subheader("Cod bursier: `VWS.CO`")

# === Obține datele despre acțiune de la Yahoo Finance ===
actiune = yf.Ticker("VWS.CO")
info = actiune.info
pret = info.get("currentPrice", "N/A")
recomandare = info.get("recommendationKey", "N/A")

# === Afișare preț & recomandare ===
col1, col2 = st.columns(2)
col1.metric("💰 Preț curent (DKK)", pret)
col2.metric("📌 Recomandare investitori", str(recomandare).upper())

# === Imagine performanță acțiuni ===
imagine1 = "Imagine1.png"
if os.path.exists(imagine1):
    st.image(imagine1, caption="📊 Performanță acțiuni VESTAS", use_container_width=True)
else:
    st.warning(f"⚠️ Imagine lipsă: {imagine1}")

# === Argumente pentru investiție ===
with st.expander("🧩 Argumente strategice pentru investiție"):
    st.markdown("""
### ✅ Avantaje competitive VESTAS:
- ✔️ Lider global în energie eoliană  
- ✔️ Tehnologie verde – trend sustenabil și viitor sigur  
- ✔️ Cerere în creștere pentru surse regenerabile  
- ✔️ Parteneriate strategice cu guverne & corporații globale  
- 📈 Piața energiei verzi este estimată să crească cu 80% până în 2030  
- 🏭 Infrastructură globală și producție eficientă  
- ⚡ Inovație continuă în turbine eoliene inteligente  
- 🌍 Aliniere perfectă la politicile climatice europene  
""")

# === Informații suplimentare în extensii ===
with st.expander("📌 Despre Vestas"):
    st.markdown("""
**Vestas Wind Systems A/S** este liderul global în soluții de energie eoliană, cu sediul în Aarhus, Danemarca.  
- 📅 **Fondare:** 1945 (de Peder Hansen)  
- 👤 **CEO:** Henrik Andersen  
- 🧑‍💼 **Președinte:** Bert Nordberg  
- 👥 **Angajați:** aproximativ 35.100 (2024)  
- 🌍 **Țări cu turbine instalate:** 88  
- ⚡ **Capacitate totală instalată:** peste 189 GW  
- 🔗 [Website oficial](https://www.vestas.com)  
""")

with st.expander("🛠️ Produse și Servicii"):
    st.markdown("""
- 🌪️ **Turbine eoliene onshore și offshore** – eficiente și fiabile  
- 🧰 **Servicii de întreținere** – optimizarea performanței turbinelor  
- 📊 **Consultanță bazată pe date** – maximizarea producției de energie  
- 🤝 **Proiecte de dezvoltare** – parteneriate pentru parcuri eoliene mari  
""")

with st.expander("💼 Performanță Financiară"):
    st.markdown("""
- 💰 **Venituri (2024):** 17,3 miliarde EUR  
- 📈 **Profit operațional Q4 2024:** 759 milioane EUR  
- 📊 **Marjă EBIT estimată 2025:** 4–7%  
- 📦 **Backlog comenzi:** 69,8 miliarde EUR  
- 📉 **Simbol bursier:** `VWS` la Bursa din Copenhaga  
""")

with st.expander("🌱 Angajament pentru Sustenabilitate"):
    st.markdown("""
- ♻️ **Reciclare pale turbine:** parteneriat cu Stena Recycling  
- 🏗️ **Reducerea emisiilor:** utilizare oțel cu emisii reduse  
- 🏅 **Clasare globală:** locul 3 în topul Corporate Knights Global 100  
""")

with st.expander("🌍 Prezență Globală"):
    st.markdown("""
**Facilități în:**  
- 🇪🇺 Europa: Danemarca, Germania, Italia, România, Spania, Suedia, Norvegia, UK  
- 🌏 Asia: China, India, Taiwan  
- 🌎 America: SUA, Brazilia  
- 🇦🇺 Australia  

**Proiecte recente:**  
- 🌊 **Nordlicht 1 (Germania):** 68 turbine V236-15.0 MW  
- 🌪️ **Fengmiao I (Taiwan):** 495 MW  
- 🌬️ **Profen II (Germania):** 62 MW  
""")

with st.expander("🔎 Noutăți și Perspective"):
    st.markdown("""
Vestas rămâne un lider în ciuda provocărilor:  
- 📈 **Creștere costuri și întârzieri**  
- 🛠️ **Necesitate accelerare autorizări și investiții în rețele**  
- 🌐 **Sprijin esențial pentru obiectivele climatice globale**  
""")

with st.expander("📬 Contact"):
    st.markdown("""
- 📍 **Adresă:** Hedeager 42, 8200 Aarhus N, Danemarca  
- ☎️ **Telefon:** +45 97 30 00 00  
- 📧 **Email:** vestas-centraleurope@vestas.com  
- 🔗 [vestas.com](https://www.vestas.com)  
""")

# === Imagine suplimentară profil companie ===
imagine2 = "Imagine2.png"
if os.path.exists(imagine2):
    st.image(imagine2, caption="📌 Profil companie Vestas Wind Systems A/S", use_container_width=True)
else:
    st.warning(f"⚠️ Imagine lipsă: {imagine2}")

# === Date fundamentale companie ===
with st.expander("📊 Date fundamentale companie"):
    st.markdown("""
- 🏢 **Sediu:** Aarhus, Danemarca  
- 👥 **Angajați:** 35.100  
- 💸 **Venituri anuale:** kr.129 miliarde  
- 📈 **Crestere vânzări 2024:** 12.55%  
- 🏦 **Profit net:** kr.3.72 miliarde  
- 📅 **Sfârșit an fiscal:** Decembrie 2025  
- 🛠️ **Industrie:** Industrial Electronics  
- 📦 **Sector:** Industrial Goods  
""")

# === Evoluție acțiune (10 zile) ===
st.divider()
st.header("📈 Evoluție recentă a acțiunii VESTAS")

data = actiune.history(period="10d")

if not data.empty:
    zile = pd.to_datetime(data.index).strftime('%d %b')
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(zile, data["Close"], marker='o', linestyle='-', color='#007f5f', linewidth=2)
    ax.set_title("📉 Evoluția valorii acțiunii VESTAS (10 zile)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preț (DKK)")
    ax.grid(True, linestyle='--', alpha=0.5)

    for i, val in enumerate(data["Close"]):
        ax.annotate(f'{val:.1f}', (i, val), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

    st.pyplot(fig)
else:
    st.info("📭 Datele nu sunt disponibile momentan.")

# === Avertisment final ===
st.warning("⚠️ Investițiile pe piața bursieră implică riscuri. Informați-vă corect!")
