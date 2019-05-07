import os


root_dir = '/home/jasmeet/Desktop/cs project/test'
file1 = open('testsamplepath.txt','w')
for subdir , dirs , files in os.walk(root_dir):
    for file in files:
        if file.endswith('wav'):
            sp = subdir.split('/')[-1]
            print (sp)
            file1.write(subdir+'/'+file+'\n')
