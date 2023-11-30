from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain

def load_model() -> OpenAI:
    """Load model.

    Keyword arguments:
    Return: llm - language model
    """
    try:
        llm = OpenAI(temperature=0, max_tokens=500, model="text-davinci-003") # model="gpt-3.5-turbo"
    except Exception as e:
        print("❌ Could not load model. Please check your API key and try again.")
        print(e)

    return llm

def run_model(llm, vectorstore):
    """Run model.

    Keyword arguments:
    llm -- language model
    vectorstore -- vector store
    Return: chain - language chain
    """

    try:
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
    except Exception as e:
        print("❌ Could not run model. Please check your data and try again.")
        print(e)

    return chain
