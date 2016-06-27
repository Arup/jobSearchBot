#!/usr/bin/python

import os, sys,re,time
from openURLExtractFields import extractData
from bs4 import BeautifulSoup
import requests
import re

path = str(os.getcwd())

for file in os.listdir(path):
  if re.match('.*txt$', file):
      	#try:
		encoding = 'utf-8'
		with open(file) as input_file:
			lines = input_file.readlines()
		    	for line in lines:
		        		url= re.search("(?P<url>https?://[^\s]+)", line).group("url")
		        		print ("filename is"+file)
		        		extractData (url)
	        #outfile.delete = False # don't delete it on closing
	    	input_file.close()
		
		#except Exception, e:
		#	raise e
		#finally:
		#	pass
	      #print file