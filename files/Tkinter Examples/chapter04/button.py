from Tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Buttons')
Label(root, text="You shot him!").pack(pady=10)
Button(root, text="He's dead!", state=DISABLED).pack(side=LEFT)
Button(root, text="He's completely dead!", command=root.quit).pack(side=RIGHT)
root.mainloop()

