from math import comb
n1 = int(input())
x = input().split()
list1 = []
max1 = 0
min1 = 100000000000000000000
for i in x:
    max1 = max(int(i),max1)
    min1 = min(int(i),min1)
    list1.append(int(i))
count1 = 0
count2 = 0

if max1 != min1:
    for i in list1:
        if i == max1:
            count1+=1
        elif i == min1:
            count2+=1
    print(max1-min1,count2*count1)
else:
    for i in list1:
        if i == max1:
            count1+=1
        elif i == min1:
            count2+=1
    print(0,comb(count1,2))
