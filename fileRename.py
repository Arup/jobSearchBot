# !/usr/bin/python

import os,re,sys,datetime,time
from tempfile import NamedTemporaryFile
from shutil import copyfile
# listing directories
#print "The dir is: %s"%os.listdir(os.getcwd())
def renameFile(filenam):

	print ("inside filerename and filename is"+filenam)
	dt = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
	inputFileName=str(filenam)

	newname = 'JobSearch_'+dt+'.txt'
	tmpFile=newname+'.tmp'

	print (newname)
	try:
		os.rename(inputFileName,newname)
		pattern=".*\/jobs\/*.*$"
		encoding = 'utf-8'
		matched = re.compile(pattern)

		with open(newname) as input_file,open(tmpFile,"w") as outfile:
			lines = input_file.readlines()
		    
		    	for line in lines:
		    		if matched.findall(line):
		        			outfile.write(line)
	        #outfile.delete = False # don't delete it on closing
	    	outfile.close()
	    	input_file.close()
		copyfile(tmpFile,newname)

		#input_file.close()
		#outfile.close()
		os.remove(tmpFile)
		
	except Exception, e:
		raise e
	finally:
		pass

	#os.replace(outfile.name, input_file.name)

	# renaming directory ''tutorialsdir"
	#os.rename("tutorialsdir","tutorialsdirectory")

	print "Successfully renamed."

	# listing directories after renaming "tutorialsdir"
	#print "the dir is: %s" %os.listdir(os.getcwd())\

#renameFile("/Users/arup_kabi/Downloads/3.txt")