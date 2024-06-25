# Weird Fungi RAG

A local RAG chatbot focused on markdown file analysis. This application uses the concept of Retrieval-Augmented Generation (RAG) to generate reliable responses.

## Forked from [PDFCHAT](https://github.com/SonicWarrior1/pdfchat) with a detailed explaination at [Medium Artcle](https://medium.com/@harjot802/building-a-local-pdf-chat-application-with-mistral-7b-llm-langchain-ollama-and-streamlit-67b314fbab57)

## Running llama3:instruct Locally using Ollama 🦙

 ```
 curl -fsSL https://ollama.com/install.sh | sh #download ollama on linux

 ollama run llama3:instruct #pull model

 ollama serve #check if ollama is running or not
 ```
# Usage

1. Clone this repository:
```
git clone 
```
2. Install all the depenedencies
```
sudo pip install -r requirements.txt #some packages require root privelges
```
3. Open terminal and run the following command
```
streamlit run weirdFungi.py
```
