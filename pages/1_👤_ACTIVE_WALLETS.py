import pandas as pd
import streamlit as st
import snowflake.connector
from snowflake.connector import DictCursor

def execute_sql(sql_string, **kwargs):
  conn = snowflake.connector.connect(user=st.secrets["user"],
                                     password=st.secrets["password"],
                                     account=st.secrets["account"],
                                     warehouse=st.secrets["warehouse"],
                                     database=st.secrets["database"],
                                     schema=st.secrets["schema"])

  sql = sql_string.format(**kwargs)
  res = conn.cursor(DictCursor).execute(sql)
  results = res.fetchall()
  conn.close()
  return results

st.set_page_config(layout="wide", page_title="Active Wallets", page_icon="👤")

st.title("Active Wallets")

df = execute_sql('''
SELECT * FROM SCROLLSTATS_BD_ACTIVE_WALLETS
''').to_pandas()

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