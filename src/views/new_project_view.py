import tkinter as tk
from tkinter import ttk


class ProjectView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.user_input=tk.StringVar()

        self.newproject_label=ttk.Label(master,text="Project Name")
        self.projectname=ttk.Entry(master,textvariable=self.user_input)
        self.newprojectdesc_label=ttk.Label(master,text="Project Description")
        self.projectdesc=tk.Text(master,height=5)
        self.addproject_btn=ttk.Button(master,text="Add Project",command=self.pressAddBtn)
        self.viewproject_btn=ttk.Button(master,text="View Project",command=self.pressViewBtn)

        self.newproject_label.grid(row=1,column=0,padx=10,pady=10)
        self.projectname.grid(row=1,column=1,padx=10,pady=10)
        self.newprojectdesc_label.grid(row=2,column=0,padx=10,pady=10)
        self.projectdesc.grid(row=2,column=1,padx=10,pady=10)
        self.addproject_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
        self.viewproject_btn.grid(row=3,column=2,columnspan=1,padx=10,pady=10)
    def pressAddBtn(self):
        print(f"Added Project: {self.user_input.get()}")
    def pressViewBtn(self):
        print(f"View Projects: {self.user_input.get()}")

    
