
import streamlit as st

from components.file_upload import file_uploader

st.set_page_config(
    page_title="Ai expense tracker",
    page_icon="💵",
    layout="centered"
)


st.title("Ai Expense Tracker")


st.divider()

uploaded_file = file_uploader(key="main_uploader")

if uploaded_file:
    st.divider()
    st.info("File is acknowledged");
    st.text(uploaded_file.type)
