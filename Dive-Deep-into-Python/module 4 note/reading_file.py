filePath = 'reading.txt'
with open(filePath,'r') as file:
    content = file.read()

input = content.strip().split()
for x in input:
    print(x,end =" ")

import os
os.rename('reading.txt','data.txt')