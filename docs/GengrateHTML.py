import os
import csv

dirs=["./images","./av"]
targetfiles=['image.csv','av.csv']
n=len(dirs)
files=list()



for i in dirs:
    temp=os.listdir(i)
    temp_ = [os.path.join(i, filename).replace('\\', '/') for filename in temp]
    files.append(temp_)

for i in range(n):
    with open(targetfiles[i], mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for way in files[i]:
            writer.writerow([way])  
