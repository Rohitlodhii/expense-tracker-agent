
import streamlit as st

from components.file_upload import file_uploader

st.set_page_config(
    page_title="Ai expense tracker",
    page_icon="💵",
    layout="centered"
)


st.title("Ai Expense Tracker")


st.divider()

file_uploader(key="main_uploader")
