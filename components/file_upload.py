import pandas as pd
import streamlit as st

from helpers.file import format_size
from helpers.ocr import ocr_file


def file_uploader(key="file_uploader"):

    st.subheader("Upload files here")
    uploaded_file = st.file_uploader(
        "Upload images or PDF documents",
        type=["png", "jpeg", "jpg", "pdf"],
        accept_multiple_files=False,
        key=key,
    )

    ocr_text = None

    if uploaded_file is not None:
        st.success("Successfully uploaded file!")

        # Display file preview & details
        st.write("### 🔍 File Details & Preview")
        with st.expander(f"📄 {uploaded_file.name}", expanded=True):
            col1, col2 = st.columns([1, 2])

            with col1:
                st.markdown(f"**Name:** `{uploaded_file.name}`")
                st.markdown(f"**Size:** `{format_size(uploaded_file.size)}`")
                st.markdown(f"**Type:** `{uploaded_file.type}`")

            with col2:
                if uploaded_file.type.startswith("image/"):
                    st.image(uploaded_file, caption=uploaded_file.name, width="content")
                elif uploaded_file.type == "application/pdf":
                    st.info("📄 PDF File loaded.")
                    st.download_button(
                        label=f"Download {uploaded_file.name}",
                        data=uploaded_file,
                        file_name=uploaded_file.name,
                        mime=uploaded_file.type,
                    )

        # OCR processing section
        ocr_text = ocr_file(uploaded_file, key=f"{key}_ocr")

    return uploaded_file, ocr_text
