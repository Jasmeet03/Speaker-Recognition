import csv
from statistics import mode
from statistics import median
from scipy import stats
import numpy as np
import re





rows = []
data_set = []
tr = [10]
highest_freq=0
lowest_freq=1000
n = 0
f=open("person.csv","r")
size=0
read = csv.reader(f,delimiter = ',')
for row in read:
	rows.append(row)
	size+=1
size-=1

while(n <= 10):
	n = n+1
	data_set = []
	for row in rows[n:n+1]:
		for r in row :
			b = r.split(',')
			d = len(b)
			for i in range (d):
				#print(d)
				if(b[i] != ' '):
					c = b[i]
					e = c[:18:]
					a = float(e)
					if (a!='nan' and a < 350):
						#print(a,i,n)
						data_set.append(a)
						#print (data_set)
						if a>highest_freq:
							highest_freq=a
						elif a<lowest_freq:
							lowest_freq=a

	tr.append(data_set)		
'''
sum1=np.zeros(size, dtype = int)
row=[[]*size]
count=np.zeros(size, dtype = int)
avg=np.zeros(size, dtype = int)
h=0
col=0
for r in rows:
	for i in r:
		col+=1	
		if re.match("^\d+?\.\d+?$", i):
			a=float(i)		
			print(a)
		if(col!=496):
			h+=1
		print(h)			
		for i in r:
			print(i)	
			if i.isdigit():
				sum1[h]+=float(i)
				count[h]+=1
				print(i)
				avg[h]=sum1[h]/count[h]'''

#print (data_set)
for i in range (10):
	print (tr[i])
	print ('\n')
	print(np.mean(tr[i]))
	print(np.median(tr[i]))
	print(stats.mode(tr[i]))

