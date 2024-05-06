"""Command-line tool to get an answer to a question based on chat history."""

import os
import warnings

import click
from dotenv import load_dotenv

from service.api_service import ApiService

# Suppress Warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Initialize ApiService with environment variables
api_service = ApiService(os.getenv("PINECONE_INDEX_NAME"))


@click.command()
@click.option(
    "--question", prompt="Please enter your question", help="The question to ask."
)
@click.option("--history", default="", help="The history of previous questions.")
def answer(question, history):
    """
    Command-line tool to get an answer to a question based on chat history.

    Parameters:
        question (str): The question to be asked.
        history (str): A semicolon-separated string of previous chat messages.
    """
    try:
        response = api_service.get_answer(question, history)
        print(response["answer"])
    except Exception as e:
        click.echo((str(e)))


if __name__ == "__main__":
    answer()
