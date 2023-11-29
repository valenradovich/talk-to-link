from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle

def load_vector_store(docs) -> FAISS:
    """Load vector store from documents provided by the user.

    Keyword arguments:
    docs -- list of splitted documents
    Return: vector store
    """

    try:
        embeddings = OpenAIEmbeddings()
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
    except Exception as e:
        print("❌ Could not load vector store. Please check your data and try again.")
        print(e)

    return vectorstore_openai

def save_vector_store(vectorstore_openai, file_path) -> None:
    """Save vector store to file.

    Keyword arguments:
    vectorstore_openai -- vector store
    filename -- name of the file
    Return: None
    """

    try:
        vectorstore_openai.save_local(file_path)
    except Exception as e:
        print("❌ Could not save vector store. Please check your data and try again.")
        print(e)
