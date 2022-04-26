import tkinter as tk
from tkinter import ttk
from tkinter import *
from libraries import trendSpike as tS

def getInputBoxValue():
	userInput = tInput.get()
	return userInput
     
def getSort():
	return comboSort.get()

def getArticles():
	return int(comboArticles.get())

def getPeaks():
	return int(comboPeaks.get())

def btnClickFunction():
        tS.searchList(getInputBoxValue(),getPeaks(),getArticles(),getSort())
	

root = Tk()

# This is the section of code which creates the main window
root.geometry('300x350')
root.configure(background='#F0F8FF')
root.title('Search Window')

# This is the section of code which creates the a label
Label(root, text='Google Trends Highlights Search', bg='#F0F8FF', font=('arial', 13, 'bold')).place(x=16, y=10)
Label(root, text='Sort by', bg='#F0F8FF', font=('arial', 11, 'normal')).place(x=25, y=125)
Label(root, text='Peaks', bg='#F0F8FF', font=('arial', 11, 'normal')).place(x=25, y=195)
Label(root, text='Articles', bg='#F0F8FF', font=('arial', 11, 'normal')).place(x=137, y=195)
Label(root, text='Search Query', bg='#F0F8FF', font=('arial', 11, 'normal')).place(x=25, y=53)

# This is the section of code which creates a text input box
tInput=Entry(root, width = 30)
tInput.place(x=27, y=77)

comboSort= ttk.Combobox(root, values=['Popularity','Chronological'], font=('arial', 12, 'normal'), width=15)
comboSort.place(x=27, y=147)
comboSort.current(0)

# This is the section of code which creates a combo box
comboArticles= ttk.Combobox(root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], font=('arial', 12, 'normal'), width=3)
comboArticles.place(x=137, y=217)
comboArticles.current(4)

# This is the section of code which creates a combo box
comboPeaks= ttk.Combobox(root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], font=('arial', 12, 'normal'), width=3)
comboPeaks.place(x=27, y=217)
comboPeaks.current(4)

# This is the section of code which creates a button
Button(root, text='Search!', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=27, y=285)

root.mainloop()



