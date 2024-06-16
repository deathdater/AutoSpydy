from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.projectModel import Project
Base = declarative_base()

class Page(Base):
    __tablename__="pages"
    project_id =ForeignKey(Project.project_id,)
    page_id=Column("pageid",Integer,primary_key=True,autoincrement="auto",unique=True)
    pagename=Column("pagename",String)
    pageurl=Column("pageurl",String)

    def __init__(self,project ,name,url):
        self.project_id=project
        self.pagename=name
        self.pageurl=url
        

    def __repr__(self):
        return f"({self.page_id}) : ({self.pagename})"
    
    def createPage(self):
        pass