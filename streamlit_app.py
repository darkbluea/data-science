import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter

from matplotlib.figure import Figure
import seaborn as sns


st.set_page_config(page_title="Heart Disease", page_icon="https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png", layout='centered', initial_sidebar_state="collapsed")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Analyzing physical condition related to heart diseases ❤️ </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    df_unclean = pd.read_csv("heart.csv")
    df_clean = pd.read_csv("clean_heart.csv")
    df_semi_clean = pd.read_csv("semi_cleaned_heart.csv")

    option = st.selectbox("Which data do you want to visualize ?", ("The distribution of men and women",
                                                                  "The distribution of the different types of chest pain",
                                                                  "The distribution of patients with and with fasting blood sugar",
                                                                  "the Distribution of patients resting electrocardiographic results",
                                                                  "The distribution of patients who feel chest pains after physical exercise",
                                                                  "The distribution of the patients number number of major blood vessels coloured by colonoscopy",
                                                                  "The distribution of the patients thal results",
                                                                  "The distribution of patients with and without a heart disease"))

    def pie(name_dataset, **kwargs):
        df = pd.read_csv(name_dataset)
        fig = px.pie(df, **kwargs)
        st.plotly_chart(fig)

    if option == "The distribution of men and women":
        pie("sex.csv", values='number of patients', names='sex', title='The distribution of men and women')
    if option == "The distribution of the different types of chest pain":
        pie("cp.csv", values='number of patients', names='chest pain type', title='The distribution of the different types of chest pain')
    if option == "The distribution of patients with and with fasting blood sugar":
        pie("fbs.csv", values='number of patients', names='fasting blood sugar over 120 mg/dl', title='The distribution of patients with and with fasting blood sugar')
    if option == "the Distribution of patients resting electrocardiographic results":
        pie("restecg.csv", values='number of patients', names='resting electrocardiographic results', title='the Distribution of patients resting electrocardiographic results')
    if option == "The distribution of patients who feel chest pains after physical exercise":
        pie("exang.csv", values='number of patients', names='exercise induced angina', title='The distribution of patients who feel chest pains after physical exercise')
    if option == "The distribution of the patients number number of major blood vessels coloured by colonoscopy":
        pie("ca.csv", values='number of patients', names='number of major blood vessels coloured by colonoscopy', title='The distribution of the patients number number of major blood vessels coloured by colonoscopy')
    if option == "The distribution of the patients thal results":
        pie("thal.csv", values='number of patients', names='thal', title='The distribution of the patients thal results')
    if option == "The distribution of patients with and without a heart disease":
        pie("target.csv", values='number of patients', names='target', title='The distribution of patients with and without a heart disease')


    opt2 = st.selectbox("Which data do you want to compare ?", ("Age of patients with and without heart disease",
                                                                "Number of slopes in peak exercise of patients with and with heart disease",
                                                                "Type of chest pains of patients with and without heart disease",
                                                                "Chest pains after exercise of patients with or without heart disease"))

    if opt2 == "Age of patients with and without heart disease":
        fig = Figure()
        ax = fig.subplots()
        sns.histplot(x='age', hue='target', data=df_semi_clean, element='step', ax=ax)
        ax.set_xlabel('age')
        ax.set_ylabel('count')
        st.pyplot(fig)
        st.write("""
        We can see that heart diseases are more common to people that are above the age of 50.
        """)

    if opt2 == "Number of slopes in peak exercise of patients with and with heart disease":
        fig = Figure()
        ax = fig.subplots()
        sns.countplot(x = 'target', data = df_semi_clean, hue = 'slope', ax=ax)
        ax.set_xlabel('target')
        ax.set_ylabel('count')
        st.pyplot(fig)
        st.write("""
        We can see that people who have less slopes in peak exercise are usually people with heart diseases. 
        """)

    if opt2 == "Type of chest pains of patients with and without heart disease":
        fig = Figure()
        ax = fig.subplots()
        sns.countplot(x = 'target', data = df_semi_clean, hue = 'cp', ax=ax)
        ax.set_xlabel('target')
        ax.set_ylabel('count')
        st.pyplot(fig)
        st.write("""
        We can see that people with heart diseases mostly have "typical angina" type of chest pain.
        """)

    if opt2 == "Chest pains after exercise of patients with or without heart disease":
        fig = Figure()
        ax = fig.subplots()
        sns.countplot(x = 'target', data = df_semi_clean, hue = 'exang', ax=ax)
        ax.set_xlabel('target')
        ax.set_ylabel('count')
        st.pyplot(fig)
        st.write("""
        We can see that people with heart diseases are more pron to chest pains after exercising
        """)

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
