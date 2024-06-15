import tkinter as tk
from tkinter import ttk

class TabbedView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.notebook = ttk.Notebook()
        self.tab1 = ttk.Frame(ttk.Notebook())
        self.tab2 = ttk.Frame(ttk.Notebook())

        self.pack(expand=1, fill="both")
        ttk.Label(self.tab1,  
          text ="Welcome to GeeksForGeeks").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   
        ttk.Label(self.tab2, 
          text ="Lets dive into theworld of computers").grid(column = 0, 
                                    row = 0,  
                                    padx = 30, 
                                    pady = 30) 

    def add_tab(self, webpage):
        # Implement adding a new tab with a webpage
        
        pass
        