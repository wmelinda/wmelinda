#This fourth part of code is something that I thought of near the end, after running the code multiple times. 
#After I ran the code multiple times, I noticed that the same beaches and files were being created over and over again (each time I ran the code). 
#This code prevents the creation of a file if a file of the same name already exists. 

#Name of the test file  
name = "Spiaggia_dei_Conigli-Lampedusa_Islands_of_Sicily_Sicily"

#Setup 
import os.path

#Location of the test file 
test = str("C:\Users\wmelinda\Documents\#JUMP Investors" + '\\' + name + ".txt")
print test

#If the file exists, print "yes" 
#If the file does not exist, print "no" 
#I was mainly testing to make sure that only a portion of the code continues to read next steps (e.g. if no file, code continues through) 
#So, because I had a test file already saved, when I ran the code = printed "no" and also printed "continue" 
if os.path.isfile(test): 
		continue 
else: 
		print "no"
		pass 
print "continue"
