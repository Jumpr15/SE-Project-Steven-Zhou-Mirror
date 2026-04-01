from models.user_query_model import UserQuery

from database.vectordb.VectorStore import VectorStore

async def retrievalGeneration(query: UserQuery):
     vector_db = VectorStore()
     collection_name = "test" # manual collection name setting
     
     client = vector_db.connect_to_db()
     collection = vector_db.connect_to_db()
     similar_text = vector_db.similarity_search_by_text(client, collection, query)
     
     # return { "message" : "retrieval generation core function" }
     return { "message" : similar_text }