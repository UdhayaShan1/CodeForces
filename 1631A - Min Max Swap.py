n1 = int(input())
list1 = []
list2 = []
listn = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    refn = listn[k1]
    ref1 = list1[k1]
    ref2 = list2[k1]
    start = 0
    c1 = False
    max1 = 0
    max2 = 0
    while c1==False:
        if ref1[start] > ref2[start]:
            temp1 = ref1[start]
            temp2 = ref2[start]
            ref1[start] = temp2
            ref2[start] = temp1
        start += 1
        if start == refn:
            break
    print(max(ref1)*max(ref2))
    k1+=1
    if k1==len(list2):
        break
