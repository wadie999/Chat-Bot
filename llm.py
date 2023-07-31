import os
import sys

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "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"

query = sys.argv[1]
print(query)

loader = TextLoader('minidata.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))