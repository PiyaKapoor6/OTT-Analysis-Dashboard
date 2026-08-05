import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.info(
    "India's Over-The-Top (OTT) streaming market includes global giants, "
    "popular Indian platforms, and regional entertainment services offering "
    "movies, TV shows, live sports, and original content."
)
st.image("images.jpg",use_container_width=True)

df1=pd.read_csv("Datasets/OTT_Platforms.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("📺 **Platforms**")
    st.write(df1["Platform"].nunique())

with col2:
    st.write("👥 **Monthly Users**")
    st.write(df1["Monthly Active Users (Millions)"].sum())

with col3:
    st.write("⭐ **Average Rating**")
    st.write(round(df1["Rating"].mean(), 2))

st.divider()

st.subheader("📊 Monthly Active Users by OTT Platform")

fig=px.bar(df1,x=df1['Platform'],y=df1['Monthly Active Users (Millions)'], title='Monthly Users of Each Platform',color_continuous_scale=px.colors.sequential.Plasma)
fig.update_layout(
    width=2000,
    height=600
)
st.plotly_chart(fig,use_container_width=True)

st.divider()

with st.expander("📌 Key Insights"):
    st.write("""
• JioHotstar has the highest monthly active users among all OTT platforms according to the dataset.

• User distribution varies significantly across platforms, with a few major services dominating the market.

• The dashboard enables comparison of OTT platforms based on popularity, subscription prices, ratings, and content offerings.
""")