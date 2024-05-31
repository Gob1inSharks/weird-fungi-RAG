from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain_community.llms import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructedMarkdownLoader
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

import streamlit as st

import os
import time

import code.utils as utils

utils.create_directories()
print(utils.delete_all_files())

TITLE = 'Weird Fungi RAG'
MODEL = 'yi:9b'
#yi is a good, English-Chinese Billingual model

if 'template' not in st.session_state:

    st.session_state.template = """You are a knowledgeable chatbot, here to help with questions of the user. Your tone should be professional and informative.

    Context: {context}
    History: {history}

    User: {question}
    Chatbot:"""

if 'prompt' not in st.session_state:

    st.session_state.prompt = PromptTemplate(
        input_variables=["history", "context", "question"],
        template=st.session_state.template,
    )

if 'memory' not in st.session_state:

    st.session_state.memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True,
        input_key="question")

if 'vectorstore' not in st.session_state:

    st.session_state.vectorstore = Chroma(persist_directory='jj',
                                          embedding_function=OllamaEmbeddings(base_url='http://localhost:11434',
                                                                              model=MODEL)
                                          )

if 'llm' not in st.session_state:

    st.session_state.llm = Ollama(base_url="http://localhost:11434",
                                  model=MODEL,
                                  verbose=True,
                                  callback_manager=CallbackManager(
                                      [StreamingStdOutCallbackHandler()]),
                                  )

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title(TITLE)

# Upload a PDF file
uploaded_file = st.file_uploader("Upload your **MARKDOWN** file", type='md')

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

if uploaded_file is not None:

    FILE_NAME = 'files/'+uploaded_file.name

    if not os.path.isfile(FILE_NAME):

        utils.delete_all_files()

        with st.status("reading the document um..."):

            bytes_data = uploaded_file.read()
            f = open(FILE_NAME, "wb")
            f.write(bytes_data)
            f.close()

            loader = UnstructedMarkdownLoader(FILE_NAME,mode='elements')
            data = loader.load()

            # Initialize text splitter
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=200,
                length_function=len
            )
            all_splits = text_splitter.split_documents(data)

            # Create and persist the vector store
            st.session_state.vectorstore = Chroma.from_documents(
                documents=all_splits,
                embedding=OllamaEmbeddings(model=MODEL)
            )
            st.session_state.vectorstore.persist()

    st.session_state.retriever = st.session_state.vectorstore.as_retriever()
    # Initialize the QA chain
    if 'qa_chain' not in st.session_state:
        st.session_state.qa_chain = RetrievalQA.from_chain_type(
            llm=st.session_state.llm,
            chain_type='stuff',
            retriever=st.session_state.retriever,
            verbose=True,
            chain_type_kwargs={
                "verbose": True,
                "prompt": st.session_state.prompt,
                "memory": st.session_state.memory,
            }
        )

    # Chat input and output
    if user_input := st.chat_input("You:", key="user_input"):

        user_message = {"role": "User", "message": user_input}
        st.session_state.chat_history.append(user_message)
        with st.chat_message("User"):
            st.markdown(user_input)

        with st.chat_message("Weird Fungi"):
            with st.spinner("Fungi is typing..."):
                response = st.session_state.qa_chain(user_input)
            message_placeholder = st.empty()
            full_response = response['result']
            message_placeholder.markdown(full_response)

        chatbot_message = {"role": "Weird Fungi", "message": response['result']}
        st.session_state.chat_history.append(chatbot_message)

else:
    st.write("Please upload a PDF file :3")
