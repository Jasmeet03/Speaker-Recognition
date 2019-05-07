import csv
import os


rootdir = "/home/jasmeet/Desktop/cs project/audio"
for subdir ,dirs , files in os.walk(rootdir):
    os.chdir(subdir)
    for file in files:
        if file.endswith('csv'):
            with open('person.csv') as csvFile:
                reader = csv.reader(csvFile)
                lines = list(reader)
                print(lines[0])
                print(lines[3])
            csvFile.close
