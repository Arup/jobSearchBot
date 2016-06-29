import pandas
#!/usr/bin/python

def getDiceIDList():
	colnames = ['DiceID',	'PhoneNo',	'Email',	'Company',	'Link']
	data = pandas.read_csv('test.csv', names=colnames)

	DiceID = data.DiceID.tolist()

	for item in DiceID:
		print str(item)


getDiceIDList()