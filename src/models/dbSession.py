from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
Base = declarative_base()

def createSession (dbName):
        engine=create_engine(f"sqlite:///data/projectdb/{dbName}",echo=True)
        Base.metadata.create_all(bind=engine)
        Session=sessionmaker(bind=engine)
        session=Session()
        return session,engine