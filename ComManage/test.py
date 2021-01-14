import sqlite3



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
c.execute("""DELETE FROM P$ITEM""")

#select items from table -- if needed
c.execute("""SELECT * FROM P$ITEM""")
records = c.fetchall()
print(records)

conn.commit()
conn.close()