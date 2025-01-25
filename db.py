from datetime import datetime #for graph and logs
import pytz
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base() # base class for ORM models

engine = create_engine('sqlite:///logs.db') # will be created when you run db.py and store all logs 

Session = scoped_session(sessionmaker(bind=engine))

IST = pytz.timezone("Asia/Kolkata")  # Replace with your timezone

#representing the logs table
class LogEntry(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    toxicity_score = Column(Float, nullable=False)
    emotion_label = Column(String, nullable=False)  # Add label column
    emotion_score = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(IST)) 

#create the tables based on models
Base.metadata.create_all(engine)
