import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter

df = pd.read_csv("heart.csv")

df['sex'] = np.where(df['sex']==1, 'male', 'female')
df['cp'] = np.where(df['cp']==0, 'typical angina', np.where(df['cp']==1, 'atypical angina',
    np.where(df['cp']==2, 'non-anginal pain', np.where(df['cp']==3, 'asymptomatic', 0))))
df['fbs'] = np.where(df['fbs']==1, 'true', 'false')
df['restecg'] = np.where(df['restecg']==0, 'normal', 'abnormal')
df['exang'] = np.where(df['exang']==1, 'yes', 'no')
df['target'] = np.where(df['target']==1, 'not sick', 'sick')

print(df.head())

def createCount(name, df_col, x, y):
    count = Counter(df_col)
    count = pd.DataFrame({x:count.keys(), y:count.values()})
    print(count.head())
    count.to_csv(f"{name}.csv")

createCount('sex', df['sex'], 'sex', 'number of patients')
createCount('cp', df['cp'], 'chest pain type', 'number of patients')
createCount('fbs', df['fbs'], 'fasting blood sugar over 120 mg/dl', 'number of patients')
createCount('restecg', df['restecg'], 'resting electrocardiographic results', 'number of patients')
createCount('exang', df['exang'], 'exercise induced angina', 'number of patients')
createCount('ca', df['ca'], 'number of major blood vessels coloured by colonoscopy', 'number of patients')
createCount('thal', df['thal'], 'thal', 'number of patients')
createCount('target', df['target'], 'target', 'number of patients')

df.to_csv("semi_cleaned_heart.csv")
