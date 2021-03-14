import tkinter
from tkinter import *

# import os
# os.system('clear')

root=Tk()
root.title('Electric Bill Calculator')


canvas1 = Canvas(root, width = 600, height = 475,  relief = 'raised')
canvas1.pack()


kWhTotal = Label(root, text='Enter the total kWh invoiced:')
kWhTotal.pack()
canvas1.create_window(300, 25, window=kWhTotal)

entry1 = Entry (root) 
canvas1.create_window(300, 50, window=entry1)


reading1 = Label(root, text='Enter the previous reading:')
reading1.pack()
canvas1.create_window(300, 75, window=reading1)

entry2 = Entry (root) 
canvas1.create_window(300, 100, window=entry2)


reading2 = Label(root, text='Enter the last reading:')
reading2.pack()
canvas1.create_window(300, 125, window=reading2)

entry3 = Entry (root) 
canvas1.create_window(300, 150, window=entry3)


consumptionCost = Label(root, text='Enter the cost to be splitted proportionally:')
consumptionCost.pack()
canvas1.create_window(300, 175, window=consumptionCost)

entry4 = Entry (root) 
canvas1.create_window(300, 200, window=entry4)


extra = Label(root, text='Enter extras like discounts or overprices to be splitted evenly:')
extra.pack()
canvas1.create_window(300, 225, window=extra)

entry5 = Entry (root) 
canvas1.create_window(300, 250, window=entry5)

def splitBill ():

    totalkWh = float(entry1.get())
    oldRead = float(entry2.get())
    newRead = float(entry3.get())
    cost = float(entry4.get())
    extra = entry5.get()

    gkWh = newRead - oldRead
    pkWh = totalkWh - gkWh

    # PERCENTAGES:
    gMultiplier = gkWh / totalkWh
    pMultiplier = pkWh / totalkWh

    if len(entry5.get()) == 0:
        gPay = str(round((gMultiplier * cost + 1.50), 2))
        pPay = str(round((pMultiplier * cost + 1.50), 2))

    else:

        extra = float(entry5.get())

        gPay = str(round((((cost * gMultiplier) + (extra * 0.5)) + 1.50), 2))
        pPay = str(round((((cost * pMultiplier) + (extra * 0.5)) + 1.50), 2))


    gLabel = Label(root, text= 'G has to pay ' + gPay + ' which includes $ 1.50 for Bollettino Postale',font=('helvetica', 10))
    canvas1.create_window(300, 350, window=gLabel)
    pLabel = Label(root, text= 'P has to pay ' + pPay + ' which includes $ 1.50 for Bollettino Postale',font=('helvetica', 10))
    canvas1.create_window(300, 400, window=pLabel)


button1 = Button(text='Split the Bill', command=splitBill, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(300, 300, window=button1)

root.mainloop()