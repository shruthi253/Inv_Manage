import sqlite3
import sys
import tkinter as tk
import exp_date as ep

def data_table():
    conn = sqlite3.connect(database='shrunev.db')
    c = conn.cursor()

    #Create table -- only one time execution
    # c.execute("""CREATE TABLE P$ITEM(
    #         Item_Name varchar,
    #         Item_Quantity real,
    #         Item_Expiry Date
    #         )""")

    #alter table -- only one time execution
    #c.execute("ALTER TABLE P$ITEM ADD Item_Days integer")

    #delete items from table -- if needed
    #c.execute("""DELETE FROM P$ITEM""")

    #select items from table -- if needed
    c.execute("""SELECT * FROM P$ITEM""")
    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()


def submit(item_name,item_quantity,item_expiry,var,Item_Days):
    try:
        conn = sqlite3.connect(database='shrunev.db')
        c = conn.cursor()

        #Insert table
        c.execute("INSERT INTO P$ITEM VALUES(:Item_Name, :Item_Quantity, :Item_Expiry, :Item_Flag, :Item_Days)",
            {'Item_Name': item_name.get() ,
            'Item_Quantity': item_quantity.get(),
            'Item_Expiry':item_expiry.get(),
            'Item_Flag': var.get(),
            'Item_Days': ep.date_avb(item_expiry)         
            } 
            )
        conn.commit()
        conn.close()
    except:
        print('Could not connect to DB',sys.exc_info()[0])
        raise


def retrieve():
    try:
        conn = sqlite3.connect(database='shrunev.db')
        c = conn.cursor()

        #Insert table
        c.execute("SELECT * FROM P$ITEM")
        #c.execute("SELECT (SELECT julianday(ITEM_EXPIRY) FROM P$ITEM) - (SELECT julianday(date('now')))")
        records = c.fetchall()
        #print(records)
        
        print_rec = ''
        for record in records:
            print_rec += str(record) + '\n'
            
            # dis_label = Label(top,text=print_rec)
            # dis_label.grid(row=8,column=0,columnspan=2,padx=10, pady=10, ipadx =137)
            #row_num += 1

        if print_rec != '':
            tk.messagebox.showinfo('Details',print_rec)
        else:
            tk.messagebox.showinfo('Details','No saved items available')
            
        conn.commit()
        conn.close()
    except:
        print('Could not connect to DB',sys.exc_info()[0])
        raise

def soon_expire():
    try:
        conn = sqlite3.connect(database='shrunev.db')
        c = conn.cursor()

        #Select items with available days <10
        c.execute("SELECT * FROM P$ITEM WHERE Item_Days < 10")
        records = c.fetchall()
        #print(records)
        
        print_rec = ''
        for record in records:
            print_rec += str(record) + '\n'
            
            # dis_label = Label(top,text=print_rec)
            # dis_label.grid(row=8,column=0,columnspan=2,padx=10, pady=10, ipadx =137)
            #row_num += 1

        if print_rec !='':
            tk.messagebox.showinfo('Details',print_rec)
        else:
            tk.messagebox.showinfo('Details','Hooray!!No soon to expire item..Enjoy!')
      
        conn.commit()
        conn.close()
    except:
        print('Could not connect to DB',sys.exc_info()[0])
        raise
