import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from database import load_data

from queries import *

from charts import sales_by_store
from charts import holidy_eff
from charts import fuel_eff
from charts import temp_eff
from charts import unemp_eff

from queries import BEST_SALES





st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("WALMART SALES DASHBOARD",width="stretch",text_alignment="justify")
st.subheader("We will study the sales data of one of the largest retailers in the world",text_alignment="justify",divider=True,width="stretch")


df = load_data(ALL_DATA)


st.sidebar.title("USE FILTERS")

number_stores = st.sidebar.multiselect(
    " SELECT NUMBER OF STORES",
    df["Store"].unique(),
    
    

)

fuel_rate = st.sidebar.multiselect(
    "SELECT FUEL PRICE RATE",
    options=df["Fuel_Price"].unique()
    
)

date = st.sidebar.multiselect(
    "SELECT MONTH",
        df['New_Date'].unique()
)

filtered_df = df.copy()

if number_stores:
    filtered_df = filtered_df[
        filtered_df["Store"].isin(number_stores)
    ]

if fuel_rate:
    filtered_df = filtered_df[
        filtered_df["Fuel_Price"].isin(fuel_rate)
    ]

if date:
    filtered_df = filtered_df[
        filtered_df["New_Date"].isin(date)
    ]

TOTAL_SALES = filtered_df['Weekly_Sales'].sum()

AVG_SALES = filtered_df['Weekly_Sales'].mean()

row = st.container(horizontal=True)

with row:
    st.metric(
        "TOTAL SALES", value=f"{TOTAL_SALES:.2f}",chart_data=filtered_df, chart_type="bar", border=True, delta='float',width ='stretch'
    )

    

    st.metric(
        "AVG SALES", value=f"{AVG_SALES:.2f}", chart_data=filtered_df, chart_type="bar", border=True, delta='float',width ='stretch'
    )




col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(sales_by_store(), use_container_width=True,theme='streamlit')

with col2:
    st.plotly_chart(holidy_eff(), use_container_width=True,theme='streamlit')
    
#col3, col4 = st.columns(2)

tab1, tab2, tab3 = st.tabs(["FUEL PRICE EFFECT","TEMPERATURE EFFECT","UNEMPLOYMENT EFFECT"])

with tab1:
    st.plotly_chart(fuel_eff(), use_container_width=True,theme='streamlit')

with tab2:
    st.plotly_chart(temp_eff(), use_container_width=True,theme='streamlit')

with tab3:
    st.plotly_chart(unemp_eff(), use_container_width=True,theme='streamlit')


best_sales = load_data(BEST_SALES)
st.markdown(" Top Five stores perform consistently well")
st.table(best_sales,border=True,width="content")

st.markdown("---")
st.caption("© 2026 Shawana Ahsan. All Rights Reserved.")


    
    