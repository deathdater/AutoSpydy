import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from models.projectModel import Project

class ProjectView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.projectnameVar=tk.StringVar()
        self.projectDescVar=tk.StringVar()

        self.newproject_label=ctk.CTkLabel(master,text="Project Name")
        self.projectname=ctk.CTkEntry(master,textvariable=self.projectnameVar)
        self.newprojectdesc_label=ctk.CTkLabel(master,text="Project Description")
        self.projectdesc=ctk.CTkEntry(master,textvariable=self.projectDescVar)
        self.addproject_btn=ctk.CTkButton(master,text="Add Project",command=self.pressAddBtn)
        self.viewproject_btn=ctk.CTkButton(master,text="View Project",command=self.pressViewBtn)

        self.newproject_label.grid(row=1,column=0,padx=10,pady=10)
        self.projectname.grid(row=1,column=1,padx=10,pady=10)
        self.newprojectdesc_label.grid(row=2,column=0,padx=10,pady=10)
        self.projectdesc.grid(row=2,column=1,padx=10,pady=10)
        self.addproject_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
        self.viewproject_btn.grid(row=3,column=2,columnspan=1,padx=10,pady=10)
    def pressAddBtn(self):
        project=Project(self.projectname.get(),self.projectdesc.get())
        project.createProject()

        
    def pressViewBtn(self):
        print(f"View Projects: {self.user_input.get()}")

    
