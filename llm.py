import os
import sys
import keys 
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = keys.key

query = sys.argv[1]
print(query)

loader = TextLoader('minidata.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))