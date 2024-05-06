"""Global variables"""

import os
from dotenv import load_dotenv

load_dotenv()
pinecone_index = os.getenv("PINECONE_INDEX_NAME")
