import pandas as pd
import json
import streamlit as st
import time

st.set_page_config(layout="wide", page_title="Active Wallets", page_icon="👤")

conn = st.connection("snowflake")

st.title("Active Wallets")

session = conn.session()

df = session.table("SCROLLSTATS_BD_ACTIVE_WALLETS").to_pandas()

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(df)

st.markdown("**Click DOWNLOAD to get active wallet data in CSV format**")
st.download_button(
    label="DOWNLOAD",
    data=csv,
    file_name="scroll_bd_active_wallets.csv",
    mime="text/csv",
)