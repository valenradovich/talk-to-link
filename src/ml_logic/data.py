from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_data(list_urls) -> list :
    """Load data from URLs provided by the user.

    Keyword arguments:
    list_urls -- list of URLs provided by the user
    Return: data - list of strings
    """

    try:
        loader = UnstructuredURLLoader(urls=list_urls)
        data = loader.load()
    except Exception as e:
        print("Error: Could not load data. Please check your URLs and try again.")
        print(e)

    return data

def split_data(data) -> list :
    """Split data provided by the user into chunks.

    Keyword arguments:
    data -- list of strings
    Return: docs - list of strings
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
        )
        docs = text_splitter.split_documents(data)
    except Exception as e:
        print("Error: Could not split data. Please check your data and try again.")
        print(e)

    return docs

def data_workflow(list_urls) -> list :
    """Load data from URLs provided by the user, split it into chunks and return the list of chunks.

    Keyword arguments:
    list_urls -- list of URLs provided by the user
    Return: docs - list of strings
    """
    data = load_data(list_urls)
    print("Data loaded successfully.")

    docs = split_data(data)
    print("Data splitted successfully.")

    return docs
