from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from datetime import datetime


app = FastAPI()

load_dotenv()

# PostgreSQL 연결 정보
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")

# SQLAlchemy 설정
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 데이터베이스 모델 정의
class Sample(Base):
    __tablename__ = "sample"
    user_id = Column(Integer, primary_key=True)
    utterance = Column(Text, nullable=False)
    created_on = Column(DateTime, primary_key=True)

class KakaoRequest(BaseModel):
    userRequest: dict
    intent: dict
    action: dict
    bot: dict
    contexts: list
    action: dict

# 데이터베이스 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/res_test")
def handle_bot_request(request: KakaoRequest):
    userRequest = request.userRequest
    print('=======================\n')
    print(userRequest['utterance'])
    print('\n=======================\n')

    return request

@app.post("/db_test")
async def handle_db(request: KakaoRequest, db = Depends(get_db)):    
    data = request
    user_request = data.userRequest

    db_sample = Sample(user_id=user_request['user']['properties']['appUserId'], utterance=user_request['utterance'], created_on=datetime.now())
    db.add(db_sample)
    db.commit()
    db.refresh(db_sample)

    print(f"저장된 데이터: {data}")  # 콘솔 출력
    return data

@app.get("/")
async def root():
    return {"message": "Hello World"}