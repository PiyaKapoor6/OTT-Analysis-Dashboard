import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🗂️ OTT Platforms Dataset")

st.write("This section provides an overview of the OTT platforms dataset and allows "
        "users to explore individual platforms interactively.")

df=pd.read_csv("Datasets/OTT_Platforms.csv")
df1=pd.read_csv("Datasets/amazon_prime_titles.csv")
df2=pd.read_csv("Datasets/netflix_titles.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**📺 Platforms:**", df["Platform"].nunique())

st.divider()

st.subheader("📊 Overall Monthly Active Users Distribution")

fig = px.pie(df,names="Platform",values="Monthly Active Users (Millions)")

fig.update_layout(height=600,width=500)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🔍 Explore Individual Platforms")

select = st.multiselect("Choose OTT Platform(s)",options=sorted(df["Platform"].unique()),default=[])

if select:
    result = df[df["Platform"].isin(select)]

    fig2 = px.pie(result,names="Platform",values="Monthly Active Users (Millions)")

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(result, use_container_width=True)

else:
    st.info("👆 Select one or more OTT platforms from the list to view their details.")

st.divider()

with st.expander("📌 Key Insights"):
    st.write("""
• The dataset includes multiple OTT platforms with different subscription plans and user bases.

• Each platform is characterized by attributes such as monthly active users, rating, video quality, and content type.

• Users can filter the dataset to analyze specific OTT platforms individually.
""")