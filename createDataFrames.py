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

print(df.head())

def createCount(df_col, x, y):
    count = Counter(df_col)
    count = pd.DataFrame({x:count.keys(), y:count.values()})
    print(count.head())
    count.to_csv(f"{x}_{y}.csv")

createCount(df['sex'], 'sex', 'number of patients')
