
import mysql.connector

crusor = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="contacts" )

mycursor = crusor.cursor()