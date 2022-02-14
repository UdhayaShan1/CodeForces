n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    list2 = []
    start = 1
    for i in range(ref):
        list2.append(2**start)
        start+=1
    sum1 = 0
    count = 0
    for i in list2:
        if count == int(ref/2 - 1):
            break
        sum1+=i
        count+=1
    sum1 += list2[-1]
    print(abs(sum(list2)-sum1 -(sum1)))
    k1+=1
    if k1==len(list1):
        break
