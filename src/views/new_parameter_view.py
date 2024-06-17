import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class ParamView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.param_name_label=ctk.CTkLabel(master,text="Parameter Name:")
        self.param_name=ctk.CTkEntry(master,)
        self.paramtype_label=ctk.CTkLabel(master,text="Parameter Type:")
        self.paramtype=ctk.CTkComboBox(master,values=("Global","Project","Page"))
        self.paramVal_label=ctk.CTkLabel(master,text="Parameter Value:")
        self.paramVal=ctk.CTkEntry(master,)
        self.paramAdd_btn=ctk.CTkButton(master,text="Add Parameter")

        self.param_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.param_name.grid(row=1,column=1,padx=10,pady=10)
        self.paramtype_label.grid(row=2,column=0,padx=10,pady=10)
        self.paramtype.grid(row=2,column=1
                            ,padx=10,pady=10)
        self.paramVal_label.grid(row=3,column=0,padx=10,pady=10)
        self.paramVal.grid(row=3,column=1,padx=10,pady=10)
        self.paramAdd_btn.grid(row=4,column=1,columnspan=1,padx=10,pady=10)