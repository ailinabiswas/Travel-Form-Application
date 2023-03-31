from tkinter import *

root=Tk()

def getvals():
    print("Submitted Successfully")

    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")

    with open("record.txt","a")as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")

root.geometry("544x344")

Label(root,text="Welcome to ABCD Travels",font="comicsansns 13 bold",pady=10).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone Number")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=3,column=2)
gender.grid(row=5,column=2)
emergency.grid(row=7,column=2)
paymentmode.grid(row=9,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=3,column=3)
genderentry.grid(row=5,column=3)
emergencyentry.grid(row=7,column=3)
paymentmodeentry.grid(row=9,column=3)

foodservice=Checkbutton(text="Want to prebook meals?",variable=foodservicevalue)
foodservice.grid(row=11,column=3)

Button(text="Submit",command=getvals).grid(row=13,column=3)

root.mainloop()

