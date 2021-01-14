import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'shru', passwd = 'odikko123',database = 'shrnvn')

mycursor = mydb.cursor()
mycursor1 = mydb.cursor()

mycursor.execute('show databases')

for i in mycursor:   #one way
    print(i)

mycursor1.execute('select * from student')
result = mycusor1.fetchall() #all rec
result = mycursor1.fetchone() #one rec

for i in result:
    print(i)