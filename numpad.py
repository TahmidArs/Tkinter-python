from tkinter import*

root=Tk()
root.title("Numpad")
root.geometry("300x300")

#Creating a frame to organize buttons better
#frame=frame(master=root,height=200,width=360,bg="grey")

nums=[[9,8,7],[6,5,4],[3,2,1],['#','0','*']]

for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=75)
    for j in range(3):
        frame=Frame(master=root,relief=SUNKEN,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg='#d0efff')
        label.pack(padx=3,pady=3)

root.mainloop()