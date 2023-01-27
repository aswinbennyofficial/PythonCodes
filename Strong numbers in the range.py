import math
n=input()
lists=[]

for i in range(int(n)+1):
    strngchk=0
    k=str(i)
    for j in range(len(k)):
        strngchk+=math.factorial(int(k[j]))
    if strngchk==int(i):
        lists.append(i)

print(lists)
