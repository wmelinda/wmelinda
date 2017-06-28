name = "Spiaggia_dei_Conigli-Lampedusa_Islands_of_Sicily_Sicily"
import os.path
test = str("C:\Users\wmelinda\Documents\#JUMP Investors" + '\\' + name + ".txt")
print test
if os.path.isfile(test): 
		print "yes" 
else: 
		print "no"
		pass 
print "continue"