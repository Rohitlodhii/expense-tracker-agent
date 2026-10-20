import os
from pathlib import Path
from typing import Any

os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"
os.environ["FLAGS_enable_pir_api"] = "0"

import pandas as pd
import streamlit as st
from langchain_core.messages import BaseMessage, HumanMessage

from components.file_upload import file_uploader
from lib.chat import agent
from lib.csv import FILEPATH

st.set_page_config(
    page_title="Ai expense tracker",
    page_icon="💸",
    layout="centered"
)


st.title("Ai Expense Tracker")


st.divider()

uploaded_file, ocr_str = file_uploader(key="main_uploader")

if ocr_str:
    print("--- Extracted OCR Text ---")
    print(ocr_str)

    st.divider()
    st.subheader("🤖 AI Agent Expense Extraction")

    agent_state_key = f"{uploaded_file.name}_agent_result" if uploaded_file else "agent_result"

    if st.button("Add Details to CSV with Agent", key="add_to_csv_btn", type="primary"):
        with st.spinner("Agent is analyzing the receipt and updating accounts.csv..."):
            prompt = (
                "You are an expense tracker assistant. Below is the text extracted from a receipt/bill using OCR.\n"
                "Please extract all necessary transaction details (date, service/vendor, payment type, amount paid, "
                "amount received, total gain, total loss, and new total sum).\n"
                "Use your tools to check if accounts.csv exists (create it if needed), "
                "fetch the last total, and append the new data to the CSV.\n\n"
                f"--- RECEIPT OCR TEXT ---\n{ocr_str}"
            )
            try:
                response: dict[str, Any] = agent.invoke({"messages": [HumanMessage(content=prompt)]})  # type: ignore[reportUnknownMemberType]
                messages: list[Any] = response.get("messages", [])
                if messages:
                    last_msg: Any = messages[-1]
                    final_answer: str = str(last_msg.content) if isinstance(last_msg, BaseMessage) else str(last_msg)
                else:
                    final_answer = "No response from agent."

                st.session_state[agent_state_key] = final_answer

                print("--- Agent Response ---")
                print(final_answer)

            except Exception as e:
                error_msg = str(e)
                if "502" in error_msg or "Bad gateway" in error_msg.lower():
                    st.error(
                        "⚠️ **502 Bad Gateway:** The API provider (`api.apinex.bond`) is temporarily overloaded or down. "
                        "Please wait 30–60 seconds and try again."
                    )
                else:
                    st.error(f"⚠️ **Error running AI agent:** {error_msg}")
                print(f"Error during agent invocation: {e}")

    if agent_state_key in st.session_state and st.session_state[agent_state_key]:
        st.success("✅ Transaction Processed by Agent!")
        st.markdown(str(st.session_state[agent_state_key]))

# Show accounts.csv preview if it exists
if FILEPATH.exists() and FILEPATH.stat().st_size > 0:
    st.divider()
    st.subheader("📊 Accounts Data")
    df = pd.read_csv(FILEPATH)
    st.dataframe(df, use_container_width=True)
