import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit as st
from database import *
from queries import *
from database import load_data
from queries import TOTAL_SALES_PER_STORE
from queries import HOLIDAY_EFFECTS
from queries import FUEL_EFF
from queries import TEMP_EFF
from queries import unemp_rate_eff


def sales_by_store():
    df = load_data(TOTAL_SALES_PER_STORE)


    fig = px.bar(
        df,
        x="Store",
        y="Number of Sales",
        color="Number of Sales",
        title="TOTAL SALES PER STORES",
        color_continuous_scale="Viridis"
        
    )



    return fig

def holidy_eff():
    df = load_data(HOLIDAY_EFFECTS)


    fig = px.bar(
        df,
        x="Holiday_Flag",
        y="average sales",
        color="average sales",
        title="How do holiday weeks affect sales",
        color_continuous_scale="Viridis"
        
    )



    return fig

def fuel_eff():
    df = load_data(FUEL_EFF)


    fig = px.scatter(

        df,
        x="Fuel_Price",
        y="WEEKLY AVG SALES",
        color="WEEKLY AVG SALES",
        title="Does fuel price affect sales",
        color_continuous_scale="Viridis"
        
    )



    return fig

def temp_eff():
    df = load_data(TEMP_EFF)


    fig = px.scatter(

        df,
        x="Temperature",
        y="WEEKLY AVG SALES",
        color="WEEKLY AVG SALES",
        title="Does Temperature  affect sales",
        color_continuous_scale="Viridis"
        
    )



    return fig

def unemp_eff():
    df = load_data(unemp_rate_eff)


    fig = px.scatter(

        df,
        x="Unemployment",
        y="WEEKLY AVG SALES",
        color="WEEKLY AVG SALES",
        title="Does Unemployment affect sales",
        color_continuous_scale="Viridis"
        
    )

    return fig