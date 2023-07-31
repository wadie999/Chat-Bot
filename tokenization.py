import openai 
import tiktoken
import os 

class TextTokenizer:
    def __init__(self, encoding):
        self.encoding = encoding
        self.tt_encoding = tiktoken.get_encoding(encoding)
    
    def read_file(self,fname):
        with open(fname, 'r', encoding="utf8") as f:
            file_text = f.read()
        return file_text
    
    def creat_chunks(self, text, chunkSize):
        tokens = self.tt_encoding.encode(file_text)
        total_tokens = len(tokens)

        chunks = []
        for i in range(0,total_tokens,chunkSize):
            chunk = tokens[i:i+chunkSize]
            chunks.append(chunk)
        return chunks


if __name__ == "__main__":
    text_tokenizer = TextTokenizer(encoding='cl100k_base')
    file_text = text_tokenizer.read_file('1_transcript.txt')
    chunks = text_tokenizer.creat_chunks(file_text, 500)

    print(len(chunks))
    print(len(chunks[0]))