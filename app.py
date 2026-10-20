"""COSMOS — laboratorio espacial interactivo para Streamlit Community Cloud."""
from pathlib import Path
import base64
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="COSMOS · Explora lo extraordinario", page_icon="🪐", layout="wide", initial_sidebar_state="collapsed")
st.markdown('''<style>
.stApp { background:#050810; }
.block-container { padding:0 !important; max-width:100% !important; }
header[data-testid="stHeader"] { background:transparent; height:0; }
[data-testid="stToolbar"] { visibility:hidden; }
iframe { border:0; display:block; }
</style>''', unsafe_allow_html=True)

@st.cache_data
def experience():
    html = (ROOT / "assets" / "cosmos.html").read_text(encoding="utf-8")
    engine = (ROOT / "assets" / "three.min.js").read_text(encoding="utf-8")
    earth = base64.b64encode((ROOT / "assets" / "earth.jpg").read_bytes()).decode()
    return html.replace("/*__THREE__*/", engine).replace("__EARTH_TEXTURE__", "data:image/jpeg;base64," + earth)

st.iframe(experience(), height="content")
