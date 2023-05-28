from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(f"postgres+psycopg2://{settings.DB_USER}:"
                       f"{settings.DB_PASSWORD}@{settings.SERVICE_NAME}/{settings.DB_NAME}")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel = declarative_base()


class Question(BaseModel):
    """
    Данная таблица хранит отдельно дату создания вопроса в сервисе jservice.io
    и отдельно дату его добавления в БД данного сервиса
    """
    __tablename__ = 'questions'
    id: int = Column(Integer, primary_key=True)
    question_text: str = Column(String)
    answer_text: str = Column(String)
    created_at: datetime = Column(DateTime)
    recorded_to_db_at: datetime = Column(DateTime, default=datetime.utcnow)
    category: str = Column(String)
