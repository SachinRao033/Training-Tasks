
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
    cursor.execute("INSERT INTO contact_saver (name,phone,email) VALUES (%s,%s,%s)",(name,phone,email)) #-----> helps to insert data.
    mysql_connector.commit()   #-----> helps to save changes in database

def readContact():
    cursor.execute("SELECT * FROM contact_saver")  #-----> helps to read data from database
    print(cursor.fetchall())

def updateContact(id, name, phone, email):
    cursor.execute("UPDATE contact_saver SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, id)) #----> helps to update data.
    mysql_connector.commit()

def deleteContact(id):
    cursor.execute("DELETE FROM contact_saver WHERE id=%s", (id,))  #-----> helps to delete data from database
    mysql_connector.commit()

while True:
    print("0---> to read contact\n1 --> create contact\n2---> update contact\n3---> delete contact\n4---> exit")
    ip = int(input("Enter a number: "))    #-----> to take input from user
    if ip==0:
        readContact()
    elif ip==1: #---to create contact
        name=input("Enter Name: ")
        phone=int(input("Enter phone number: "))
        email=input("Enter email: ")
        createContact(name, phone , email,)
    elif ip==2: #---to update contact
        id=int(input("Enter id to update: "))
        name=input("Enter new name: ")
        phone=int(input("Enter new phone number: "))
        email=input("Enter new email: ")
        updateContact(id, name, phone, email)
    elif ip==3: #---to delete contact
        id=int(input("Enter id to delete: "))
        deleteContact(id)
    elif ip==4: #---to exit
        break
    else:
        print("Invalid input\n------------>Please try again<------------")










'''class ContactSaver:
    def __init__(self):
        self.name = name
        self.phone = phone
        self.email = email

    def save_contact(self):
        sql = "INSERT INTO contact_saver (name, phone, email) VALUES (%s, %s, %s)"
        val = (self.name, self.phone, self.email)
        mycursor.execute(sql, val)
        mysql_connector.commit()
        print(mycursor.rowcount, "record inserted.")'''



'''name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

def save_contact(name, phone, email):
    sql = "INSERT INTO contact_saver (name, phone, email) VALUES (%s, %s, %s)"
    val = (name, phone, email)
    mycursor.execute(sql, val)
    mysql_connector.commit()
    print(mycursor.rowcount, "record inserted.")


save_contact(name, phone, email)'''



