# Generative Question Answering (GQA) example

## Introduction
This command-line tool provides a convenient way to retrieve answers to questions based on contextual chat history 
stored in a vector database. It leverages advanced AI models to understand the questions and provide relevant responses.

### Install Dependencies:

Ensure that the required dependencies are installed. 

These dependencies include Pinecone, Transformers, and dotenv. You can install them via pip:

```commandline
py -m venv venv
.\venv\Scripts\activate
pip install -r requirments.txt
```

### Setup Environment Variables: 

Before running the script, set up a .env file in the root directory of the project. 

This file should contain the following variables:

- PINECONE_API_KEY: Your Pinecone API key.
- PINECONE_INDEX_NAME: The name of the Pinecone index where the vectors will be stored.
- OPENAI_API_KEY: Your OpenAI API key.

### Running the Tool

To use the command-line tool, follow these steps:

- Navigate to the directory where the tool is located
- Run the script with the --question flag followed by the question you want to ask.
- Optionally, provide the --history flag followed by the history of previous chat messages.

```commandline
py answer_tool.py --question "What is the capital of France?" --history "Previous chat messages here."
```

#### Input Paramaters: 

--question: Specifies the question you want to ask.
--history: (Optional) Provides the history of previous chat messages. This helps the AI model understand the context better.

#### Output: 

The tool will return the AI-generated answer to your question.

## Data Ingestor

The **data_ingestor** script facilitates the ingestion of documents from a specified folder and subsequently vectorizes 
them using Pinecone, a vector database service. The resulting vectors can then be utilized for various downstream tasks 
such as similarity search, recommendation systems, or clustering.

### Usage

To use the script, follow these steps:

#### Install Dependencies:

Follow the **Install Dependencies** steps previously mentioned.

#### Setup Environment Variables: 

Follow the **Setup Environment Variables** steps previously mentioned.

#### Run the Script: 

Execute the script, specifying the path to the folder containing the documents you want to ingest. For example:

```commandline
py data_ingestor.py --folder-path test_docs
```

#### Example
Consider a scenario where you have a collection of PDF documents in a folder named docs. 
By running the script with this folder path, the documents will be ingested, vectorized using OpenAI, and stored in 
Pinecone under the specified index name.

#### Note
Ensure that you have the necessary permissions and access to the Pinecone and OpenAI services before running the script.
Also, consider the potential costs associated with API usage, especially for large-scale document processing tasks.

