import streamlit as st
from utils import *
st.set_page_config(initial_sidebar_state="collapsed",layout='wide', page_title="Стартовая страница", page_icon="🌍")
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)

url = '/Ввести_вручную'
for i in range(0, 5):
    res = st.columns(1)

col4, col5, col6 = st.columns([1, 2, 1])

col5.markdown(f'''
<a href="{url}"><button style="background-color:#FF7314; color:White; font-size: 40px; border-radius: 10px; border: 3px solid #FF7314; padding: -15px 1112px; text-align: left; text-decoration: none; display: inline-block; margin: -30px -100px; cursor: pointer;">ПОЛУЧИТЬ ПРОГНОЗ</button></a>
''',
              unsafe_allow_html=True)
# invisible button
