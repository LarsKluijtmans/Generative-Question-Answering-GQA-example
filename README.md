# Generative Question Answering (GQA) example

## Data Ingestor

The **data_ingestor** script facilitates the ingestion of documents from a specified folder and subsequently vectorizes 
them using Pinecone, a vector database service. The resulting vectors can then be utilized for various downstream tasks 
such as similarity search, recommendation systems, or clustering.

### Usage

To use the script, follow these steps:

#### Install Dependencies:

Ensure that the required dependencies are installed. 

These dependencies include Pinecone, Transformers, and dotenv. You can install them via pip:

```commandline
py -m venv venv
.\venv\Scripts\activate
pip install -r requirments.txt
```

#### Setup Environment Variables: 

Before running the script, set up a .env file in the root directory of the project. 

This file should contain the following variables:

- PINECONE_API_KEY: Your Pinecone API key.
- PINECONE_INDEX_NAME: The name of the Pinecone index where the vectors will be stored.
- OPENAI_API_KEY: Your OpenAI API key.
- 
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

