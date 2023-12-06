import streamlit as st
import pandas as pd
import numpy as np
st.title('For Jeff')
dfPath='Data.xlsx'
df=pd.read_excel(dfPath,sheet_name="Import")
def get_image_link(image_filename):
    image_path = "/Plots/"+image_filename
    return f'<a href="{image_path}" target="_blank">Show Plot</a>'

df['Plot Link'] = df['Plot Name'].apply(get_image_link)
st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)
