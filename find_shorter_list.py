# find_shorter_list.py
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	given two lists: shorter_list.txt and longer_list.txt
#	shorter_list.txt 	(a list with two columns)
#	longer_list.txt		(a list containing two columns)
#						(second column matches some but not all of shorter_list.txt)
#
#	will return, in the order of the shorter list:
#	firstcolumn	second column
#
#	ex.	shorter_list.txt:		cat
#		longer_list.txt:	a	dog
#							b 	cat
#	OUTPUT:	b	cat


import sys

short = []
f = open("shorter_list.txt",'r')
for line in f:
	line = line.strip()
	short.append(line)
print short

lon = []
g = open("longer_list.txt",'r')
for line in g:
	line = line.strip()
	lon.append(line.split("\t"))
#print lon


for i in range(0,len(short)):
	for x in range(0,len(lon)):
		if short[i] in lon[x][1]:
			print str(lon[x][0])+"\t"+str(lon[x][1])


#output should be:
# d	adam
# a nuts
# b peas
		
