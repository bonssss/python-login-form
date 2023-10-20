from tkinter import *
root =Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")


Label(root,text="python registration form",font="ar 15 bold").grid(row=0, column=3)

name=Label(root, text="name")
phone=Label(root, text="phone")
Gender=Label(root, text="Gender")
emergency=Label(root, text="emergency")
payment=Label(root, text="payment")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
Gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
Gendervalue = StringVar
emergencyvalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
Genderentry = Entry(root, textvariable =Gendervalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)
paymententry = Entry(root, textvariable =paymentvalue)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

checkbtn = Checkbutton(text=" remember me?", variable = checkvalue)
checkbtn.grid(row=6 , column=3)

Button(text=" submit", command=getvals).grid(row=7 ,column=3)
root.mainloop()
