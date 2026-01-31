Create Database Notes;
Use Notes;

Create table notescontent_saver (
s_no INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(50) NOT NULL,
note_content CHAR(200) NOT NULL,
date DATE
)

SELECT * FROM notescontent_saver;
#Truncate table notescontent_saver;
#drop table notescontent_saver;

INSERT INTO notescontent_saver (s_no,title,note_content,date) VALUES(1,"SQL CRUD","CRUD Operations in SQL -- Create, Read, Update, Delete",curdate());


