# Weird Fungi RAG

A local PDF chatbot focused English-Chinese Q&A.This application uses the concept of Retrieval-Augmented Generation (RAG) to generate responses in the context of a particular document. RAG applications augment their generation capabilities by retrieving relevant information from an external knowledge base. This allows RAG applications to produce more informative and comprehensive responses to a wider range of prompts and questions.
### For detailed explaination of how this works follow my [Medium Artcle](https://medium.com/@harjot802/building-a-local-pdf-chat-application-with-mistral-7b-llm-langchain-ollama-and-streamlit-67b314fbab57)
## Running Mistral 7B Locally using Ollama 🦙

Ollama allows you to run open-source large language models, such as Llama 3, locally. It bundles model weights, configuration, and data into a single package, defined by a Modelfile, optimizing setup and configuration details, including GPU usage.

**For Mac and Linux Users:**
Ollama effortlessly integrates with Mac and Linux systems, offering a user-friendly installation process. Mac and Linux users can swiftly set up Ollama to access its rich features for local language model usage. Detailed instructions can be found here: [Ollama GitHub Repository for Mac and Linux](https://github.com/ollama/ollama).

# Usage

1. Clone this repository:
   
 ```
 git clone 
 ```
2. Install all the depenedencies :
   
```
pip install -r requirements.txt
```
3. Open terminal and run the following command:
```
streamlit run app.py
```