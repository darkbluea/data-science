import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter


st.beta_set_page_config(page_title="Heart Disease", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Crop Recommendation  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_unclean = pd.read_csv("heart.csv")
    df_clean = pd.read_csv("clean_heart.csv")
    
    def pie(name_dataset, **kwargs):
        df = pd.read_csv(name_dataset)
        fig = px.pie(df, **kwargs)
        st.plotly_chart(fig)

    pie("sex_number of patients.csv")
#    pie(df_unclean['sex'], 'sex', 'number of patients')
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
