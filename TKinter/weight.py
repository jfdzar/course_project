from tkinter import *

window=Tk()

def convert_kg():
    kg = float(e1_value.get())
    grams = kg*1000
    pounds = kg*2.20462
    ounces = kg*35.274

    t_grams.delete(1.0,END)
    t_grams.insert(CURRENT,grams)
    t_pounds.delete(1.0,END)
    t_pounds.insert(END,pounds)
    t_ounces.delete(1.0,END)
    t_ounces.insert(END,ounces)

t_kg=Label(window,text="Kg")
t_kg.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text='Convert',command=convert_kg)
b1.grid(row=0,column=2)

t_grams=Text(window,height=1,width=20)
t_grams.grid(row=1,column=0)

t_pounds=Text(window,height=1,width=20)
t_pounds.grid(row=1,column=1)

t_ounces=Text(window,height=1,width=20)
t_ounces.grid(row=1,column=2)



window.mainloop()
