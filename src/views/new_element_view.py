import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from models.projectModel import Project
from models.pageModel import Page
from models.elementModel import Element
import models.dbSession as db

class ElementView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)

        self.elementnameVar=tk.StringVar()
        self.elementLocatorVar=tk.StringVar()
        self.projVar=tk.IntVar()
        self.pageVar=tk.IntVar()


        self.projlist_label=ctk.CTkLabel(master,text="Select Project:")
        
        self.projects=Project.getProjects()
        self.projlist=ctk.CTkComboBox(master,state="readonly",values=self.projects)
        self.projdbname=self.projlist.get().removesuffix(".db")
        
        self.pagelist_label=ctk.CTkLabel(master,text="Select Page:")
        print(self.projdbname)
        self.pages=""
        if(self.projdbname!=""):
            self.pages=Page.getPages(self.projdbname)
        self.pagelist=ctk.CTkComboBox(master,state="readonly",values=self.pages)



        self.element_name_label=ctk.CTkLabel(master,text="Element Name:")
        self.element_name=ctk.CTkEntry(master,textvariable=self.elementnameVar)
        self.locatortype_label=ctk.CTkLabel(master,text="Locator Type:")
        self.locatortype=ctk.CTkComboBox(master,values=("XPATH","ID","CSS"))
        self.locatorVal_label=ctk.CTkLabel(master,text="Locator Value:")
        self.locatorVal=ctk.CTkEntry(master,textvariable=self.elementLocatorVar)
        self.locatorAdd_btn=ctk.CTkButton(master,text="Add Locator",command=self.pressAddElement)


        self.projlist_label.grid(row=0,column=0,padx=10,pady=10)
        self.projlist.grid(row=0,column=1,padx=10,pady=10)

        self.pagelist_label.grid(row=0,column=2,padx=10,pady=10)
        self.pagelist.grid(row=0,column=3,padx=10,pady=10)

        self.element_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.element_name.grid(row=1,column=1,padx=10,pady=10)
        self.locatortype_label.grid(row=2,column=0,padx=10,pady=10)
        self.locatortype.grid(row=2,column=1,padx=10,pady=10)
        self.locatorVal_label.grid(row=3,column=0,padx=10,pady=10)
        self.locatorVal.grid(row=3,column=1,padx=10,pady=10)
        self.locatorAdd_btn.grid(row=4,column=1,columnspan=2,padx=10,pady=10)

    def pressAddElement(self):
        self.projdbname=self.projlist.get()
        self.session,self.engine=db.createSession(self.projdbname)
        self.projectid=self.session.query(Project.project_id).filter(Project.projectname==self.projlist.get().removesuffix(".db"))
        self.pageid=1 #self.session.query(Page.page_id).filter(Page.pagename==self.pagelist.get())  #FIX This
        
        # print("abcddasd : {0}",self.projectid)
        element=Element(self.projectid,self.pageid,self.element_name.get(),self.locatortype.get(),self.locatorVal.get())
        element.createElement(self.projdbname,self.pageid)