#--------------------------------------------------------#
# Imports
#--------------------------------------------------------#
import streamlit as st

#--------------------------------------------------------#
# Main Body
#--------------------------------------------------------#

st.set_page_config(
  page_title="Scroll BD",
  page_icon="✨",
  layout="wide",
)

# Create the title at the tp of page
st.title('Scroll BD Data')

st.markdown(
    """
    This app allows you to download, view and edit data in the Scroll BD database.
    - ACTIVE WALLETS: Download historical active wallet data for Scroll projects.
    - TVL: Download historical TVL data for Scroll projects.
    - TRANSACTIONS: Download historical transaction quantity data for Scroll projects.
    - PROJECT LABELS: View and edit project - contract labels.
    
    **👈 Select a table from the sidebar**
"""
)