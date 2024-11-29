# Mentor.AI recommendation system

This is a recommendation system for Mentor.AI. Using Cohere's embeddings and Weaviate as a vector database to create a RAG to respond to user queries.

## Technologies
- Cohere
- Weaviate
- Docker

## Files
- [vectorDB.py](./src/vectorDB.py) is an abstraction to control weaviate database.
- [main.ipynb](./main.ipynb) is the main file to clean the data and create the embeddings.
- [data_cleaning.ipynb](./data_cleaning.ipynb) used to process JSON data and save it to a CSV file.
- [docker-compose.yml](./docker-compose.yml) is used to start a local  instance of Weaviate.

## How to use
1. Clone the repository
2. Run `docker-compose up` to start the local instance of Weaviate.
3. Create a `.env` file with the following variables:
    - `COHERE_KEY`: Your Cohere API key.
4. Run the appropriate cells in the `main.ipynb` file to create the embeddings or genrate a response.