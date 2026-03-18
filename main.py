import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call it at the top of your app
local_css("assets/style.css")

st.title("Growth Calendar")