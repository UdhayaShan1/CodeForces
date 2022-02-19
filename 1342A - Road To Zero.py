n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
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
    ref1 = list1[k1]
    ref2 = list2[k1]
    x = ref1[0]
    y = ref1[1]
    a = ref2[0]
    b = ref2[1]
    count = 0
    if a*2 >= b:
        min1 = min(x,y)
        max1 = max(x,y)
        count += (min1*b)
        max1 -= min1
        min1 -= min1
        count += (max1*a)
    else:
        min1 = min(x,y)
        max1 = max(x,y)
        count += (min1*a + max1*a)
    print(count)
    k1+=1
    if k1==len(list1):
        break
