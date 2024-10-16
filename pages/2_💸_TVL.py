################################
# Imports
################################
import pandas as pd
import streamlit as st
import snowflake.connector
from snowflake.connector import DictCursor

st.set_page_config(layout="wide", page_title="TVL", page_icon="💸")

################################
# Helper Functions
################################
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

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

################################
# Data Retrieval and Processing 
################################

raw_data = execute_sql('''
SELECT MONTH, NAME, ROUND(TVL) AS TVL FROM SCROLLSTATS.DBT_SCROLLSTATS.SCROLL_BD_TVL
''')

df = pd.DataFrame(raw_data)
df['MONTH'] = pd.to_datetime(df['MONTH'], format='%Y-%m-%d')
pivoted_df = df.pivot(index='NAME', columns='MONTH', values='TVL')
pivoted_df = pivoted_df.reset_index()
pivoted_df.columns = ['NAME'] + [d.strftime('%b %Y') for d in pivoted_df.columns[1:]]
csv = convert_df(pivoted_df)

################################
# Frontend
################################

st.title("TVL")

st.markdown("**Click DOWNLOAD to get TVL data in CSV format**")
st.download_button(
    label="DOWNLOAD",
    data=csv,
    file_name="scroll_bd_tvl.csv",
    mime="text/csv",
)