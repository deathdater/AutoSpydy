import tkinter as tk
from tkinter import ttk

class ElementView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.element_name_label=ttk.Label(master,text="Element Name:")
        self.element_name=ttk.Entry(master,)
        self.locatortype_label=ttk.Label(master,text="Locator Type:")
        self.locatortype=ttk.Combobox(master,values=("XPATH","ID","CSS"))
        self.locatorVal_label=ttk.Label(master,text="Locator Value:")
        self.locatorVal=tk.Text(master,height=5)
        self.locatorAdd_btn=ttk.Button(master,text="Add Locator")

        self.element_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.element_name.grid(row=1,column=1,padx=10,pady=10)
        self.locatortype_label.grid(row=2,column=0,padx=10,pady=10)
        self.locatortype.grid(row=2,column=1,padx=10,pady=10)
        self.locatorVal_label.grid(row=3,column=0,padx=10,pady=10)
        self.locatorVal.grid(row=3,column=1,padx=10,pady=10)
        self.locatorAdd_btn.grid(row=4,column=1,columnspan=2,padx=10,pady=10)