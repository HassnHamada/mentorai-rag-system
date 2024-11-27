import time
import weaviate
import weaviate.classes as wvc
import weaviate.client as WeaviateClient
from weaviate.classes.config import Configure
from dotenv import find_dotenv, load_dotenv
import os
from typing import List, Dict, Set, AnyStr


class VectorDB:
    def __init__(self):
        load_dotenv(find_dotenv())
        # wcd_url = os.getenv("WCD_URL")
        # wcd_api_key = os.getenv("WCD_API_KEY")
        cohere_key = os.getenv("COHERE_KEY")
        print("Connecting to Weaviate")
        # self.client = weaviate.connect_to_local()
        self.client = weaviate.connect_to_local(
            # skip_init_checks=True,
            headers={"X-Cohere-Api-Key": cohere_key}
        )
        # self.client = weaviate.connect_to_wcs(
        #     cluster_url=wcd_url,
        #     auth_credentials=wvc.init.Auth.api_key(wcd_api_key),
        #     headers={"X-Cohere-Api-Key": cohere_key}
        # )

    def create_collection(self, collection_name, **config):
        if not self.client.collections.exists(collection_name):
            print("Creating collection")
            self.client.collections.create(
                collection_name,
                **config,
            )
        else:
            print("Collection already exists")

    def insert_data(self, collection_name, data: Dict[AnyStr, Dict[AnyStr, AnyStr]], key_field="custom_id"):
        collection = self.client.collections.get(collection_name)
        with collection.batch.dynamic() as batch:
            for k, src_obj in data.items():
                weaviate_obj = src_obj | {key_field: k}
                batch.add_object(
                    properties=weaviate_obj,
                )
                # time.sleep(1)  # Sleep for 1 second to avoid rate limit

        if len(collection.batch.failed_objects):
            print(collection.batch.failed_objects)
            raise Exception("Failed to insert data")

    def search_data(self, collection_name, query: str, limit: int = 10):
        collection = self.client.collections.get(collection_name)
        results = collection.query.near_text(query=query, limit=limit)
        return results

    def get_by_uuid(self, collection_name, uuid):
        collection = self.client.collections.get(collection_name)
        return collection.query.fetch_object_by_id(uuid)

    def delete_collection(self, collection_name):
        self.client.collections.delete(collection_name)

    def delete_all(self):
        self.client.collections.delete_all()

    def close(self):
        self.client.close()
