import tkinter as tk
from tkinter import ttk


class ScriptView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.newscript_label=ttk.Label(master,text="New Script Name")
        self.scriptname=ttk.Entry(master)
        self.newscriptobjective_label=ttk.Label(master,text="Script Objective")
        self.scriptobjective=tk.Text(master,height=5)
        self.addscript_btn=ttk.Button(master,text="Add Script")
        self.viewscript_btn=ttk.Button(master,text="View Script")

        self.newscript_label.grid(row=1,column=0,padx=10,pady=10)
        self.scriptname.grid(row=1,column=1,padx=10,pady=10)
        self.newscriptobjective_label.grid(row=2,column=0,padx=10,pady=10)
        self.scriptobjective.grid(row=2,column=1,padx=10,pady=10)
        self.addscript_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
        self.viewscript_btn.grid(row=3,column=2,columnspan=1,padx=10,pady=10)

    
