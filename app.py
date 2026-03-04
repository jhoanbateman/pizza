import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="The Smiley Crew: Pizza Quest", page_icon="🍕", layout="wide")

# --- 🚀 MÉTRICAS CORE (ACTUALIZA LOS NÚMEROS AQUÍ) ---
CURRENT_MX_SMILEY = 88.9
CURRENT_IA_SMILEY = 88.9
TOTAL_SURVEYS = 19
MX_GOAL = 83.0
IA_GOAL = 85.0

# Datos de la tabla (Actualiza los nombres aquí)
leaderboard_data = [
    {"name": "Oriana Patricia Gonzalez Escobar", "count": 4, "rate": "100%"},
    {"name": "Mari Quevedo", "count": 3, "rate": "100%"},
    {"name": "Alejandro Caicedo", "count": 2, "rate": "66.67%"},
    {"name": "Julian Alfonso", "count": 2, "rate": "100%"},
    {"name": "Cristian Galvis", "count": 1, "rate": "100%"},
    {"name": "Jhoan Orozco", "count": 1, "rate": "100%"},
    {"name": "Juan Martínez", "count": 1, "rate": "100%"},
    {"name": "Sebastián Vélez", "count": 1, "rate": "100%"},
    {"name": "Veronica Castillo", "count": 1, "rate": "50%"},
]

# --- LÓGICA DE CÁLCULO ---
needed = max(0, int((IA_GOAL * (TOTAL_SURVEYS + 1) / 100) - (CURRENT_IA_SMILEY * TOTAL_SURVEYS / 100)))

# --- DISEÑO CSS (EL "LOOK" DE LA FOTO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&display=swap');
    
    .main {{
        background-color: #050505;
        font-family: 'Inter', sans-serif;
        color: white;
    }}
    
    /* Título Neón */
    .header-title {{
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(to right, #008060, #ffffff, #ff9100);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(0,128,96,0.5));
        margin-bottom: 0;
    }}
    
    /* Tarjetas Glassmorphism */
    .glass-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        margin-bottom: 1rem;
    }}
    
    /* El Cohete y la Barra Vertical */
    .rocket-track {{
        height: 300px;
        width: 80px;
        background: rgba(0,0,0,0.4);
        border-radius: 50px;
        position: relative;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 0 auto;
    }}
    
    .rocket-fill {{
        position: absolute;
        bottom: 0;
        width: 100%;
        border-radius: 50px;
        background: linear-gradient(to top, rgba(0,128,96,0.3), transparent);
    }}
    
    .rocket-icon {{
        position: absolute;
        left: 50%;
        transform: translateX(-50%) rotate(-45deg);
        font-size: 30px;
        filter: drop-shadow(0 0 10px white);
        transition: bottom 2s ease-in-out;
    }}
    
    /* Animación de la llama */
    .flame {{
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 10px;
        height: 20px;
        background: orange;
        border-radius: 50%;
        filter: blur(2px);
        animation: flicker 0.1s infinite;
    }}
    
    @keyframes flicker {{
        0% {{ height: 20px; opacity: 0.8; }}
        50% {{ height: 25px; opacity: 1; }}
        100% {{ height: 20px; opacity: 0.8; }}
    }}

    /* Tabla de posiciones */
    .leader-row {{
        display: flex;
        justify-content: space-between;
        padding: 10px;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        align-items: center;
    }}
    .gold {{ border: 1px solid gold; background: rgba(255,215,0,0.1); border-radius: 10px; }}
    </style>
    """, unsafe_allow_html=True)

# --- CUERPO DE LA APP ---
st.markdown('<h1 class="header-title">🚀 THE SMILEY CREW: PIZZA QUEST 🍕</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666; letter-spacing:2px;">SHOPIFY SUPPORT TEAM • DUAL MISSION TARGET</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div class="glass-card">
        <h3>📈 Mission Status</h3>
        <div style="display: flex; justify-content: space-around; align-items: flex-end; height: 350px;">
            <div style="text-align: center;">
                <div class="rocket-track">
                    <div class="rocket-fill" style="height: {CURRENT_MX_SMILEY}%;"></div>
                    <div class="rocket-icon" style="bottom: {CURRENT_MX_SMILEY}%;">🚀<div class="flame"></div></div>
                </div>
                <h2 style="color:#008060; margin-top:10px;">{CURRENT_MX_SMILEY}%</h2>
                <p style="font-size:10px; color:#666;">MX SMILEY</p>
            </div>
            <div style="text-align: center;">
                <div class="rocket-track">
                    <div class="rocket-fill" style="height: {CURRENT_IA_SMILEY}%; background: linear-gradient(to top, rgba(255,145,0,0.3), transparent);"></div>
                    <div class="rocket-icon" style="bottom: {CURRENT_IA_SMILEY}%;">🚀<div class="flame"></div></div>
                </div>
                <h2 style="color:#ff9100; margin-top:10px;">{CURRENT_IA_SMILEY}%</h2>
                <p style="font-size:10px; color:#666;">IA SMILEY</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="glass-card" style="text-align: center; height: 435px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 50px;">⭐</div>
        <h1 style="font-size: 80px; margin: 0;">{needed}</h1>
        <p style="color: #ff9100; font-weight: bold;">CONSECUTIVE SMILEYS NEEDED</p>
        <p style="color: #444; font-size: 12px;">To maintain the {IA_GOAL}% IA goal</p>
    </div>
    """, unsafe_allow_html=True)

# Mensaje de Estado
if CURRENT_IA_SMILEY >= IA_GOAL:
    st.markdown(f'<div class="glass-card" style="border-color: #008060; text-align: center;"><h2 style="color: #00ff9d;">🟢 DOUBLE GOAL SECURED! PIZZA FEAST TIME! 🍕</h2></div>', unsafe_allow_html=True)
    st.balloons()
else:
    st.markdown(f'<div class="glass-card" style="border-color: #ff9100; text-align: center;"><h2 style="color: #ff9100;">🟡 So close! The oven is warming up...</h2></div>', unsafe_allow_html=True)

# Leaderboard
st.markdown('<div class="glass-card"><h3>🏆 Top 10 Performers</h3>', unsafe_allow_html=True)
for i, entry in enumerate(leaderboard_data):
    medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else str(i+1)
    row_class = "leader-row gold" if i == 0 else "leader-row"
    st.markdown(f"""
    <div class="{row_class}">
        <span>{medal} <b>{entry['name']}</b></span>
        <span>{entry['count']} Smileys <small style="color:#666;">({entry['rate']})</small></span>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
