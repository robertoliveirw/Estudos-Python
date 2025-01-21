import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('dataset/ClienteBanco.csv')

df