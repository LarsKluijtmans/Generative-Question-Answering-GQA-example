"""Ingest documents from a folder and vectorize them using Pinecone."""

import argparse

from langchain.document_loaders.directory import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.pinecone import Pinecone as LangPinecone
from pinecone import Pinecone


def run(folder_path):
    """
    Ingest documents from a folder and vectorize them using Pinecone.
    """
    try:
        pinecone = Pinecone()
        directory_loader = DirectoryLoader(folder_path)

        raw_docs = directory_loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )

        docs = text_splitter.split_documents(raw_docs)
        print("Raw text chunks:", docs)

        print("Vectorizing documents")
        embeddings = OpenAIEmbeddings()
        index = pinecone.Index("test")

        LangPinecone.from_documents(
            docs, embeddings, {"pineconeIndex": index, "textKey": "text"}
        )
        print("Document ingestion complete")
    except Exception as error:
        raise RuntimeError("Failed to ingest your data") from error


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest documents and vectorize them.")
    parser.add_argument(
        "--folder_path", default="docs", help="Path to the folder containing documents."
    )

    args = parser.parse_args()
    run(args.folder_path)
