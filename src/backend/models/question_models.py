from typing import Optional
from pydantic import BaseModel

class Question(BaseModel):
     question_number: int
     question_type: str
     question_content: str
     question_answer_choices: Optional[list[str]] = None
     
class QuestionChunk(BaseModel):
     school_of_paper: str
     topic_of_paper: str
     year_of_paper: int
     grade_of_paper: int
     question_number: int
     question_type: str
     question_content: str
     question_answer_choices: Optional[list[str]] = None