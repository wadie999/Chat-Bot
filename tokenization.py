import openai 
import tiktoken
import os 

def read_file_creat_chunks(fname,chunkSize):
    tt_encoding = tiktoken.get_encoding("cl100k_base")
    with open(fname,'r', encoding = "utf8") as f :
        file_text = f.read()

    tokens = tt_encoding.encode(file_text)
    total_tokens = len(tokens)

    chunks = []
    for i in range(0,total_tokens,chunkSize):
        chunk = tokens[i:i+chunkSize]
        chunks.append(chunk)
    return chunks


chunks = read_file_creat_chunks('1_transcript.txt',500)
print(len(chunks))
print(len(chunks[0]))
print(len(chunks[2]))
print(len(chunks[8]))