Create Database Notes;
Use Notes;

Create table notes_saver (
s_no INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(50) NOT NULL,
note_content CHAR(200) NOT NULL,
date DATE
)

SELECT * FROM notes_saver;
#Truncate table notes_saver;
#drop table notes_saver;

INSERT INTO notes_saver (s_no,title,note_content,date) VALUES(1,"SQL CRUD","CRUD Operations in SQL -- Create, Read, Update, Delete",curdate());
