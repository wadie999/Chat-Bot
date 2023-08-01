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
            if tokens[last_period_index] == period_token[0]:
                return last_period_index
            last_period_index -= 1
        return -1

    def create_chunks(self, text, chunkSize):
        tokens = self.tt_encoding.encode(text)
        total_tokens = len(tokens)

        chunks = []
        i = 0           #On decoupe le texte depuis le debut
        while i < total_tokens:
            next_chunk_size = min(chunkSize, total_tokens - i)
            last_period_index = self.find_last_period(tokens[i:i + next_chunk_size])

            if last_period_index != -1:
                chunk_end = i + last_period_index + 1
            else:
                chunk_end = i + next_chunk_size

            chunk = tokens[i:i+chunk_end]
            chunks.append(chunk)
            i = chunk_end
        return chunks


if __name__ == "__main__":
    text_tokenizer = TextTokenizer(encoding='cl100k_base')
    file_text = text_tokenizer.read_file('minidata.txt')
    chunks = text_tokenizer.create_chunks(file_text, 500)

    for chunk in chunks : 
        chunk_text = text_tokenizer.tt_encoding.decode(chunk)
        print(chunk_text)
        print("\n" + "="*50 + "\n")
    
    

