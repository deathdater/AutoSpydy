from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
Base = declarative_base()

class Project(Base):
    __tablename__="projects"

    project_id=Column("projectid",Integer,primary_key=True,autoincrement="auto",unique=True)
    projectname=Column("projectname",String)
    projectdesc=Column("projectdesc",String)
    projectdb_string=Column("dbstr",String)

    def __init__(self,name,desc):
        self.projectname=name
        self.projectdesc=desc

        

    def __repr__(self):
        return f"({self.project_id}_{self.projectname})"
    
    def createProject(self):
        self.engine=create_engine(f"sqlite:///data/projectdb/{self.projectname}.db",echo=True)
        super().metadata.create_all(bind=self.engine)
        self.Session=sessionmaker(bind=self.engine)
        session=self.Session()
        self.projdb=f"sqlite:///data/projectdb/{self.projectname}.db"
        session.add(Project(self.projectname,self.projectdesc))
        session.commit()
        print (f"{self.projectname} Added To DB")
        results=session.query(Project).filter(Project.projectname==self.projectname).update({Project.projectdb_string:self.projdb})
        session.commit()
        print (f"{self.projectname} DB String Updated")
    
    def getProjects():
        path="AutoSpydy//src//data//projectdb//"
        files=os.listdir("data/projectdb/")
        return files





