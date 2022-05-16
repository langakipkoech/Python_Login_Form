#import tkinter library
from tkinter import *
from unicodedata import name

root = Tk()




#create window
root.geometry("500x300")

#define function
def getvals():
    print("Accepted")

#heading
    Label(root, text="Python Reg Form", font="arial 15 bold").grid(row=0, column=3)
#reg attributes
#field name
name=Label(root, text="Name")
Phone=Label(root, text="Phone")
Gender=Label(root, text="Gender")
Payment=Label(root, text="Payment")
#packing fields
name.grid(row=1, column=2)
Payment.grid(row=2, column=2)
Phone.grid(row=3, column=2)
Gender.grid(row=4, column=2)

#storing bvalues using variables
namevalue = StringVar
Paymentvalue = StringVar
Phonevalue = StringVar
Gendervalue = StringVar

checkvalue = IntVar



#create entry for inputing details

nameentry = Entry(root, textvariable = namevalue)
Paymententry = Entry(root, textvariable = Paymentvalue)
Phoneentry = Entry(root, textvariable = Phonevalue)
Genderentry = Entry(root, textvariable = Gendervalue)
#packing entry fields
nameentry.grid(row=1, column=3)
Paymententry.grid(row=2, column=3)
Phoneentry.grid(row=3, column=3)
Genderentry.grid(row=4, column=3)

#create checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=5, column=3)

#submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
