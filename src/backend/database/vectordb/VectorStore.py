from dotenv import load_dotenv
import os 
import weaviate
import weaviate.classes as wvc
from weaviate.classes.init import Auth
import weaviate.classes.config as wc
from weaviate.classes.config import Property, DataType, Configure
import requests
import json

from models.question_models import QuestionChunk
from models.user_query_model import UserQuery

load_dotenv()

class VectorStore:
     def __init__(
          self
     ):
          self.weaviate_url = os.getenv("WEAVIATE_URL")
          self.weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
     
     def connect_to_db(
          self
     ):
          try:
               client = weaviate.connect_to_weaviate_cloud(
                    cluster_url=self.weaviate_url,
                    auth_credentials=Auth.api_key(self.weaviate_api_key)
               )

               return client

          except Exception as e:
               print(e) 

          # finally:
          #      client.close()
               
               
     def create_collection(
          self, 
          client, 
          collection_name
     ):
          try:
               
               if client.collections.exists(collection_name):
                    return client.collections.get(collection_name)
               
               collection = client.collections.create(
                    name=collection_name, 
                    # vectorize_collection_name=True,
                    # vector_config=Configure.Vectors.text2vec_openai() # manually text vectorizer 
               )
               return collection
          
          except Exception as e:
               print(e)
               
     def insert_chunked_questions(
          self, 
          client, 
          collection_name, 
          documents: list[QuestionChunk]
     ):
          try:
               collection = client.collections.use(collection_name)
               with collection.batch.experimental() as batch:
                    for document in documents:
                         batch.add_object(
                              properties=document.model_dump()
                         )
               
          
          except Exception as e:
               print(e)
               
          finally:
               client.close()

     def similarity_search_by_text(
          self, 
          client,
          collection_name,
          text_query: UserQuery,
          limit = 1
     ):
          try:
               collection = client.collections.use(collection_name)
               response = collection.query.near_text(
                    query=text_query.query_text,
                    limit=limit # semi manual limit set
               )
               
               return response
               
               
          except Exception as e:
               print(e)
               
          finally:
               client.close()