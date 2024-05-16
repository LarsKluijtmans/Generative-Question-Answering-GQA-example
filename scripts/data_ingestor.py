"""Ingest documents from a folder and vectorize them using Pinecone."""

import argparse
import os

from langchain.document_loaders.directory import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.pinecone import Pinecone as LangPinecone
from pinecone import Pinecone

from dotenv import load_dotenv
from transformers import logging

logging.set_verbosity_error()


def run(folder_path):
    """
    Ingest documents from a folder and vectorize them using Pinecone.
    """
    load_dotenv()
    pinecone_index = os.getenv("PINECONE_INDEX_NAME")

    pinecone = Pinecone()
    directory_loader = DirectoryLoader(folder_path)

    print("Loading documents")
    raw_docs = directory_loader.load()

    print("Create text spliter")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    print("Chunk the data")
    docs = text_splitter.split_documents(raw_docs)
    print("Raw text chunks:", len(docs))

    print("Initialize embeddings")
    embeddings = OpenAIEmbeddings()

    print("Insert documents into pinecone")
    LangPinecone.from_documents(docs, embeddings, index_name=pinecone_index)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest documents and vectorize them.")
    parser.add_argument(
        "--folder-path", default="docs", help="Path to the folder containing documents."
    )

    args = parser.parse_args()
    run(args.folder_path)
