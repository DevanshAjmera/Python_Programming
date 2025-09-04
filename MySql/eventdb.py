import mysql.connector

# create databases connection to mysql
connection = mysql.connector.connect(host = "localhost",
                                     username = "root",
                                     password = "Devansh@1012",
                                     database = "event")

# to check the connection establish or not
if connection.is_connected():
    print("db is connected")
else:
    print("db not connected")

# to create user table in database
user = "create table if not exists user(fname text)"

#to pass the cursor handle sql query
mycursor = connection.cursor()

#to execute the sql query
mycursor.execute(user)
connection.commit()

# to insert fname in users table
insertName = "insert into user values ('{}')".format("Devansh Ajmera")
mycursor.execute(insertName)
connection.commit()

#to create user table in database
users = "create table if not exists addevent(eventname text, username text, eventdate text, email text, department text, mobile text)" #table name 

#to pass the cursor handle sql query
mycursor = connection.cursor()

#to execute the sql query
mycursor.execute(users)
connection.commit()

#to insert fname in users table
# insertName = "insert into addevent values ('{}','{}','{}','{}','{}','{}')".format(input("enter event name"),input("enter username:"),input("enter evendate:"),input("enter email:"),input("enter departmentname:"),input("enter mobileno:"))
# it is the static data on compile tiome 
# mycursor.execute(insertName) 
# connection.commit()

# to update the event details in database
# updateEvent="update addevent set eventname='VAm'where mobile='9876556780'"
# # update is based on unique column
# mycursor.execute(updateEvent)
# connection.commit()

# to delete the event from dtabase
# deleteEvent="delete from addevent where mobile='980007659'"
# mycursor.execute(deleteEvent)
# connection.commit()

# to fetch the event list fromm database
eventlist="select *from addevent"
mycursor.execute(eventlist)
print(mycursor.fetchall())
connection.commit()

# drop the  table event
dropevent="drop table addevent"
mycursor.execute(dropevent)
connection.commit()

# event railway reservation system, college management system, library, hotel booking, flight booking