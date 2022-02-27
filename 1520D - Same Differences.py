import math
n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    y = int(input())
    list1.append(y)
    x = input().split()
    dict1 = {}
    for j in range(y):
        z = int(x[j]) - (j+1)
        if z not in dict1:
            dict1[z] = 1
        else:
            dict1[z] += 1
    list2.append(dict1)


k1 = 0
b1 = False
while b1==False:
    ref = list2[k1]
    count = 0
    for i in ref.values():
        count += math.comb(i,2)
    print(count)
    k1+=1
    if k1==len(list2):
        break
