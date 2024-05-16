"""Command-line tool to get an answer to a question based on vector database."""

import warnings
import argparse

from global_variables import pinecone_index
from service.api_service import ApiService

api_service = ApiService(pinecone_index)

# Ignore LangChainDeprecationWarning
warnings.filterwarnings("ignore")


def answer(question, history):
    """
    Command-line tool to get an answer to a question based on vector database.

    This tool utilizes the ApiService to fetch an answer to the provided
    question using the contextual chat history stored in the vector database.
    """
    try:
        response = api_service.get_answer(question, history)
        print(response["answer"])
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get an answer to a question.")
    parser.add_argument("--question", type=str, help="The question to ask.")
    parser.add_argument(
        "--history", default="", help="The history of previous questions."
    )

    args = parser.parse_args()
    answer(args.question, args.history)
