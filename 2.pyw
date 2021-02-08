import sys
from tkinter import *
import random

def color_change():
	list1=["red","yellow","blue","orange"]
	virus.config(background=random.choice(list1))
	virus.after(200,color_change)

root=Tk()
root.geometry("750x150")
virus=Label(root,text="Do you like my tits best friend?",font=("times",35,"bold"))
virus.grid(row=2,column=0,pady=20,padx=20)
color_change()

root.mainloop()