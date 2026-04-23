import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/sbali/OneDrive/Desktop/project EDA/data/sales_data_sample.csv", encoding='latin1')

st.title("Sales EDA Dashboard")

st.dataframe(df.head())

country = st.selectbox("Select Country", df['COUNTRY'].unique())

filtered_df = df[df['COUNTRY'] == country]

st.dataframe(filtered_df)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x='PRODUCTLINE', y='SALES', data=filtered_df, ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)