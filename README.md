
## Introduction

This project provides a custom text search functionality for large text documents, integrating with the LangChain library. 
It aims to provide efficient and relevant text retrieval for specific use cases.

## Installation and Setup

1. Clone the repository
2. Install the required packages: `pip install -r requirements.txt`
3. Place your text file in the desired location

## Usage

The main code is encapsulated in the TextSearch class, which provides methods to load documents, split text, store chunks, and retrieve chunks. A separate function run_query is used to execute a query and print the result.

## Running the Script
Set your OpenAI API key: Make sure to set your OpenAI API key in the environment or modify the code accordingly to include it.

Prepare the Transcript: Place your transcript file in the project directory and name it 1_transcript.txt.

Run the Script: You can run the script from the command line with the desired query as an argument:
python llm.py "Your Query Here"
