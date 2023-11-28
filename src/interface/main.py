from src.ml_logic.data import data_workflow
from src.ml_logic.model import load_model, run_model
from src.ml_logic.vector_db import load_vector_store, save_vector_store
import pickle

def talk_to_link(prompt, file_path):
    llm = load_model()

    with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = run_model(llm, vectorstore)
            result = chain({"question": prompt}, return_only_outputs=True)

            return result # this function should return the result or this code should be in the streamlit app






if __name__ == "__main__":
    pass
