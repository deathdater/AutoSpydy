import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class ElementView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.element_name_label=ctk.CTkLabel(master,text="Element Name:")
        self.element_name=ctk.CTkEntry(master,)
        self.locatortype_label=ctk.CTkLabel(master,text="Locator Type:")
        self.locatortype=ctk.CTkComboBox(master,values=("XPATH","ID","CSS"))
        self.locatorVal_label=ctk.CTkLabel(master,text="Locator Value:")
        self.locatorVal=ctk.CTkEntry(master,)
        self.locatorAdd_btn=ctk.CTkButton(master,text="Add Locator")

        self.element_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.element_name.grid(row=1,column=1,padx=10,pady=10)
        self.locatortype_label.grid(row=2,column=0,padx=10,pady=10)
        self.locatortype.grid(row=2,column=1,padx=10,pady=10)
        self.locatorVal_label.grid(row=3,column=0,padx=10,pady=10)
        self.locatorVal.grid(row=3,column=1,padx=10,pady=10)
        self.locatorAdd_btn.grid(row=4,column=1,columnspan=2,padx=10,pady=10)