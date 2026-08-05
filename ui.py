import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="OTT Analysis Dashboard",page_icon="📺",layout="wide")

st.title("📺 OTT Platforms Analysis Dashboard")
st.caption("📊 Interactive Data Analysis & Visualization using Python")

st.divider()

st.sidebar.title("🧭 Navigation")

pages=[
    st.Page('Home.py',title="🏠 Home"),
    st.Page('Dataset.py',title="🗂️ Dataset"),
    st.Page('Visualization.py',title="📊Visualization"),
    st.Page('Comparison.py',title="⚖️ Comparison"),
]
pg=st.navigation(pages,position="sidebar")
pg.run()