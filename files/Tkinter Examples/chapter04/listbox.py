from Tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Listbox')
list = Listbox(root, width=15)
list.pack()
for item in range(10):
    list.insert(END, item)
root.mainloop()

