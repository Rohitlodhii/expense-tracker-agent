import os

from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()



OPENAI_BASE_URL=os.environ["OPENAI_BASE_URL"]
OPENAI_MODEL=os.environ["OPENAI_MODEL"]

# return the api as a function

def get_api_key() -> SecretStr:
    return SecretStr(os.environ["OPENAI_API_URL"])
