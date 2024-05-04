import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style="ticks", context="talk")
plt.style.use("dark_background")

st.title("Let's see the data")

df = pd.read_csv('data/raw/Churn_Modelling.csv')
df = df.drop(columns=['RowNumber', 'CustomerId'])
dic = pd.read_csv('data/external/dictionary.csv')
qualitative_variables = dic.query("tipo == 'qualitativa'").variavel.tolist()
qualitative_variables.remove('Surname')

st.header("A dataset of Banking Customer Churn")
st.write(df)

st.title("Scatter plot")
st.subheader("Select Scatter Plot Axes")

num_columns = dic.query("tipo == 'quantitativa'").variavel.tolist()
cat_columns = [None] + qualitative_variables

with st.expander("Scatter Plot Configuration"):
    x_axis_scatter = st.selectbox('X axis', num_columns, index=0, key='scatter_x')
    y_axis_scatter = st.selectbox('Y axis', num_columns, index=1, key='scatter_y')
    c_axis_scatter = st.selectbox('Color', cat_columns, key='scatter_c')
    
fig, ax = plt.subplots()
sns.scatterplot(x=x_axis_scatter, y=y_axis_scatter, hue=c_axis_scatter, data=df)
st.pyplot(fig)

st.title("Box plot")
st.subheader("Select Box Plot Axes")

with st.expander("Box Plot Configuration"):
    x_axis_box = st.selectbox('X axis', num_columns, index=0, key='box_x')
    y_axis_box = st.selectbox('Y axis', num_columns, index=1, key='box_y')
    c_axis_box = st.selectbox('Color', cat_columns, key='box_c')

fig_box = px.box(df, x=x_axis_box, y=y_axis_box, color=c_axis_box)
st.plotly_chart(fig_box)
