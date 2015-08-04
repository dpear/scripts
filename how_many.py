#	how_many.py
#
#	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	given 'text.txt'
#	will print:
#		total number of lines inputted
#		number of unique lines





f = open('text.txt','r')

lines = []
for line in f:
	line = line.strip()
	lines.append(line)

print len(lines)
lines = set(lines)
print len(lines)
# final = []
# for i in range (0, len(lines)):
# 	if lines[i] == lines [i-1]:
# 		pass
# 	else:
# 		final.append(lines[i])

# fil = open('final.txt','w')
# fil.write(str(len(lines)))