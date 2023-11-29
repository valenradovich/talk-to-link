import streamlit as st
from src.ml_logic.model import load_model
from src.interface.main import prepare_data, talk_to_link
from src.params import VECTOR_DB_PATH

llm = load_model()

st.title("intelliNotes📝")
st.sidebar.title("Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()

if process_url_clicked:
    main_placeholder.text("Data Loading...Started...✅✅✅")
    prepare_data(urls)

prompt = main_placeholder.text_input("Question")

if prompt:
    result = talk_to_link(llm=llm, prompt=prompt, file_path=VECTOR_DB_PATH)
    st.header("Answer")
    st.write(result["answer"])

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.write(source)
