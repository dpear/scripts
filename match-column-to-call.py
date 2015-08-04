# 	match-column-to-call.py

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 	given two documents
# 		columns.txt
# 		call-columns.txt

# 	columns.txt:		two tab separated columns and space separated keys
# 	call-columns.txt:	a longer list of the first column (or not) in columns.txt

# 	will return, in the order of call-columns.txt, the values, or a dash for NO VALUE

# 	ex.	columns.txt:		c	3 welyn
# 							a	1 tree
# 							b	2 nute
# 		call-columns.txt:	c
# 							d
# 							b
# 							a
# 	OUTPUT: c	3 welyn
# 			d	--
# 			b	2 nute
# 			a	1 tree

import sys

call = []
c = open('call-columns.txt','r')
for line in c:
	line = line.strip()
	call.append(line)
print call

column = []
calls = []
lines = []
d = {}
col = open('columns.txt','r')
for line in col:
	line = line.strip()
	section = line.split('\t')
	d[section[0]] = section[1]

col_names = d.keys()
print col_names

notmatched = []
for i in range(0,len(call)):
	if call[i] in col_names:
		print call[i] + "\t" + d[call[i]]
	else:
		print call[i] + "\t--"
		notmatched.append(call[i])

for x in notmatched:
	print x