from dotenv import load_dotenv
import os
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes as wvc
import weaviate.classes.config as wc
from weaviate.classes.config import Property, DataType
import requests
import json

load_dotenv()

weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")

def load_text(fname):
     with open(fname, "r") as file:
          text = file.read()
          return text

def connect_to_db():
     try:
          client = weaviate.connect_to_weaviate_cloud(
               cluster_url=weaviate_url,
               auth_credentials=Auth.api_key(weaviate_api_key)
          )

          print(client.is_ready())
          return client

     except Exception as e:
          print(e) 

     finally:
          client.close()

# deletes and reinstantiates new collection
def create_collection(client, collection_name):
     try:
          collection = client.collections.create(
               name=collection_name, 
          )
          return collection
     
     except Exception as e:
          print(e)

def chunk_text(text, chunk_size):
     chunked_list = []
     text_len = len(text)

     for i in range(0, text_len, chunk_size):
          chunked_list.append(text[i:i+chunk_size])
     
     return chunked_list[1:5]


def insert_document(client, collection_name, document):
     try:
          collection = client.collections.use(collection_name)
          res = collection.data.insert({"content":document})
          return res
     
     except Exception as e:
          print(e)

def insert_many_documents(client, collection_name, documents):
     try:
          documents = [{"content":documents[i]} for i in range(len(documents))]
          print(documents)

          collection = client.collections.use(collection_name)
          res = collection.data.insert_many(documents)
          return res

     except Exception as e:
          print(e)

def retrieve_document(client, collection_name, document_id):
     try:
          collection = client.collections.use(collection_name)
          data_object = collection.query.fetch_object_by_id(
               document_id
          )
          return data_object
     
     except Exception as e:
          print(e)

client = connect_to_db()
# col = create_collection(client, "test_collection_2")

# text = load_text("example_text.txt")
# c = chunk_text(text, 50)
# # print(insert_document(client, "test_collection_2", c))
# insert_many_documents(client, "test_collection_2", c)

# print(retrieve_document(client, "test_collection_2", "28718b25-2382-4b86-a3de-7eed5319c082").properties)

# client.close()
