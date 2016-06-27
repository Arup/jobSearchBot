#!/usr/bin/python
import sqlite3

 
def insert(diceId,positionId,jobtitle,location,companyName,postedDate,jobDescription,
	postedBy,phoneNumber,email,contactText,posting_searched_date,isEmailSent):

	conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
	cursor = conn.cursor()	



	print ("before insert")
	print (type(diceId))
	print (type(jobtitle))
	#sql='INSERT INTO jobsearchTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(diceId,positionId,jobtitle,location,companyName,postedDate,jobDescription,postedBy,phoneNumber,email,contactText,posting_searched_date,isEmailSent)
	print ("$$$$$$$$$")
	#print (sql)
	cursor.execute('INSERT INTO jobsearchTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(diceId,positionId,jobtitle,location,companyName,postedDate,jobDescription,postedBy,phoneNumber,email,contactText,posting_searched_date,isEmailSent))
	print ("after insert")
	# save data to database
	conn.commit()


