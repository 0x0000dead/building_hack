import pandas as pd
import streamlit as st
import plotly.graph_objects as go
st.set_page_config(initial_sidebar_state="collapsed")

from PIL import Image

# Load the image from a file
image = Image.open('/app/building_hack/final/fi.png')

# Show the image in the Streamlit app
st.image(image, caption='Интерпретируемость')