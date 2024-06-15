import tkinter as tk


class MenuBar(tk.Menu):
    def __init__(self, master, *args, **kwargs):
        tk.Menu.__init__(self, master, *args, **kwargs)

        # Create the file menu
        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label="New Project", command=self.new_project)
        self.file_menu.add_command(label="Open Project", command=self.open_project)
        self.file_menu.add_command(label="Save Project", command=self.save_project)
        self.file_menu.add_command(label="Exit", command=master.quit)

        # Add the file menu to the menu bar
        self.add_cascade(label="File", menu=self.file_menu)



    def new_project(self):
        # Implement creating a new project
        print("New Project")
        pass

    def open_project(self):
        # Implement opening an existing project
        print("Open Project")
        pass

    def save_project(self):
        # Implement saving the current project
        print("Save Project")
        pass