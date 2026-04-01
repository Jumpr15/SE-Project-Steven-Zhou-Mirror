from pydantic import BaseModel

from models.question_models import Question

class QuestionDocument(BaseModel):
     school_of_paper: str
     topic_of_paper: str
     year_of_paper: int
     grade_of_paper: int
     question_list: list[Question]