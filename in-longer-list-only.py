#	in-longer-list-only.py
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	given two single column files:
#			shorter.txt
#			longer.txt
#
#	This will print all the values from 'longer.txt' that
#	do not appear in 'shorter.txt'
#
#	ex.	longer.txt:	cat
#					mouse
#					climb
#		shorter.txt:climb
#					cat
#	OUTPUT:	mouse
#			

import sys
#will print the list of items that are unique to longer.txt 
# i.e. things in longer.txt that are not in shorter.txt


print "THE FOLLOWING APPEARS IN 'longer.txt'\nBUT NOT IN 'shorter.txt':"
longer = []
l = open('longer.txt','r')
for line in l:
	line = line.strip()
	longer.append(line)

shorter = []
s = open('shorter.txt','r')
for line in s:
	line = line.strip()
	shorter.append(line)

for i in range(0,len(longer)):
	if longer[i] in shorter:
		pass
	else:
		print longer[i]