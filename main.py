import time

import requests
from fastapi import FastAPI, Depends
from sqlalchemy.exc import OperationalError

from database import Session, BaseModel, engine, Question

app = FastAPI()

# ожидание готовности БД
while True:
    try:
        conn = engine.connect()
        conn.close()
        break
    except OperationalError:
        time.sleep(1)

BaseModel.metadata.create_all(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post('/quiz')
def quiz(questions_num: int, db=Depends(get_db)):
    questions_count = 0
    while questions_count < questions_num:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num - questions_count}")
        if response.status_code == 200:
            for item in response.json():
                if not db.query(Question).filter_by(id=item['id']).first():
                    questions_count += 1
                    new_question = Question(
                        id=item['id'],
                        question_text=item['question'],
                        answer_text=item['answer'],
                        created_at=item['created_at'],
                        category=item['category']['title'],
                    )
                    db.add(new_question)
                    db.commit()
    last_question = db.query(Question).order_by(Question.recorded_to_db_at.desc()).first()
    if last_question:
        return last_question
    else:
        return {}
