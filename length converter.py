import tkinter as tk
root=tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x400")

def convert_to_centimeters(inches):
    try:
        inches=float(entry_inch.get())
        cm = inches * 2.54
    except ValueError:
        print("Invalid input.Please enter a number")


tk.Label(root,text="Enter length in Inches:").grid(row=0,column=0,padx=20,pady=10)
entry_inch=tk.Entry(root)
entry_inch.grid(row=0,column=1,padx=10,pady=10)


convert_button=tk.Button(root,text="Convert",command=convert_to_centimeters)
convert_button.grid(row=1,column=0,columnspan=2,pady=10)

root.mainloop()