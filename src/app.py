import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from menu import MenuBar
from tabbed_view import TabbedView
from views.loginview import LoginView
from views.new_project_view import ProjectView
from views.new_script_view import ScriptView
from views.new_element_view import ElementView
from views.new_page_view import PageView
from views.new_parameter_view import ParamView


class MainApplication(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title("Auto-Spydy")
        
        # Initialize the menu bar
        self.menu_bar = MenuBar(self)

        # Add the menu bar to the application
        self.config(menu=self.menu_bar)
        
        # self.loginview=LoginView()
        self.projectBtn=ctk.CTkButton(self,text="Projects",command= self.showProjects)
        self.projectBtn.grid(row=0,column=2,padx=10,pady=10,columnspan=1)
        self.paramsBtn=ctk.CTkButton(self,text="Parameters",command= self.showParams).grid(row=1,column=2,padx=10,pady=10,columnspan=1)
        self.scriptsBtn=ctk.CTkButton(self,text="Scripts",command= self.showScripts).grid(row=2,column=2,padx=10,pady=10,columnspan=1)
        self.pagesBtn=ctk.CTkButton(self,text="Pages",command= self.showPages).grid(row=3,column=2,padx=10,pady=10,columnspan=1)
        self.elementsBtn=ctk.CTkButton(self,text="Elements",command= self.showElements).grid(row=4,column=2,padx=10,pady=10,columnspan=1)

        
        

        # Create the tabbed view
        # self.tabbed_view = TabbedView()
    
    def showProjects(self):
        self.win=ctk.CTkToplevel()
        self.win.title("Projects")
        self.projectview=ProjectView(self.win)


    def showScripts(self):
        self.win=ctk.CTkToplevel()
        self.win.title("Scripts")
        self.scriptview=ScriptView(self.win)
        

    def showPages(self):
        self.win=ctk.CTkToplevel()
        self.win.title("Pages")
        self.pageview=PageView(self.win)

    def showParams(self):
        self.win=ctk.CTkToplevel()
        self.win.title("Parameters")
        self.pageview=ParamView(self.win)


    def showElements(self):

        self.win=ctk.CTkToplevel()
        self.win.title("Elements")
        self.elementview=ElementView(self.win)


        

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()