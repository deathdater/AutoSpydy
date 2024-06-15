import tkinter as tk
from tkinter import ttk

class ElementView(tk.Frame):
    def __init__(self):
        super().__init__()
        self.element_name_label=ttk.Label(text="Element Name:")
        self.element_name=ttk.Entry()
        self.locatortype_label=ttk.Label(text="Locator Type:")
        self.locatortype=ttk.Combobox(values=("XPATH","ID","CSS"))
        self.locatorVal_label=ttk.Label(text="Locator Value:")
        self.locatorVal=tk.Text(height=3)
        self.locatorAdd_btn=ttk.Button(text="Add Locator")

        self.element_name_label.pack()
        self.element_name.pack()
        self.locatortype_label.pack()
        self.locatortype.pack()
        self.locatorVal_label.pack()
        self.locatorVal.pack()
        self.locatorAdd_btn.pack()