#	overlap.py
#
#	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	takes two documents (in this case SGD.txt and marc.txt)
#	prints which items are in both and which are different




# 	output should be:
#	individual lists of all
#	in SGD's list only: (number)
#	in both SGD and Marc: (number)
#	in Marc onle: (number)


s = open('ohcrap.txt','r')
SGD = []
for line in s:
	line = line.strip()
	SGD.append(line)

SGD = set(SGD)
arrSGD = []
for x in SGD:
	arrSGD.append(x)


m = open('noncomp-mgi.txt','r')
marc = []
for line in m:
	line = line.strip()
	marc.append(line)

marc = set(marc)
arrmarc = []
for x in marc:
	arrmarc.append(x)

both = []
marconly = []
SGDonly = []
for i in range (0,len(arrmarc)):
	if arrmarc[i] in SGD:
		both.append(arrmarc[i])
	else:
		marconly.append(arrmarc[i])
for i in range(0,len(arrSGD)):
	if arrSGD[i] in arrmarc:
		pass
	else:
		SGDonly.append(arrSGD[i])	

print "ohcrap:"
for x in SGDonly:
	print x
print "\nboth:"
for x in both:
	print x
print "\nentrez only:"
for x in marconly:
	print x
print "52 only: " + str(len(SGDonly))
print "both: " + str(len(both))
print "entrez only: " + str(len(marconly))

