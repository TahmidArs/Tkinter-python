from tkinter import*
from datetime import date

#Create Window
root=Tk()
root.title("Getting started with widgets")
root.geometry('500x500')

#add widgets
#add label
lbl=Label(text="Hey there!",fg="white",bg="black",height=1,width=300)

#add label for getting name as input from user
name_lbl=Label(text="Full Name:",bg="blue")
name_entry=Entry()

def display():
    name=name_entry.get()
    
    global massage
    massage="Welcome to the application \n Today's date is:"
    greet="Hello " + name + "\n"
    
    text_box.insert(END,greet)
    text_box.insert(END,massage)
    text_box.insert(END,date.today())

#add a text widget to display the massage
text_box=Text(height=3)
btn=Button(text="Begin",command=display,height=1,bg="green",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()