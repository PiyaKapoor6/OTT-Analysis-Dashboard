import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("💰 Subscription Price vs Monthly Active Users")

st.write(
    "This visualization compares the subscription price of OTT platforms "
    "with their monthly active users to identify whether higher-priced "
    "platforms attract more users."
)

st.divider()

df = pd.read_csv("Datasets/OTT_Platforms.csv")

fig = px.scatter(df,x="Subscription Price (INR/Month)",y="Monthly Active Users (Millions)",color="Platform",size="Rating",hover_name="Platform",title="Subscription Price vs Monthly Active Users")

fig.update_layout(
    height=600,
    xaxis_title="Subscription Price (₹/Month)",
    yaxis_title="Monthly Active Users (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

with st.expander("📌 Key Insights"):
    st.write("""
• The comparison highlights the relationship between subscription price and monthly active users.

• Higher subscription prices do not necessarily correspond to a larger user base.

• JioHotstar maintains the highest monthly active users according to the dataset.
""")