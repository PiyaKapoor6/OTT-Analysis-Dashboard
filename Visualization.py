import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🌞 Sunburst Visualization")

st.write(
    "This visualization represents the hierarchical relationship between OTT "
    "platforms, content types, and video quality. The size of each section "
    "depends on the monthly active users, while the color represents ratings."
)

st.divider()

df = pd.read_csv("Datasets/OTT_Platforms.csv")

selected_platforms = st.multiselect("📺 Select OTT Platform(s)",options=sorted(df["Platform"].unique()),placeholder="Choose one or more platforms")

if selected_platforms:
    filtered_df = df[df["Platform"].isin(selected_platforms)]
else:
    filtered_df = df

fig = px.sunburst(filtered_df,path=["Platform", "Content Type", "Video Quality"],values="Monthly Active Users (Millions)",color="Rating",color_continuous_scale="RdBu",title="OTT Platform Analysis")

fig.update_layout(
    height=750,
    margin=dict(t=60, l=20, r=20, b=20)
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>Monthly Users: %{value} Million<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

with st.expander("📌 Key Insights"):
    st.write("""
• The sunburst chart illustrates the hierarchical relationship between OTT platforms, content types, and video quality.

• Segment size represents monthly active users, while color indicates platform ratings.

• Users can interact with the chart to explore platform-specific distributions.
""")