from tkinter import*
root=Tk()
root.title("main")
root.geometry("400x300")

def topwin():
    top=Toplevel()
    top.title("Top window")
    top.geometry("100x100")

    l2=Label(top,text="This is a toplevel window")
    l2.pack()

    top.mainloop()

#Addng a label and button widget to root(main) window
l=Label(root,text="This is the main window")
l.pack()
btn=Button(root,text="Click here to open top window",command=topwin)
btn.pack()

root.mainloop()