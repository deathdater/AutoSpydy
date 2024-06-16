import tkinter as tk
from tkinter import ttk
from models.projectModel import Project
from models.pageModel import Page

class PageView(tk.Frame):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master)
        
        self.pagenameVar=tk.StringVar()
        self.pageurlVar=tk.StringVar()
        self.projVar=tk.IntVar()
        # print(Project.getProjects())

        self.projlist_label=ttk.Label(master,text="Select Project:")
        self.projects, self.session=Project.getProjects()  # JUGAAD to be corrected later

        self.projlist=ttk.Combobox(master,state="readonly",values=self.projects)
        self.page_name_label=ttk.Label(master,text="Page Name:")
        self.page_name=ttk.Entry(master,textvariable=self.pagenameVar)
        self.pageURL_label=ttk.Label(master,text="Page URL:")
        self.pageURL=tk.Entry(master,textvariable=self.pageurlVar)
        self.pageAdd_btn=ttk.Button(master,text="Add Page",command=self.createPage)


        self.projlist_label.grid(row=0,column=0,padx=10,pady=10)
        self.projlist.grid(row=0,column=1,padx=10,pady=10)

        self.page_name_label.grid(row=1,column=0,padx=10,pady=10)
        self.page_name.grid(row=1,column=1,padx=10,pady=10)
        self.pageURL_label.grid(row=2,column=0,padx=10,pady=10)
        self.pageURL.grid(row=2,column=1,padx=10,pady=10)
        self.pageAdd_btn.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
    
    def createPage(self):
        self.session.add(Page(int(self.projects[0]),self.page_name.get(),self.pageURL.get()))
        self.session.commit()
        print("Page Created")