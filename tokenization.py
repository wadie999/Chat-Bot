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
    
    def find_last_period(self, tokens, chunkSize=500):
        period_token = self.tt_encoding.encode('.')

        last_period_index = chunkSize - 1 if len(tokens) > chunkSize else len(tokens) - 1
        while last_period_index >= 0:
            if tokens[last_period_index] == '.':
                return last_period_index
            last_period_index -= 1
        return -1

    

if __name__ == "__main__":
    text_tokenizer = TextTokenizer(encoding='cl100k_base')
    file_text = text_tokenizer.read_file('minidata.txt')
    chunks = text_tokenizer.create_chunks(file_text, 500)
    for chunk in chunks:
        print(chunk)
        print("\n" + "="*50 + "\n")
    

