# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#importing database
import sqlite3;

#connecting the databse to the program
conn= sqlite3.connect('akaike_sql.db');
print("connection established");
cursor= conn.cursor();

#dropping table so that previous versions are discarded
cursor.execute("DROP TABLE IF EXISTS EMPLOYEEE");

#creating a table
query= '''CREATE TABLE IF NOT EXISTS employeee (
    `Employee_Id` INT NOT NULL,
    `Employee_Name` VARCHAR(5),
    `rating` INT,
    `Supervisor_id` INT,
    `Designation` VARCHAR(10) 
)''';
cursor.execute(query);
conn.commit();
print('Table created');

#Adding values into the table
query='''INSERT INTO employeee VALUES
    (1,'Dr. Max',9,3,'doctor'),
    (2,'Dr. James',8,4,'doctor'),
    (3,'Peter',6,0,'Supervisor'),
    (4,'Simon',9,0,'Supervisor');'''
cursor.execute(query);
conn.commit();
print("Records inserted");
   

#Executing the query asked in the assignment
query='''SELECT
        firstt.Employee_Name 
    FROM
        `employeee` firstt 
    INNER JOIN
        `employeee` second 
            ON firstt.Supervisor_id = second.Employee_id 
    WHERE firstt.rating > second.rating;''';
cursor.execute(query);
result=cursor.fetchall();
#Printing the results
for x in range(len(result)):
    print (result[x],end=' ');
    print("earns more than his supervisor\n") 
conn.commit();

#closing the connection
conn.close();
