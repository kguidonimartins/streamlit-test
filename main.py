import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Set page config
st.set_page_config(page_title="Interactive Map", layout="wide")

# Title
st.title("Interactive Occurrence Map")

# Load data
try:
    df = pd.read_csv("occ.csv")
except FileNotFoundError:
    st.error("Please ensure 'occ.csv' file exists in the same directory")
    st.stop()

# Create map centered on mean coordinates
m = folium.Map(
    location=[df['decimalLatitude'].mean(), df['decimalLongitude'].mean()],
    zoom_start=4
)

# Add points to map
for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['decimalLatitude'], row['decimalLongitude']],
        radius=5,
        color='red',
        fill=True,
        popup=row['scientificName'] if 'scientificName' in df.columns else None,
        tooltip=row['scientificName'] if 'scientificName' in df.columns else "Occurrence point"
    ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Display map
st.write("### Occurrence Points Map")
st_folium(m)

# Display data table
st.write("### Data Table")
st.dataframe(df)

## run with: streamlit run main.py