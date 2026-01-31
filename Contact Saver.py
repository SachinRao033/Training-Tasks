
import mysql.connector

mysql_connector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="contacts" )

cursor = mysql_connector.cursor()

#cursor.execute("")   #-----> helps to execute sql commands
#cursor.execute("Select * from contact_saver")
#print(cursor.fetchall())


def createContact(name, phone, email):
    cursor.execute("INSERT INTO contact_saver (name,phone,email) VALUES (%s,%s,%s)",(name,phone,email)) #-----> helps to insert data into database
    mysql_connector.commit()   #-----> helps to save changes in database

def readContact():
    cursor.execute("SELECT * FROM contact_saver")  #-----> helps to read data from database
    print(cursor.fetchall())

def searchContact(name,phone,email):
    cursor.execute("SELECT * FROM contact_saver WHERE name=%s OR phone=%s OR email=%s", (name,phone,email))  #-----> helps to search data from database
    print(cursor.fetchall())

def updateContact(id, name, phone, email):
    cursor.execute("UPDATE contact_saver SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, id)) #----> helps to update data in database
    mysql_connector.commit()

def deleteContact(id):
    cursor.execute("DELETE FROM contact_saver WHERE id=%s", (id,))                  #-----> helps to delete data from database
    mysql_connector.commit()

while True:
    print("0---> to read contact\n 1 --> create contact\n 2---> update contact\n 3---> search contact\n 4---> delete contact\n 5---> exit")
    ip = int(input("Enter a number: "))                                             #-----> to take input from user
    if ip==0:
        readContact()
    elif ip==1:                                                                     #---to create contact
        name=input("Enter Name: ")
        phone=int(input("Enter phone number: "))
        email=input("Enter email: ")
        createContact(name, phone , email,)
    elif ip==2:                                                                     #---to update contact
        id=int(input("Enter id to update: "))
        name=input("Enter new name: ")
        phone=int(input("Enter new phone number: "))
        email=input("Enter new email: ")
        updateContact(id, name, phone, email)
    elif ip==3:                                                                     #---to search contact
        name=input("Enter Name to search (or) press enter to skip: ")
        phone=input("Enter phone number to search (or) press enter to skip: ")
        email=input("Enter email to search (or) press enter to skip: ")
        if name=="":
            name=None
        if phone=="":
            phone=None
        if email=="":
            email=None
        searchContact(name, phone, email)
    elif ip==4:                                                                     #---to delete contact
        id=int(input("Enter id to delete: "))
        deleteContact(id)
    elif ip==5:                                                                     #---to exit
        break
    else:
        print("Invalid input\n------------>Please try again<------------")

#mysql_connector.close()  #-----> helps to close the connection with database