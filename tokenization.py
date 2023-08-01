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
        last_period_index = chunkSize - 1 if len(tokens) > chunkSize else len(tokens) - 1
        while last_period_index >= 0:
            if tokens[last_period_index] == '.':
                return last_period_index
            last_period_index -= 1
        return -1

    def creat_chunks(self, text, chunkSize):
        tokens = self.tt_encoding.encode(text)
        total_tokens = len(tokens)

        chunks = []
        for i in range(0,total_tokens,chunkSize):
            chunk = tokens[i:i+chunkSize]
            chunks.append(chunk)
        return chunks


if __name__ == "__main__":
    text_tokenizer = TextTokenizer(encoding='cl100k_base')
    file_text = text_tokenizer.read_file('minidata.txt')
    
    
    tokens = text_tokenizer.tt_encoding.encode(file_text)
    
    index = text_tokenizer.find_last_period(tokens[:500])
    print("le dernier point est a {index}")

    tokens_as_text = text_tokenizer.tt_encoding.decode(tokens[:500])

    print("les 500 premier tokens") 
    print(tokens_as_text)


    tokens_as_text_lastperiod = text_tokenizer.tt_encoding.decode(tokens[:index+1])
    print("tokens finissent par un point")
    print(tokens_as_text_lastperiod)