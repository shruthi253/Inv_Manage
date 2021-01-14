import tkinter as tk
from tkinter import messagebox
import db_con as dbc
import exp_date as ep
import gen_func as gf
from tkcalendar import Calendar,DateEntry

#manage close button 
def on_closing():
    top.destroy()

#Define Main screen
top = tk.Tk()
top.title ('COMMODITY MANAGEMENT')
top.geometry('500x300')

#Add labels to items
item_name_lbl = tk.Label(top,text='ITEM NAME',width=30)
item_name_lbl.grid(row=0,column=0, padx=10)
item_quantity_lbl = tk.Label(top,text='ITEM QUANTITY')
item_quantity_lbl.grid(row=1,column=0, padx=10)
item_expiry_lbl = tk.Label(top,text='ITEM EXPIRY')
item_expiry_lbl.grid(row=2,column=0, padx=10)


#Add items to screen using edit/entry box 
item_name = tk.Entry(top,width=30)
item_name.grid(row=0,column=1,padx = 10, pady = 10)
item_quantity = tk.Entry(top,width=30)
item_quantity.grid(row=1,column=1,padx =10, pady = 10)
item_expiry = DateEntry(top,width=27,bg="darkblue",fg="white",year=2020)
item_expiry.grid(row=2,column=1,padx =10, pady = 10)

item_days = tk.Button(top,text='Soon to Expire!!',bg= 'red', command=dbc.soon_expire)
item_days.grid(row=6, column=0,padx=10, pady=10, ipadx=40)

#checkbox for item type
var = tk.StringVar()
item_flag = tk.Checkbutton(top,text = 'Perishable', variable = var, onvalue = 'Perishable',offvalue='Non-perishable')
item_flag.deselect() #happens to have checkbox selected by default when using StringVar()
item_flag.grid(row=5, column=0, padx=10, pady=10)

#add submit button to add to DB
Submit_btn = tk.Button(top,text='Add Items', bg = 'green', command = lambda : dbc.submit(item_name,item_quantity,item_expiry,var,item_days),width=25)
Submit_btn.grid(row=5,column=1,padx =10, pady = 10)

#show details of all saved items
Details_btn = tk.Button(top,text='Show Saved Items', bg = 'blue', command = dbc.retrieve)
Details_btn.grid(row=6, column=1,padx=10, pady=10, ipadx=40)

#button to browse from internet
Browser_btn = tk.Button(top,text='Browse More', bg = 'green', command = gf.Open_Program, width=25)
Browser_btn.grid(row=7, column=1,padx=10, pady=10)

#calculate days
# Days_entry= tk.Button(top,text='Days Left',command=ep.date_avb(item_expiry), width=25)
# Days_entry.grid(row=7, column=0,padx=10, pady=10)

#added in case need to manipulate close button
top.protocol("WM_DELETE_WINDOW", on_closing)

top.mainloop()