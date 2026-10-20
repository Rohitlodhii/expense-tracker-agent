import os
from pathlib import Path

import pandas as pd
from langchain.tools import tool

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_DIR = BASE_DIR / "csv"
CSV_DIR.mkdir(parents=True, exist_ok=True)
FILEPATH = CSV_DIR / "accounts.csv"

COLUMNS = [
    "Date", "Service", "Payment Type",
    "Amount Paid", "Amount Received",
    "Total Gain", "Total Loss", "Total Sum"
]

NEW_SERVICE_DF = pd.DataFrame([[
    "00/00/0000", "Nil", "Nil", "00.00", "00.00", "00.00", "00.00", "00.00"
]], columns=COLUMNS)


def _check_if_csv_exists() -> bool:
    return FILEPATH.exists() and FILEPATH.stat().st_size > 0


@tool
def check_if_csv_exists() -> bool:
    """Checks if accounts.csv exists and is not empty. Returns True or False."""
    return _check_if_csv_exists()


@tool
def create_empty_csv():
    """Creates a new accounts.csv if it doesn't already exist."""
    if not _check_if_csv_exists():
        NEW_SERVICE_DF.to_csv(FILEPATH, mode='w', index=False, header=True)
        return {
            "status": "Success",
            "msg": "New csv created and initialized with nil and zeros."
        }
    return {
        "status": "Failed",
        "msg": "accounts.csv already exists; try appending data instead."
    }


@tool
def append_data_to_csv(
    date: str,
    service: str,
    payment_type: str,
    amount_paid: str,
    amount_received: str,
    total_gain: str,
    total_loss: str,
    total: str
):
    """
    Appends a new expense/income transaction row to accounts.csv.
    The 'total' represents the new Total Sum, which can be derived using the last total from get_last_total.
    """
    new_data = pd.DataFrame(
        [[date, service, payment_type, amount_paid, amount_received, total_gain, total_loss, total]],
        columns=COLUMNS
    )
    new_data.to_csv(FILEPATH, mode='a', index=False, header=False)
    return {
        "status": "Success",
        "msg": f"Added {service} amount data to the csv."
    }


@tool
def get_last_total():
    """Returns the last total amount recorded in accounts.csv."""
    if not _check_if_csv_exists():
        return {
            "status": "Failed",
            "msg": "Cannot get last total; file does not exist or is empty."
        }

    df = pd.read_csv(FILEPATH)
    if not df.empty:
        last_total = df.iloc[-1]["Total Sum"]
        return {
            "status": "Success",
            "msg": f"Last total is {last_total}"
        }

    return {
        "status": "Failed",
        "msg": "CSV file has no data rows."
    }
