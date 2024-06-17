from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.projectModel import Project
import  models.dbSession as db
Base =declarative_base()
class Script(Base):
    __tablename__="scripts"

    project_id =Column("project_id", ForeignKey(Project.project_id), nullable=False)
    script_id=Column("script_id",Integer,primary_key=True,autoincrement="auto",unique=True)
    scriptname=Column("scriptname",String)
    scriptobjective=Column("scriptobjective",String)

    def __init__(self,project ,name,objective):
        self.project_id=project
        self.scriptname=name
        self.scriptobjective=objective
        

    def __repr__(self):
        return f"({self.script_id}) : ({self.scriptname})"
    
    def createScript(self,dbname):
        session,engine=db.createSession(dbname)
        Base.metadata.create_all(bind=engine)
        session.add(Script(self.project_id,self.scriptname,self.scriptobjective))
        session.commit()
        print (f"{self.scriptname} Added To DB")