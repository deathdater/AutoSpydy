import tkinter as tk
from tkinter import ttk

class ParamView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.param_name_label=ttk.Label(master,text="Parameter Name:")
        self.param_name=ttk.Entry(master,)
        self.paramtype_label=ttk.Label(master,text="Parameter Type:")
        self.paramtype=ttk.Combobox(master,values=("Global","Project","Page"))
        self.paramVal_label=ttk.Label(master,text="Parameter Value:")
        self.paramVal=tk.Text(master,height=3)
        self.paramAdd_btn=ttk.Button(master,text="Add Parameter")

        self.param_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.param_name.grid(row=1,column=1,padx=10,pady=10)
        self.paramtype_label.grid(row=2,column=0,padx=10,pady=10)
        self.paramtype.grid(row=2,column=1
                            ,padx=10,pady=10)
        self.paramVal_label.grid(row=3,column=0,padx=10,pady=10)
        self.paramVal.grid(row=3,column=1,padx=10,pady=10)
        self.paramAdd_btn.grid(row=4,column=1,columnspan=1,padx=10,pady=10)