
import mysql.connector

mysql_connector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="notes" )

cursor = mysql_connector.cursor()               #-----> helps to execute sql commands


def createNote(title,note_content):
    cursor.execute("INSERT INTO notes_saver (title, note_content, date) VALUES (%s, %s, CURDATE())", (title, note_content)) #-----> helps to insert data into database
    mysql_connector.commit()                            #-----> helps to save changes in database

def readNote():
    cursor.execute("SELECT * FROM notes_saver")  #-----> helps to read data from database
    rows = cursor.fetchall()

    for row in rows:
        s_no, title, note_content, date = row
        print(f"SERIAL NO:- {s_no}, TITLE:- {title}, NOTE CONTENT:- {note_content}, DATE:- {date.strftime('%Y-%m-%d')} \n")

def updateNote(s_no, title, note_content, date):                                  #----> helps to update data in database
    update_fields = []
    update_values = []

    f=update_fields     #f for fields
    v=update_values     #v for values

    if title is not None:
        f.append("title=%s")
        v.append(title)
    if note_content is not None:
        f.append("note_content=%s")
        v.append(note_content)
    if date is not None:
        f.append("date=%s")
        v.append(date)

    if update_fields:
        query = (f"UPDATE notes_saver SET {', '.join(f)} WHERE s_no=%s")
        v.append(s_no)
        cursor.execute(query, tuple(v))

    mysql_connector.commit()

def deleteNote(s_no):
    cursor.execute("DELETE FROM notes_saver WHERE s_no=%s", (s_no,))             #-----> helps to delete data from database
    mysql_connector.commit()

def searchNote(title,note_content,date):
    cursor.execute("SELECT * FROM notes_saver WHERE title=%s OR note_content=%s OR date=%s", (title,note_content,date))  #-----> helps to search data from database
    print(cursor.fetchall())

while True:
    print(" 0---> To Read Notes\n 1 --> Create Note\n 2---> Update Note\n 3---> Search Note\n 4---> Delete Note\n 5---> Exit")
    ip = int(input("Enter a number: "))                                             #-----> to take input from user

    if ip==0:
        readNote()
    elif ip==1:                                                                     #---to create note
        title=input("Enter title: ")
        note_content=input("Enter note content: ")
        createNote(title, note_content)
    elif ip==2:                                                                     #---to update note
        s_no=int(input("Enter serial number to update: "))
        title=input("Enter new title (or) press enter to skip: ")
        note_content=input("Enter new note content (or) press enter to skip: ")
        date=input("Enter new date (YYYY-MM-DD) (or) press enter to skip: ")
        if title=="":
            title=None
        if note_content=="":
            note_content=None
        if date=="":
            date=None
        updateNote(s_no, title, note_content, date)
    elif ip==3:                                                                     #---to search note
        title=input("Enter title to search (or) press enter to skip: ")
        note_content=input("Enter note content or keyword to search (or) press enter to skip: ")
        date=input("Enter date to search (or) press enter to skip: ")
        if title=="":
            title=None
        if note_content=="":
            note_content=None
        if date=="":
            date=None
        searchNote(title,note_content,date)
    elif ip==4:                                                                     #---to delete contact
        s_no=int(input("Enter serial number to delete: "))
        deleteNote(s_no)
    elif ip==5:                                                                     #---to exit
        break
    else:
        print(" Invalid Input\n ------------> PLEASE TRY AGAIN <------------ ")



#mysql_connector.close()                                                        #-----> helps to close the connection with database
