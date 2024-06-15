import tkinter as tk
from tkinter import ttk


class ScriptView(ttk.Frame):
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.newscript_label=ttk.Label(text="New Script Name")
        self.scriptname=ttk.Entry()
        self.newscriptobjective_label=ttk.Label(text="Script Objective")
        self.scriptobjective=tk.Text(height=5)
        self.addscript_btn=ttk.Button(text="Add Script")
        self.viewscript_btn=ttk.Button(text="View Script")

        self.newscript_label.pack()
        self.scriptname.pack()
        self.newscriptobjective_label.pack()
        self.scriptobjective.pack()
        self.addscript_btn.pack()
        self.viewscript_btn.pack()

    
