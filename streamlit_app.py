import streamlit as st
from src.ml_logic.model import load_model
from src.interface.main import prepare_data, talk_to_link
from src.params import VECTOR_DB_PATH

st.set_page_config(
    page_title="Talk to Links", page_icon="💬", layout="wide", initial_sidebar_state="expanded"
)

st.title("Talk to Links 💬")
st.caption("🚀 Chat with every link you want.")

st.sidebar.markdown("## How to use")
st.sidebar.write(
    """
    1. Enter your [OpenAI API](https://platform.openai.com/account/api-keys) key below🔑
    2. Enter the URLs you want to process🔗
    3. Done! Now, your imagination is the limit💬
    """)

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="You can get your API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).")

if openai_api_key:
    llm = load_model(openai_api_key)
else:
    llm = None

st.sidebar.divider()

st.sidebar.markdown("## Article URLs")

urls = []
n_urls = st.sidebar.number_input("How many URLs do you want to process?", min_value=1, max_value=5)

for i in range(n_urls):
    url = st.sidebar.text_input(f"🔗 {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

st.sidebar.divider()

st.sidebar.markdown("## About")
st.sidebar.write(
    """
    **💬Talk to Links** allows you to speak with every link you want.
    It uses [OpenAI's API](https://openai.com/), [LangChain](https://www.langchain.com) and [FAISS](https://github.com/facebookresearch/faiss).

    This tool is just a demo created for testing purposes. You can find the source code on [GitHub](https://github.com/valenradovich/talk-to-link). I appreciate any feedback or suggestions.

    Made by [Valentin Radovich](https://www.linkedin.com/in/valentin-fernandez-radovich/).
    """
    )
main_placeholder = st.empty()

if process_url_clicked:
    if not openai_api_key:
        st.error("❌ Please enter your OpenAI API key.")
        st.stop()
    st.info("⏳ Please wait while we process your URLs...")
    done = prepare_data(urls, openai_api_key)

    if done is False:
        st.exception(
            "❌ Could not prepare data. Please check your urls and try again."
        )
    else:
        st.success(
            "✅ Data successfully loaded. You can now ask questions to the links you provided."
        )

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input()

if prompt:
    if not openai_api_key:
        st.error("❌ Please enter your OpenAI API key.")
        st.stop()
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    result = talk_to_link(llm=llm, prompt=prompt, file_path=VECTOR_DB_PATH)
    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.chat_message("assistant").write(result["answer"] + "\nSources: " + source)
    else:
        st.chat_message("assistant").write(result["answer"])
