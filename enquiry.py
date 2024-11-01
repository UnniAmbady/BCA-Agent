import streamlit as st
from streamlit_app import go_home

def enquiry():
    st.write("This is the Enquiry section.")
    # Add any additional functionality needed for the Enquiry section here.
    
    # Go Home button at the bottom left
    st.markdown('<div style="position: absolute; bottom: 0; left: 0;">', unsafe_allow_html=True)
    if st.button("Go Home"):
        go_home()
    st.markdown('</div>', unsafe_allow_html=True)
