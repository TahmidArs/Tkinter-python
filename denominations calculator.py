from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Denominations Calculator")
root.geometry("650x400")
root.configure(bg="light blue")

label1=Label(root,text="Hey user!Welcome to Denominations Calculator",bg="light blue",font=("Arial",16))
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    MsgBox=messagebox.showinfo("Alert!","Do you want to calculate the denomination count?")
    if MsgBox=="yes":
        topwin()

button1=Button(root,text="Let's get started!",command=msg,bg='brown',fg='white')
button1.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light gray")
    top.geometry("600x450")

    label=Label(top,text="enter total amount",bg="light gray")
    entry=Entry(top)
    lbl=Label(top,text="Here are the number of notes for each denomination",bg="light gray")

    l1=Label(top,text='2000',bg='light gray')
    l2=Label(top,text='500',bg='light gray')
    l3=Label(top,text='100',bg='light gray')

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note2000=amount//2000
            amount %=2000
            note500=amount//500
            amount %=500
            note100=amount//100
            amount %=100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    button=Button(top,text="Calculate",command=calculator,bg='brown',fg='white')

    #centering widget in top window
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    lbl.place(x=150,y=100)
    l1.place(x=100,y=150)
    t1.place(x=200,y=150)
    l2.place(x=100,y=200)
    t2.place(x=200,y=200)
    l3.place(x=100,y=250)
    t3.place(x=200,y=250)
    button.place(x=240,y=120)

    top.mainloop()

root.mainloop()