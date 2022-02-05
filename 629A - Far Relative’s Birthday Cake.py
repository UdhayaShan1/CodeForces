import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
sum1=0

def ncr(no1):
    if no1 <=1:
        return 0
    return (math.factorial(no1) / (2*math.factorial(no1-2)))
    

for i in list1:
    no_c = 0
    for j in i:
        if j == "C":
            no_c+=1
    
    sum1 += ncr(no_c)
    
k1 = 0
b1 = False
while b1==False:
    no_c = 0
    for i in range(n1):
        if list1[i][k1] == "C":
            no_c+=1
    sum1 += ncr(no_c)
    k1+=1
    if k1==len(list1):
        break

print(int(sum1))
