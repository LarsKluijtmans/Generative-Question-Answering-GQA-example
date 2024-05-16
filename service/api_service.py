"""Service to interact with AI for answering questions based on chat history."""

from langchain.chains.base import Chain
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone as LangPinecone
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class ApiService:
    """
    Service to interact with AI for answering questions based on chat history.

    This service utilizes a conversational retrieval model to provide answers
    based on contextual chat history. It interfaces with Pinecone vector stores
    and leverages OpenAI's language model for conversational understanding.
    """

    QA_template = """
    You are a helpful AI assistant. Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say you don't know. DO NOT try to make up an answer.
    If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.

    Chat History: {chat_history}

    Helpful answer in markdown:
    """

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", QA_template),
            ("human", "{question}"),
        ]
    )

    def __init__(
        self,
        pinecone_index_name: str,
    ):
        """
        Initialize the ApiService.

        Parameters:
            pinecone_index_name (str): The name of the Pinecone index.
        """
        self.pinecone_index_name = pinecone_index_name

    def get_answer(self, question: str, history: str) -> dict[str, any]:
        """
        Get an answer to a question based on chat history.

        Parameters:
            question (str): The question to be answered.
            history (str): Previous chat messages.

        Returns:
            dict[str, any]: The answer to the question, along with the chat history.
        """
        vector_store = self._get_pinecone()

        chain = self._get_chain(vector_store)

        # Ask a question using chat history
        response = chain.invoke({"question": question, "chat_history": history})

        return response

    def _get_pinecone(self) -> LangPinecone:
        """
        Create and return a Pinecone vector store.

        Returns:
            LangPinecone: The Pinecone vector store.
        """
        vector_store = LangPinecone.from_existing_index(
            embedding=OpenAIEmbeddings(),
            index_name=self.pinecone_index_name,
            text_key="text",
        )
        return vector_store

    def _get_chain(self, vector_store: LangPinecone) -> Chain:
        """
        Create a conversational retrieval question-answering (QA) chain.

        Parameters:
            vector_store (LangPinecone): The vector store used for retrieval.

        Returns:
            Chain: The created QA chain.
        """
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        retriever = vector_store.as_retriever()
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            condense_question_prompt=self.chat_template,
        )
        return chain
