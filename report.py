#!/usr/bin/python
import sqlite3

def reportDiceId(diceId):
	conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM

	cursor = conn.cursor()

	#sql = "SELECT * FROM jobsearchTable WHERE diceId=?"
	m=cursor.execute('SELECT diceId,postedBy,email,phoneNumber FROM jobsearchTable ')
	#print cursor.fetchall()  # or use fetchone()
	 
	print "\nHere's a listing of all the records in the table:\n"
	for row in m:
	    if row:
	    	print (row)
	    	

print(reportDiceId('10114742'))
print(reportDiceId('90526500'))