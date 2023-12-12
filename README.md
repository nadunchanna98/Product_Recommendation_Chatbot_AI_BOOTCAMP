# Product Recommendation Chatbot AI BOOTCAMP




https://github.com/nadunchanna98/Product_Recommendation_Chatbot_AI_BOOTCAMP/assets/108536998/56898a3c-3763-4e62-ab87-ee3017845418






## Overview

This project implements a chatbot using the LLAMA Index library, specifically the PaLM2 model, to retrieve responses based on user queries and PDF documents. It utilizes Hugging Face embeddings for document and query representation, indexing, and a vector store for efficient retrieval.

![image](https://github.com/nadunchanna98/Product_Recommendation_Chatbot_AI_BOOTCAMP/assets/108536998/ff755119-f25a-492b-837e-8af9f5128667)


## Features

- User queries are processed through Hugging Face embeddings.
- Company or Detail Documents are embedded and indexed for efficient retrieval.
- PaLM2 LLM is used for generating responses based on user queries.
- Streamlit Interface
- transformers - Usage in transformers by Hugging Face is a library for working with pre-trained models (NLP). In here, it used for working with Hugging Face embeddings.
- torch - PyTorch, a popular open-source machine learning library. It provides tools for building and training deep neural networks.


1. Clone the repository:

```bash
git clone https://github.com/nadunchanna98/Product_Recommendation_Chatbot_AI_BOOTCAMP.git
```

2. Installation

```bash
pip install llama_index
pip install streamlit
pip install torch
pip install transformers
pip install google-generativeai
pip install pypdf
```

3. Navigate to the project directory and run the Streamlit app:

```bash
cd Product_Recommendation_Chatbot_AI_BOOTCAMP
streamlit run app.py
```

