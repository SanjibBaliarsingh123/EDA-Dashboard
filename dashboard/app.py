import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv("C:/Users/sbali/OneDrive/Desktop/project EDA/data/sales_data_sample.csv", encoding='latin1')

# Title
st.title("📊 Sales Exploratory Data Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")

country = st.sidebar.selectbox("Select Country", df['COUNTRY'].unique())
product = st.sidebar.selectbox("Select Product Line", df['PRODUCTLINE'].unique())

# Filtered data
filtered_df = df[(df['COUNTRY'] == country) & (df['PRODUCTLINE'] == product)]

# KPI cards
total_sales = filtered_df['SALES'].sum()
total_orders = filtered_df['ORDERNUMBER'].nunique()
avg_sales = filtered_df['SALES'].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Average Sales", f"${avg_sales:,.2f}")

st.markdown("---")

# Layout for charts
col4, col5 = st.columns(2)

# Product line sales chart
with col4:
    st.subheader("Sales by Product Line")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x='PRODUCTLINE', y='SALES', data=filtered_df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Deal size chart
with col5:
    st.subheader("Deal Size Distribution")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.countplot(x='DEALSIZE', data=filtered_df, ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# Year wise sales
st.subheader("Year-wise Sales Trend")

fig3, ax3 = plt.subplots(figsize=(10,4))
sns.barplot(x='YEAR_ID', y='SALES', data=filtered_df, ax=ax3)
st.pyplot(fig3)

# Raw data
with st.expander("View Raw Data"):
    st.dataframe(filtered_df)