import tkinter as tk
from tkinter import ttk


class LoginView(ttk.Frame):
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.username=ttk.Entry()
        self.password=ttk.Entry()
        self.loginbtn=ttk.Button(text="Login")
        self.username.pack()
        self.password.pack()
        self.loginbtn.pack()

    
