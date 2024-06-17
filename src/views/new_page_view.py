import tkinter as tk
from tkinter import ttk
from models.projectModel import Project
from models.pageModel import Page
import models.dbSession as db


class PageView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        
        self.pagenameVar=tk.StringVar()
        self.pageurlVar=tk.StringVar()
        self.projVar=tk.IntVar()
        # print(Project.getProjects())

        self.projlist_label=ttk.Label(master,text="Select Project:")
        self.projects=Project.getProjects()

        self.projlist=ttk.Combobox(master,state="readonly",values=self.projects)
        self.page_name_label=ttk.Label(master,text="Page Name:")
        self.page_name=ttk.Entry(master,textvariable=self.pagenameVar)
        self.pageURL_label=ttk.Label(master,text="Page URL:")
        self.pageURL=tk.Entry(master,textvariable=self.pageurlVar)
        self.pageAdd_btn=ttk.Button(master,text="Add Page",command=self.pressAddPage)


        self.projlist_label.grid(row=0,column=0,padx=10,pady=10)
        self.projlist.grid(row=0,column=1,padx=10,pady=10)

        self.page_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.page_name.grid(row=1,column=1,padx=10,pady=10)
        self.pageURL_label.grid(row=2,column=0,padx=10,pady=10)
        self.pageURL.grid(row=2,column=1,padx=10,pady=10)
        self.pageAdd_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
    
    def pressAddPage(self):
        self.projdbname=self.projlist.get()
        self.session,self.engine=db.createSession(self.projdbname)
        self.projectid=self.session.query(Project.project_id).filter(Project.projectname==self.projlist.get().removesuffix(".db"))
        print("abcddasd : {0}",self.projectid)
        page=Page(self.projectid,self.page_name.get(),self.pageURL.get())
        page.createPage(self.projdbname)
       