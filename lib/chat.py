

# Setup the agent and give it the tools

from langchain.agents import create_agent

from helpers.model import llm
from lib.csv import append_data_to_csv, check_if_csv_exists, create_empty_csv, get_last_total


# Lets give work to agent to do all


agent = create_agent(
    model=llm,
    tools = [check_if_csv_exists , create_empty_csv , append_data_to_csv , get_last_total ],
    system_prompt="You are a Expense tracker agent , you will be given a receipt string from which you have to extract neccessary details and have to add to the csv : you can use the tools to check if csv is created or not , what is the last total of expenses , add data to csv etc"
)
