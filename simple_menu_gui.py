# menu bar in python #gui python programming
# using tkinter module

from tkinter import * #import all
# do all libaries need to be  imported, warning given.

root = Tk()
root.title("Menu in GUI")
root.geometry("250x100")

#create menubar
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)

#creates file in menu bar
menubar.add_cascade(label="File", menu=filemenu)
#create another option in file menu # can add more???
filemenu.add_command(label="New",command=None)
#create view menu in menubar
menubar.add_cascade(label="View")
#create exit menu, close menu window while, clicked??
menubar.add_command(label="Exit",command=root.destroy)

root.mainloop()