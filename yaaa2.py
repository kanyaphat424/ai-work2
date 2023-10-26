from tkinter import *
from tkinter import ttk

root2 = Tk()
root2.title("FACT")
root2.geometry("500x220")

#input
fact1 = StringVar(value="-----Enter-----")
Label(text="Fact1",padx=10,font=30).grid(row=0,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=fact1)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=0,column=1)
opertorr = StringVar(value="-----None-----")
Label(text="Operator",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=opertorr)
combo["values"]=("AND","OR")
combo.grid(row=1,column=1)

fact2 = StringVar(value="-----Enter-----")
Label(text="Fact2",padx=10,font=30).grid(row=2,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=fact2)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=2,column=1)

conclude1 = StringVar(value="-----None-----")
Label(text="Conclude1",padx=10,font=30).grid(row=3,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=conclude1)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=3,column=1)

conclude2 = StringVar(value="-----None-----")
Label(text="Conclude2",padx=10,font=30).grid(row=4,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=conclude2)
combo["values"]=("A","B","C","D","E","X")
combo.grid(row=4,column=1)

def cancel():
    root2.destroy()

def calculate():
    pass
Button(text="Cancel",font=30,width=15,command=cancel).grid(row=5,column=1,sticky=W)
Button(text="Calculate",font=30,width=15,bg="blue",command=calculate).grid(row=5,column=1,sticky=E)
root2.mainloop()