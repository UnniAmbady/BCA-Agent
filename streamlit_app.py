import streamlit as st
from enquiry import enquiry
from requirements import requirement
from agents import agents
from ack import ack

# Title and author information
st.title("BCA Project")
st.write(":by Woon Wei & UNNI")

# Creating columns for checkbox layout
col1, col2, col3, col4 = st.columns(4)

# Checkboxes with expanders for each section
with col1:
    if st.checkbox("Enquiry"):
        with st.expander("Enquiry Section", expanded=True):
            enquiry()

with col2:
    if st.checkbox("Requirements"):
        with st.expander("Requirements Section", expanded=True):
            requirement()

with col3:
    if st.checkbox("Agent"):
        with st.expander("Agent Section", expanded=True):
            agents()

with col4:
    if st.checkbox("Ack"):
        with st.expander("Ack Section", expanded=True):
            ack()

