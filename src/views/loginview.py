import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class LoginView(ctk.CTkFrame):
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.username=ctk.CTkEntry()
        self.password=ctk.CTkEntry()
        self.loginbtn=ctk.CTkButton(text="Login")
        self.username.pack()
        self.password.pack()
        self.loginbtn.pack()

    
