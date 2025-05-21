import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

# 🔄 Refresh automat la 5 secunde
time.sleep(5)
st.rerun()

# Configurații generale ale paginii
st.set_page_config(layout="centered", page_title="Analiză VESTAS", page_icon="📈")

st.title("🌬️ Analiză Investiție: VESTAS WIND SYSTEMS A/S")
st.subheader("Cod bursier: `VWS.CO`")

# Obține datele despre acțiune de la Yahoo Finance
actiune = yf.Ticker("VWS.CO")
info = actiune.info
pret = info.get("currentPrice", "N/A")
recomandare = info.get("recommendationKey", "N/A")

# Afișare preț & recomandare
col1, col2 = st.columns(2)
col1.metric("💰 Preț curent (DKK)", pret)
col2.metric("📌 Recomandare investitori", str(recomandare).upper())

# Afișare imagine performanță acțiuni
imagine1 = "images/Captura1.png"
if os.path.exists(imagine1):
    st.image(imagine1, caption="📊 Performanță acțiuni VESTAS", use_container_width=True)
else:
    st.warning(f"⚠️ Imagine lipsă: {imagine1}")

# Argumente pentru investiție
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

# Afișare imagine profil companie
imagine2 = "images/Captura2.png"
if os.path.exists(imagine2):
    st.image(imagine2, caption="📌 Profil companie Vestas Wind Systems A/S", use_container_width=True)
else:
    st.warning(f"⚠️ Imagine lipsă: {imagine2}")

# Date fundamentale
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

# Grafic evoluție recentă
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

# Avertisment
st.warning("⚠️ Investițiile pe piața bursieră implică riscuri. Informați-vă corect!")