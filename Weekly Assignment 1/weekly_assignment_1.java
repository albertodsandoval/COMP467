import random

numlist = []
max = 0;
for x in range(25):
    numlist.append(random.randint(0,100))
    if(numlist[x]>max):
        max = numlist[x]
print("List: ",numlist)
print("Max number: ",max)