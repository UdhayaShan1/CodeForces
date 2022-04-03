n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    min1 = 1000000000
    count = 0
    for i in range(n-1,-1,-1):
        if ref[i] <= min1:
            min1 = ref[i]
        else:
            count+=1
    print(count)
    k1+=1
    if k1==len(list1):
        break
