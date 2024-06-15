import tkinter as tk
from tkinter import ttk

class ElementView(tk.Frame):
    def __init__(self):
        super().__init__()
        self.param_name_label=ttk.Label(text="Parameter Name:")
        self.param_name=ttk.Entry()
        self.paramtype_label=ttk.Label(text="Parameter Type:")
        self.paramtype=ttk.Combobox(values=("Global","Project","Page"))
        self.paramVal_label=ttk.Label(text="Parameter Value:")
        self.paramVal=tk.Text(height=3)
        self.paramAdd_btn=ttk.Button(text="Add Parameter")

        self.param_name_label.pack()
        self.param_name.pack()
        self.paramtype_label.pack()
        self.paramtype.pack()
        self.paramVal_label.pack()
        self.paramVal.pack()
        self.paramAdd_btn.pack()