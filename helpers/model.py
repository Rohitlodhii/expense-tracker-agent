from langchain_openai import ChatOpenAI

from config import OPENAI_BASE_URL, OPENAI_MODEL, get_api_key

llm = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=get_api_key(),
    base_url=OPENAI_BASE_URL,
    temperature=0.7,
    max_retries=3,
    timeout=60,
)
