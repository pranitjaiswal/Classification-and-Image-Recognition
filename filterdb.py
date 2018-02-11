import sys
import csv


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

with open(sys.argv[1],'rb') as f:
	reader=csv.reader(f)
	i=0
	for row in reader:
		if row[2] !='False':
			if 'India' in '+'.join(row):
				if not('United' in row[31]):
					url=find_between('+'.join(row), 'http','+')
					print(row[0]+';'+url)
					#i=i+1
#print(i)


