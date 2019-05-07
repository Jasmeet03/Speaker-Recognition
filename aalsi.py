import csv
from statistics import mode
from statistics import median
from scipy import stats
import numpy as np
f=open("person.csv","r")
read = csv.reader(f,delimiter = '\t')
for row in read:
	print(row[0])


'''
sum=0
x=0
#arr=[1000]
#i=0
highest_freq=0
lowest_freq=1000
con = 0
data_set=[]
if f.mode=='r':
	for word in f:
		b = word.split(',')
		print (b)
		d = len(b)
		for i in range (d):
			if (b[i] != ' '):
				c=b[i]
				d = c[:18:]
				print(d)
				a = float(d)
				if a!='nan':	
					if a<350:
						data_set.append(a)
						#arr.append[i]=a
						#i=i+1
						sum=sum+a
						x=x+1
						if a>highest_freq:
							highest_freq=a
						elif a<lowest_freq:
							lowest_freq=a
mean=sum/x
means = np.mean(data_set)
median = np.median(data_set)
mode = stats.mode(data_set)
print (means)
print (median)
print (mode)
print("sarthak alsi")
print(mean)
print(highest_freq)
print(lowest_freq)

name=input("enter name: ")
gender=input("enter gender: ")
#csvData = [['Name','Gender','Mean','Median','Mode','Lowest Freq','Highest Freq'],[name,gender,mean,'','',lowest_freq,highest_freq]]
csvData = [[name,gender,mean,lowest_freq,highest_freq]]

with open('Frequency Data.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(csvData)

csvFile.close()
'''
