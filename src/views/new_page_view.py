import tkinter as tk
from tkinter import ttk

class PageView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        self.page_name_label=ttk.Label(master,text="Page Name:")
        self.page_name=ttk.Entry(master)
        self.pageURL_label=ttk.Label(master,text="Page URL:")
        self.pageURL=tk.Text(master,height=5)
        self.pageAdd_btn=ttk.Button(master,text="Add Page")

        self.page_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.page_name.grid(row=1,column=1,padx=10,pady=10)
        self.pageURL_label.grid(row=2,column=0,padx=10,pady=10)
        self.pageURL.grid(row=2,column=1,padx=10,pady=10)
        self.pageAdd_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
