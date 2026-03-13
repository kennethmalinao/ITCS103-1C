import tkinter as tk

window=tk.Tk()
window.title("Simple Calculator")
window.geometry("200x200")
window.config(bg="lightblue")

label=tk.Label(window,text="Simple Calculation",width=28,height=2)
label.grid(row=0,column=0,columnspan=2)

tk.Label(window,text="Enter 1st Number:").place(x=10,y=45)
entry1=tk.Entry(window,width=10)
entry1.place(x=120,y=45)

tk.Label(window,text="Enter 2nd Number:").place(x=8,y=80)
entry2=tk.Entry(window,width=10)
entry2.place(x=120,y=80)

def add():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1+num2
    label.config(text=f"The sum of {num1} + {num2} = {result}")

def subtract():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1-num2
    label.config(text=f"The difference of {num1} - {num2} = {result}")

def multiply():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1*num2
    label.config(text=f"The product of {num1} x {num2} = {result}")

def divide():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result=num1/num2
    label.config(text=f"The quotient of {num1} / {num2} = {result}")


btn1=tk.Button(window,text="Add",command=add)
btn1.place(x=45,y=110)

btn2=tk.Button(window,text="Subtract",command=subtract)
btn2.place(x=125,y=110)

btn3=tk.Button(window,text="Multiply",command=multiply)
btn3.place(x=35,y=150)

btn4=tk.Button(window,text="Division",command=divide)
btn4.place(x=126,y=150)
window.mainloop()