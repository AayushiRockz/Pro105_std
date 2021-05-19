import csv
import math

with open("105Data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

print(file_data)
data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data :
        total += int(i) 
    mean = total/n
    return mean
    
sqr_list = []

for num in data:
    a = int(num)-mean(data)
    a = a**2
    sqr_list.append(a)

sum = 0

for x in sqr_list:
    sum += x

result = sum/(len(data)-1)

sd = math.sqrt(result)
print("SD is :"+str(sd))





