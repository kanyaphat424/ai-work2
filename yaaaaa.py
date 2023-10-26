from tkinter import *
from tkinter import ttk

root = Tk()
root.title("FACT")
root.geometry("500x100")

#input
name = StringVar(value="enter fact name")
Label(text="fact name",padx=10,font=30).grid(row=0,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=name)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=0,column=1)

choice = StringVar(value="enter description")
Label(text="description",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=1,column=1)

def cancel():
    root.destroy()

def create():
    pass
Button(text="cancel",font=30,width=15,command=cancel).grid(row=2,column=1,sticky=W)
Button(text="create",font=30,width=15,command=create).grid(row=2,column=1,sticky=E)


root.mainloop()