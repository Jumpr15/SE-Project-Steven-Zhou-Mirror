from models.document_model import QuestionDocument
from models.question_models import Question, QuestionChunk

class document_chunker:

     def chunk_question_document(
          self, 
          question_document: QuestionDocument
     ) -> list[QuestionChunk]:
          
          chunked_question_list = []
          
          for question in question_document.question_list:
               props = {
                    **question_document.model_dump(exclude={'question_list'}), 
                    **question.model_dump()
               }
               
               question_chunk = QuestionChunk(**props)
               chunked_question_list.append(question_chunk)
          
          return chunked_question_list