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
    
    def count_tokens(self, text):
        tokens = self.tt_encoding.encode(text)
        return len(tokens)
    
    def creat_chunks(self, text, max_tokens):
        chunks = []
        current_chunk = ""
        current_chunk_tokens = 0
        
        sentences = text.split(".")
        for sentence in sentences:
            sentence_tokens = self.count_tokens(sentence)
            
            if current_chunk_tokens + sentence_tokens <= max_tokens:
                current_chunk += sentence + "."
                current_chunk_tokens += sentence_tokens
            else:
                chunks.append((current_chunk, current_chunk_tokens))
                current_chunk = sentence + "."
                current_chunk_tokens = sentence_tokens
        
        if current_chunk:
            chunks.append((current_chunk, current_chunk_tokens))
        
        return chunks

if __name__ == "__main__":
    text_tokenizer = TextTokenizer(encoding='cl100k_base')
    file_text = text_tokenizer.read_file('minidata.txt')
    
    max_tokens_per_chunk = 500
    chunks = text_tokenizer.creat_chunks(file_text, max_tokens_per_chunk)

    concatenated_text = ""
    for idx, (chunk, token_count) in enumerate(chunks):
        print(f"Chunk {idx + 1} ({token_count} tokens):")
        print(chunk)
        print("-------------------")
        concatenated_text += chunk

    print("Original and concatenated texts are the same:", concatenated_text == file_text)