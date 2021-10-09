import time
import sys

#this code opens the file in read mode
showfile = open(sys.argv[1], "r")

#create a list to store 
list = []

#this code reads the file line by line into a list?
fl = showfile.readlines()
#print(fl)

showfile.close

print("\n THIS IS THE INPUT CHANNEL LIST: \n \n")


#~~~~TEST CODE HERE~~~~
#this code iterates over each list item dentifying text to find items containing channel names
#and prints them 
for x in fl:
	if "ch" in x:
		if "config" in x:

			#this will print line by line
			print(x)
			time.sleep(0.05)

	if "bus" in x:
		if "config" in x:

			#this will print line by line
			print(x)
			time.sleep(0.05)


#~~~~WRITE TO FILE CODE HERE~~~~
#this code iterates over each list item dentifying text to find items containing channel names
#and adds them to our list
for x in range(0, len(fl)):
	if "ch" in fl[x]:
		if "config" in fl[x]:
			list.append(fl[x])

for x in range(0, len(fl)):
	if "bus" in fl[x]:
		if "config" in fl[x]:
			list.append(fl[x])

'''x = 0

prefix = "/ch/"

while x = < len(list)'''
	


#creates text file to write into
patchlist = open("patchlist.txt", "w+")
	
for x in list: 

	patchlist.write(x + "\n")

patchlist.close()


#/ch/01/config - this is the text that precedes the channel name
