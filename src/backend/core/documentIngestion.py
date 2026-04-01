from models.document_model import QuestionDocument

from core.documentChunker import document_chunker
from database.vectordb.VectorStore import VectorStore

# only for past paper questions
async def documentIngestion(document: QuestionDocument):
     
     question_chunker = document_chunker()
     chunked_question_list = question_chunker.chunk_question_document(document)
     
     vector_db = VectorStore()
     collection_name = "test" # manual collection name settin
     
     client = vector_db.connect_to_db()
     collection = vector_db.create_collection(client, collection_name)
     res = vector_db.insert_chunked_questions(client, collection_name, chunked_question_list) # temporarily using Test collection
     
     return { "message" : "successfully uploaded documents" }
