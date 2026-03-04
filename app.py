import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="The Smiley Crew: Pizza Quest", page_icon="🍕", layout="wide")

# --- 🚀 MÉTRICAS CORE (ACTUALIZA LOS NÚMEROS AQUÍ) ---
CURRENT_IA_SMILEY = 88.9
TOTAL_SURVEYS = 19
GOAL = 85.0
# ----------------------------------------------------

# Estilos CSS para el look "Premium Dark"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #008060; }
    .title { font-size: 50px; font-weight: bold; color: #008060; text-align: center; text-shadow: 0 0 20px #008060; }
    .pizza-card { background: rgba(255, 145, 0, 0.1); padding: 20px; border-radius: 15px; border: 2px dashed #ff9100; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title">🚀 THE SMILEY CREW: PIZZA QUEST 🍕</p>', unsafe_allow_html=True)

# Lógica de progreso
progress = CURRENT_IA_SMILEY / 100
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.write(f"### Progreso actual: {CURRENT_IA_SMILEY}%")
    st.progress(progress)
    
    if CURRENT_IA_SMILEY >= GOAL:
        st.success("🟢 PIZZA SECURED! Great job Crew! 🍕")
        st.balloons()
    elif CURRENT_IA_SMILEY >= 80:
        st.warning("🟡 So close! The oven is warming up... 🥵")
    else:
        st.error("🔴 We are far from the pizza! Let's push! 💪")

# Tabla de posiciones (Leaderboard)
st.write("---")
st.write("### 🏆 Top Performers")

# Datos de la tabla (Actualiza los nombres aquí)
data = {
    "Rank": ["1st", "2nd", "3rd", "4th", "5th"],
    "Name": ["Oriana Patricia", "Mari Quevedo", "Alejandro Caicedo", "Lina (TL)", "Team Member"],
    "Smileys": [4, 3, 2, 1, 0]
}
df = pd.DataFrame(data)

# Mostrar tabla con iconos
def highlight_medals(val):
    if val == "1st": return "🥇"
    if val == "2nd": return "🥈"
    if val == "3rd": return "🥉"
    return val

df["Rank"] = df["Rank"].apply(highlight_medals)
st.table(df)

# Cálculo de cuánto falta
needed = max(0, int((GOAL * (TOTAL_SURVEYS + 1) / 100) - (CURRENT_IA_SMILEY * TOTAL_SURVEYS / 100)))
st.sidebar.metric("Smileys needed for Goal", f"+{needed}")
st.sidebar.write("Keep up the great work, team! 💚")
