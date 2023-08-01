import os
import sys
import keys 
import tokenization

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


class TextSearch:
    def __init__(self, filename, encoding='cl100k_base'):
        self.filename = filename
        self.encoding = encoding
        self.tokenizer = tokenization.TextTokenizer(encoding)
        self.text = None
        self.chunks = None
        self.index = None

    def load_document(self):
        self.text = self.tokenizer.read_file(self.filename)

    def split_text(self, max_tokens=500):
        self.chunks = self.tokenizer.creat_chunks(self.text, max_tokens)
        
    def store_chunks(self):
        texts = [chunk for chunk in self.chunks]
        self.vectorstore = Chroma.from_texts(texts=texts, embedding=OpenAIEmbeddings())

    def retrieve_n_chunks(self, question, n=3):
        important_chunks = self.vectorstore.similarity_search(question)
        return important_chunks[:n]
    


if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = keys.key

    query = sys.argv[1]
    print(query)

    text_search = TextSearch('1_transcript.txt')
    text_search.load_document()
    text_search.split_text()
    text_search.store_chunks()
    results = text_search.retrieve_n_chunks(query) 
    print(results)