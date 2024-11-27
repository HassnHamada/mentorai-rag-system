# Mentor.AI recommendation system

This is a recommendation system for Mentor.AI. Using Cohere's embeddings and Weaviate as a vector database to create a RAG to respond to user queries.

## Technologies
- Cohere
- Weaviate
- Docker

## Files
- [vectorDB.py](./src/vectorDB.py) is an abstraction to control weaviate database.
- [main.ipynb](./main.ipynb) is the main file to clean the data and create the embeddings.
- [data_cleaning.ipynb](./data_cleaning.ipynb) used to process JSON data.
- [docker-compose.yml](./docker-compose.yml) is used to start a local  instance of Weaviate.