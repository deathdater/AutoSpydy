import tkinter as tk
from tkinter import ttk
from menu import MenuBar
from tabbed_view import TabbedView
from views.loginview import LoginView
from views.new_project_view import ProjectView
from views.new_script_view import ScriptView
from views.new_element_view import ElementView
from views.new_page_view import PageView
from views.new_parameter_view import ParamView


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Auto-Spydy")
        
        # Initialize the menu bar
        self.menu_bar = MenuBar(self)

        # Add the menu bar to the application
        self.config(menu=self.menu_bar)
        
        # self.loginview=LoginView()
        self.projectBtn=ttk.Button(text="Projects",command= self.showProjects)
        self.projectBtn.grid(row=0,column=2,padx=10,pady=10,columnspan=1)
        self.paramsBtn=ttk.Button(text="Parameters",command= self.showParams).grid(row=1,column=2,padx=10,pady=10,columnspan=1)
        self.scriptsBtn=ttk.Button(text="Scripts",command= self.showScripts).grid(row=2,column=2,padx=10,pady=10,columnspan=1)
        self.pagesBtn=ttk.Button(text="Pages",command= self.showPages).grid(row=3,column=2,padx=10,pady=10,columnspan=1)
        self.elementsBtn=ttk.Button(text="Elements",command= self.showElements).grid(row=4,column=2,padx=10,pady=10,columnspan=1)

        
        

        # Create the tabbed view
        # self.tabbed_view = TabbedView()
    
    def showProjects(self):
        self.projectview=ProjectView(tk.Toplevel())


    def showScripts(self):
        self.scriptview=ScriptView(tk.Toplevel())
        

    def showPages(self):
        self.pageview=PageView(tk.Toplevel())

    def showParams(self):
        self.pageview=ParamView(tk.Toplevel())


    def showElements(self):
        self.elementview=ElementView(tk.Toplevel())


        

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()