from src.ml_logic.data import data_workflow
from src.ml_logic.model import load_model, run_model
from src.ml_logic.vector_db import load_vector_store, save_vector_store

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def talk_to_link(llm, prompt, file_path):
    try:
        vectorstore = FAISS.load_local(file_path, OpenAIEmbeddings())
        chain = run_model(llm, vectorstore)
        result = chain({"question": prompt}, return_only_outputs=True)

        return result # this function should return the result or this code should be in the streamlit app
    except Exception as e:
        print("❌ Could not run model. Please check your data and try again.")
        print(e)

def prepare_data(list_urls):
    file_path = "src/ml_logic/vector_store"

    # loading and splitting urls
    docs = data_workflow(list_urls)

    # loading and saving vector store
    vectorstore_openai = load_vector_store(docs)
    save_vector_store(vectorstore_openai, file_path)

    # prompt = input("Enter a prompt: ")

    # if prompt:
    #     result = talk_to_link(prompt, file_path)
    #     print(result['answer'])
    #     print(f"Sources: {result['sources']}")

    return
