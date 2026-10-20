from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
from streamlit.typing import UploadedFile


@st.cache_resource
def load_ocr() -> PaddleOCR:
    return PaddleOCR(use_angle_cls=True, lang="en")


def ocr_file(file: UploadedFile, key: str) -> None:
    st.subheader("OCR RESULTS")

    if not st.button("Run OCR", key=key):
        return

    with st.spinner("Processing file..."):
        ocr = load_ocr()
        if file.type == "application/pdf":
            with TemporaryDirectory() as temp_dir:
                pdf_path = Path(temp_dir) / (Path(file.name).name or "upload.pdf")
                if pdf_path.suffix.lower() != ".pdf":
                    pdf_path = pdf_path.with_suffix(".pdf")
                pdf_path.write_bytes(file.getvalue())
                results = ocr.predict(input=str(pdf_path))
        else:
            file.seek(0)
            image = Image.open(file).convert("RGB")
            results = ocr.predict(input=np.array(image))

    extracted_text: list[str] = []
    for result in results:
        result_data = result.json
        if isinstance(result_data, dict):
            page_data = result_data.get("res", result_data)
            if isinstance(page_data, dict):
                texts = page_data.get("rec_texts", [])
                if isinstance(texts, list):
                    extracted_text.extend(str(text) for text in texts)

    if extracted_text:
        st.markdown("**Extracted Text:**")
        for text in extracted_text:
            st.write(text)
    else:
        st.warning("No text found in the file.")
