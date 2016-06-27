#!/usr/bin/python
import sqlite3
 
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()
 
	#create a table
cursor.execute("""CREATE TABLE jobsearchTable
               (diceId text, positionId text,jobtitle text,location text, companyName text,
               	postedDate text, jobDescription text, postedBy text, phoneNumber text, email text, 
               	contactText text,posting_searched_date text,isEmailSent text) 
            """)
