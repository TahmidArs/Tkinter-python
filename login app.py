from tkinter import*

root=Tk()
root.title("Login App")
root.geometry("300x300")

frame=Frame(master=root,height=200,width=360,bg='blue')

#Add widgets
#Add Label
lbl1=Label(frame,text='Username',bg='#3895D3',fg='white',width=12)
lbl2=Label(frame,text='Password',bg='#3895D3',fg='white',width=12)
lbl3=Label(frame,text='Email Id',bg='#3895D3',fg='white',width=12)

#Use Entry widget to take in put from user
name_entry=Entry(frame)
password_entry=Entry(frame)
email_entry=Entry(frame,show='*')

def display():
    name=name_entry.get()
    greet='Hey'+name
    massage="Congratulations for your new account!"
    textbox.insert(END,greet)
    textbox.insert(END,massage)

#Textbox to display massage
textbox=Text(bg='#BEBEBE',fg='black')

btn=Button(frame,text='create account',command=display,bg='red')

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
lbl2.place(x=20,y=80)
lbl3.place(x=20,y=140)
name_entry.place(x=150,y=20)
password_entry.place(x=150,y=140)
email_entry.place(x=150,y=80)
btn.place(x=130,y=210)
textbox.place(y=250)
root.mainloop()