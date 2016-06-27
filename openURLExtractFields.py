#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re
import sys,datetime,time
from databaseInsert import insert
from databaseQueries import ifDiceIdExists
from ssl import SSLError

def extractData(url):
	#url = "https://www.dice.com/jobs/detail/Senior-Java-MongoDB-Engineer-Intelliswift-Software-Inc-Santa-Clara-CA-95054/10108150/500370?icid=sr57-6p&q=%28java%29&l=94041"
	#url= "https://www.dice.com/jobs/browse"
	#print(url)
	r  = requests.get(url)

	data = r.text
	soup = BeautifulSoup(data,"html.parser")

	try:

		compHeaderInfo=soup.find_all(class_=re.compile("company-header-info"))
		
		#soup5=BeautifulSoup(str(compHeaderInfo),"html.parser")
		#compHead=soup5.find_all(class_=re.compile("col-md-12"))
		
		para = []
		diceIdPost=[]
		positionIdPost=[]
		
		iceBaby=''
		diceId=''

		posBaby=''
		positionId=''

		for x in compHeaderInfo:
		   para.append(str(x))

		paraVal=str(para)
		#print (paraVal)

		#print("****************")

		if paraVal:
			diceIdPost=paraVal.split("Dice Id : ")


		#print (diceIdPost)

		#print("+++++++++++++++")

		if diceIdPost and len(diceIdPost)>1:
			iceBaby=diceIdPost[1]
			diceId=iceBaby[0:8]
		else:
			diceId=''

		paraVal=str(para)
		if paraVal:
			positionIdPost=paraVal.split("Position Id : ")


		if positionIdPost and len(positionIdPost)>1:
			posBaby=positionIdPost[1]
			positionId=posBaby[0:6]
		else:
			positionId=''

		if diceId and diceId.strip():

			print 'diceId:'+diceId
			#print 'positionId:'+positionId

			titleTag = soup.html.head.title
			dara = []
			
			for x in titleTag:
			   dara.append(str(x))

			titleVal=str(dara)
			#title[0]+[1],Company[2],Loc[3],postDate[4]+[5]+[6]

			titleTagSplit=titleVal.split('-')

			jobTitle=str(titleTagSplit[0])
			companyName=str(titleTagSplit[1])
			location=str(titleTagSplit[2])
			postDate=str(titleTagSplit[3]+"-"+titleTagSplit[4]+"-"+titleTagSplit[5])

			# print 'jobTitle is:'+jobTitle
			# print 'companyName:'+companyName
			# print 'location:'+location
			# print 'postDate:'+postDate

			# print type(jobTitle)
			# print type(companyName)
			# print type (location)
			# print type(postDate)

			#diceId positionId




			#postedBy, phoneNumber, email, contactText
			phoneRegex="(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})"
			emailRegex="[\w.-]+@[\w.-]+.\w+"

			matchPhone=re.compile(phoneRegex)
			matchEmail=re.compile(emailRegex)
			
			contacts=soup.find_all(id="contact-container")

			lara = []

			for x in compHeaderInfo:
			   lara.append(str(x))

			laraVal=str(lara)

			phoneNumberList=matchPhone.findall(laraVal)
			phoneNumber=""
			for ph in phoneNumberList:
				phoneNumber=ph

			emailList=matchEmail.findall(laraVal)
			email=""
			for em in emailList:
				email=em

			contactText=laraVal
			
		 	print 'phoneNumber:'+phoneNumber
			print 'email:'+email

			soup6=BeautifulSoup(str(contacts),"html.parser")
		 	postedBy=soup6.find_all(id="contact-name")
			postedB=str(postedBy)

		 	#print 'postedBy:'+postedB
			#print 'contactText:'+contactText
			#jobDetails=soup.find_all(id="bd")

			#jobDescription
			jobDesc=soup.find_all(id="jobdescSec")
			jobDescription=str(jobDesc)

			#print 'jobDescription:'+jobDescription
			posting_searched_date=str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

			if not ifDiceIdExists(diceId):
				insert(diceId,positionId,jobTitle,location ,companyName,postDate,jobDescription,url,phoneNumber,email,contactText,posting_searched_date,"N")
			else:
				print("diceId "+diceId+"already exists, not inserting")

		else:
			print("NO DICE ID")

	#except ValueError:
	#	raise ValueError('empty string')
	except:
		pass


#extractData("https://www.dice.com/jobs/detail/Java-Engineer-Cognate-Inc-Mountain-View-CA-94035/10114372/COGN_25?icid=sr21-1p&q=(java)&l=95134")