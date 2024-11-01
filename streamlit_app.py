import streamlit as st
from enquiry import enquiry
from requirements import requirement
from agents import agents
from ack import ack

# Define a reusable function to return to the main page
def go_home():
    st.experimental_set_query_params()  # Resets query parameters, taking user back to the main page

# Title and author information
st.title("BCA Project")
st.write(":by Woon Wei & UNNI")

# Buttons to trigger functions
if st.button("Enquiry"):
    enquiry()

if st.button("Requirements"):
    requirement()

if st.button("Agent"):
    agents()

if st.button("Ack"):
    ack()

