# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:59:12 2015

@author: yinyin
"""

from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry()

def print_item(event):
    print lb.get(lb.curselection())
    
var = StringVar()
lb = Listbox(root, height=8, listvariable = var)
lb.bind('<ButtonRelease-1>', print_item)
list_item = [1 , 2 , 3, 4, 5, 6, 7, 8, 9, 0]
for item in list_item:
    lb.insert(END, item)
    
scrl = Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
lb.configure(yscrollcommand = scrl.set)
lb.pack(side=LEFT)
scrl['command'] = lb.yview

root.mainloop()