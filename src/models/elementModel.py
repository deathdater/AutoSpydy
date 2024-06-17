from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.pageModel import Page
from models.projectModel import Project
import  models.dbSession as db
Base =declarative_base()
class Element(Base):
    __tablename__="elements"

    project_id =Column("project_id", ForeignKey(Project.project_id), nullable=False)
    page_id=Column("page_id",Integer,ForeignKey(Page.page_id), nullable=False)
    element_id=Column("element_id",Integer,primary_key=True,autoincrement="auto",unique=True)
    elementname=Column("elementname",String,nullable=False)
    elementlocatortype=Column("elementlocatortype",String,nullable=False)
    elementlocatorvalue=Column("elementlocatorvalue",String,nullable=False)

    def __init__(self,project,page,name,locatortype,value):
        self.project_id=project
        self.page_id=page
        self.elementname=name
        self.elementlocatortype=locatortype
        self.elementlocatorvalue=value
        

    def __repr__(self):
        return f"({self.element_id}) : ({self.elementname})"
    
    def createElement(self,dbname,page):
        session,engine=db.createSession(dbname)
        Base.metadata.create_all(bind=engine)
        session.add(Element(self.project_id,page,self.elementname,self.elementlocatortype,self.elementlocatorvalue))
        session.commit()
        print (f"{self.elementname} Added To DB")