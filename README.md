# LLM_experiments
* This repository contains several experiments with LLM models. - WIP

# RAG-based LLM application LLM 
* RAG: using LangChain to parse documents and create embeddings using HuggingFaceEmbeddings 
* Results stored in a local vector database using Chroma vector store.
* LLM - Option 1: Using API from OpenAI and Anyscale
* LLM - Option 2: Using local deployment of GPT4All or LlamaCpp

# Comparing models using ELO rating
* Ask any question to two models and vote for the better one.
* Votes recorded to build up Elo-rating of the models.
* Comparison includes models that don't have access to the documents, to identify benefit created by RAG application.

# Credits:
* [https://github.com/ray-project/llm-applications](https://github.com/ray-project/llm-applications)
* [https://github.com/imartinez/privateGPT](https://github.com/imartinez/privateGPT/tree/primordial)
* https://arena.lmsys.org/
* Please check corresponding Licenses before using any code deployed here.
