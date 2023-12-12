from llama_index import SimpleDirectoryReader, VectorStoreIndex, Prompt
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms.palm import PaLM
from llama_index import ServiceContext
from llama_index import StorageContext


import os

class RAGPaLMQuery:
    def __init__(self):
        # Create a folder for data if it doesn't exist
        if not os.path.exists("data"):
            os.makedirs("data")

        # Load documents from the data folder
        self.documents = SimpleDirectoryReader("./data").load_data()

        # Set up API key for PaLM
        os.environ['GOOGLE_API_KEY'] = 'AIzaSyD-F6JA2IjqPrKO6otl0qPQVah5OfbF9_o'
        

        # Initialize PaLM and Hugging Face embedding model
        self.llm = PaLM()
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

        # Set up service context
        self.service_context = ServiceContext.from_defaults(llm=self.llm, embed_model=self.embed_model, chunk_size=800, chunk_overlap=20)

        # Create a VectorStoreIndex from the documents
        self.index = VectorStoreIndex.from_documents(self.documents, service_context=self.service_context)

        # Persist the index to storage
        self.index.storage_context.persist()

        # Define a custom prompt with an enhanced table-like format
        template = (
    "+------------------------+-------------------------------------+\n"
     "|     Product Name     |             Description                  |\n"
    "+------------------------+-------------------------------------+\n"
    "|      Attributes        |          Price Range            |\n"
    "+------------------------+-------------------------------------+\n"
    "|     Recommendation  |                                      |\n"
    "+------------------------+-------------------------------------+\n"

            "Please provide your answer starting with 'Doc chat:'. If the answer is not in the given context, reply with 'Sorry.'\n"
        )
        self.qa_template = Prompt(template)
    
        # Create a query engine with the custom prompt template
        self.query_engine = self.index.as_chat_engine(prompt=self.qa_template, response_mode='accumulate')

    def query_response(self, query):
        # Perform a query
        response = self.query_engine.chat(query)
        return response
