p = open('with-isoforms-noncomp.txt','r')

lines = []
for line in p:
	oneline = []
	line = line.strip()
	oneline = line.split("\t")
	lines.append(oneline)

q = open('first-column.txt','w')
for i in range(0,len(lines)):
	q.write(lines[i][2]+"\n")

