#!/usr/bin/python
import sqlite3

def ifDiceIdExists(diceId):
	isExists=False
	conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM

	cursor = conn.cursor()

	sql = "SELECT * FROM jobsearchTable WHERE diceId=?"
	m=cursor.execute('SELECT * FROM jobsearchTable WHERE diceId=?', (diceId,))
	#print cursor.fetchall()  # or use fetchone()
	 
	print "\nHere's a listing of all the records in the table:\n"
	for row in m:
	    if row:
	    	isExists=True
	    	break

	return isExists
	 
print(ifDiceIdExists('10114742'))
print(ifDiceIdExists('90526500'))