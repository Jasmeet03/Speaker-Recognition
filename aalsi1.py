import csv
from statistics import mode
from statistics import median
from scipy import stats
import numpy as np
import os

rootdir="/home/jasmeet/Desktop/cs project/audio"
for subdir,dirs,files in os.walk(rootdir):
	for file in files:
		if file.endswith('csv'):
			try:
				if (file=='person.csv'):
					f=open("person.csv","r")
					read = csv.reader(f,delimiter = '\t')
					for row in read:
						print(row)
			except:
				continue



