from tkinter import *
import tkinter as tk
root = Tk()
menu = Menu(root)
root.geometry("400x400")  #for menu 

root.title('Stock Simulator v1.0')

#--Config elements--#
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#--for buying stonks--#
B1t=Label(root, text='First Name').grid(row=0)
b1t=Entry(root)
b1t.grid(row=0, column=1)

b1b = tk.Button(root, text='Close', width=25, command=root.destroy)
b1b.grid(row=0,column=2)

#--for selling stonks--#



w = Spinbox(root, from_ = 0, to = 10)
#w.pack()
#b1b.pack()
root.mainloop()
