import tkinter as tk
from menu import MenuBar
from tabbed_view import TabbedView
from views.loginview import LoginView
from views.new_project_view import ProjectView
from views.new_script_view import ScriptView
from views.new_element_view import ElementView
from views.new_page_view import PageView

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Auto-Spydy")
        
        # Initialize the menu bar
        self.menu_bar = MenuBar(self)

        # Add the menu bar to the application
        self.config(menu=self.menu_bar)
        
        # self.loginview=LoginView()

        self.projectview=ProjectView()
        self.projectview=ScriptView()
        self.pageview=PageView()
        self.elementview=ElementView()

        # Create the tabbed view
        # self.tabbed_view = TabbedView()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()