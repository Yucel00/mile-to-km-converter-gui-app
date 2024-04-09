from tkinter import *
window=Tk()
window.title("Mile To Km Converter")
window.config(padx=20,pady=20)


miles=Entry()
miles.insert(END,string="Please Input Mile")
miles.focus()
miles.grid(column=1,row=0)


label1=Label(text="Miles",font=("Arial",14))
label1.grid(column=2,row=0)


label2=Label(text="is equal to",font=("Arial",14))
label2.grid(column=0,row=1)
label3=Label(text="",font=("Arial",14),width=20)
label3.grid(column=1,row=1)
label4=Label(text="Km",font=("Arial",14))
label4.grid(column=2,row=1)

def mile_to_kilometer():
    mile=miles.get()
    km=int(mile)/0.62137
    label3.config(text=km)

button=Button(text="calculate",command=mile_to_kilometer)
button.grid(column=1,row=2)
button.config(padx=5,pady=5)

window.mainloop()
