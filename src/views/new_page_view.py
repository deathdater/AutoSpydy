import tkinter as tk
from tkinter import ttk

class PageView(tk.Frame):
    def __init__(self):
        super().__init__()
        self.page_name_label=ttk.Label(text="Page Name:")
        self.page_name=ttk.Entry()
        self.pageURL_label=ttk.Label(text="Page URL:")
        self.pageURL=tk.Text(height=3)
        self.pageAdd_btn=ttk.Button(text="Add Page")

        self.page_name_label.pack()
        self.page_name.pack()
        self.pageURL_label.pack()
        self.pageURL.pack()
        self.pageAdd_btn.pack()
