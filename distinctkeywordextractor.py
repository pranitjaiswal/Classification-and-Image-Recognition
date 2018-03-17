import sys

print('Creating labels text file')
file = open('label.txt','a')
for line in sys.stdin:
	link,keywords = line.split('@')
	words = keywords.split(';')
	name=link.split('/')[-1]
	for word in words:
		word = word.strip()
		file.write(word+'\n')

scan = set()
output = open('labels.txt', "w")
for line in open('label.txt', "r"):
    if line not in scan:
        output.write(line)
        scan.add(line)
output.close()
