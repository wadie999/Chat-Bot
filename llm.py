import os
import sys
import keys 
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

class TextSearch:
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.index = None

    def load_document(self):
        loader = TextLoader(self.filename, self.encoding)
        self.index = VectorstoreIndexCreator().from_loaders([loader])

    def search(self, query):
        if self.index is None:
            raise ValueError("The document is not Loaded")

        return self.index.query(query)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = keys.key

    query = sys.argv[1]
    print(query)

    text_search = TextSearch('1_transcript.txt', encoding='utf-8')
    text_search.load_document()
    results = text_search.search(query)
    print(results)