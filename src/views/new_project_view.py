import tkinter as tk
from tkinter import ttk


class ProjectView(ttk.Frame):
    def __init__(self, *args,**kwargs):
        super().__init__()

        self.newproject_label=ttk.Label(text="New Project Name")
        self.projectname=ttk.Entry()
        self.newprojectdesc_label=ttk.Label(text="Project Description")
        self.projectdesc=tk.Text(height=5)
        self.addproject_btn=ttk.Button(text="Add Project")
        self.viewproject_btn=ttk.Button(text="View Project")

        self.newproject_label.pack()
        self.projectname.pack()
        self.newprojectdesc_label.pack()
        self.projectdesc.pack()
        self.addproject_btn.pack()
        self.viewproject_btn.pack()

    
