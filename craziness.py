f = open('uniprots.txt','r')
i = open('isoformlist.txt','r')

isoforms = []
for line in i:
	line = line.strip()
	isoforms.append(line)

big_list = []
for line in f:
	line = line.strip()
	big_list.append(line)

for i in range(0,len(big_list)):
	if big_list[i] in isoforms:
		print big_list

for x in big_list: