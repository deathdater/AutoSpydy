import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from models.projectModel import Project
from models.scriptModel import Script
import models.dbSession as db


class ScriptView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)

        self.scriptnameVar=tk.StringVar()
        self.scriptobjectiveVar=tk.StringVar()
        self.projVar=tk.IntVar()

        self.projlist_label=ctk.CTkLabel(master,text="Select Project:")
        self.projects=Project.getProjects()
        self.projlist=ctk.CTkComboBox(master,state="readonly",values=self.projects)



        self.newscript_label=ctk.CTkLabel(master,text="New Script Name")
        self.scriptname=ctk.CTkEntry(master,textvariable=self.scriptnameVar)
        self.newscriptobjective_label=ctk.CTkLabel(master,text="Script Objective")
        self.scriptobjective=ctk.CTkEntry(master,textvariable=self.scriptobjectiveVar)
        self.addscript_btn=ctk.CTkButton(master,text="Add Script",command=self.pressAddScript)
        self.viewscript_btn=ctk.CTkButton(master,text="View Script")


        self.projlist_label.grid(row=0,column=0,padx=10,pady=10)
        self.projlist.grid(row=0,column=1,padx=10,pady=10)

        self.newscript_label.grid(row=1,column=0,padx=10,pady=10)
        self.scriptname.grid(row=1,column=1,padx=10,pady=10)
        self.newscriptobjective_label.grid(row=2,column=0,padx=10,pady=10)
        self.scriptobjective.grid(row=2,column=1,padx=10,pady=10)
        self.addscript_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
        self.viewscript_btn.grid(row=3,column=2,columnspan=1,padx=10,pady=10)


    def pressAddScript(self):
        self.projdbname=self.projlist.get()
        self.session,self.engine=db.createSession(self.projdbname)
        self.projectid=self.session.query(Project.project_id).filter(Project.projectname==self.projlist.get().removesuffix(".db"))
        # print("abcddasd : {0}",self.projectid)
        script=Script(self.projectid,self.scriptname.get(),self.scriptobjective.get())
        script.createScript(self.projdbname)
    

    
