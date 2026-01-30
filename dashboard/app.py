import streamlit as st

st.title("AI Powered LULC Change Detection – Tirupati")

st.header("Land Use Maps")
st.image("outputs/lulc_year1.png", caption="Year 1 LULC Map")
st.image("outputs/lulc_year2.png", caption="Year 2 LULC Map")

st.header("Change Detection")
st.image("outputs/change_map.png", caption="Pixel-Level Change Map")

st.write("This system detects land cover transitions using satellite imagery and AI.")
