import streamlit as st
from bookstore import Bookstore

st.set_page_config(page_title="Paisasmart Chatbot", page_icon=":books:")
    
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title('Paisasmart Bookstore')

store = Bookstore()

for message in st.session_state.messages:
    # if message["role"] == "context":
    #     with st.expander("Context"):
    #         st.markdown(message["content"])
    #     continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your question"):
    with st.chat_message('user'):
        st.write(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = store.text_classification(prompt)

    with st.chat_message('assistant'):
        st.write(f'{response}')
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    