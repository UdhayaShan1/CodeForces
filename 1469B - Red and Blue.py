n1 = int(input())
list1 = []
list2 = []
list3 = []
list4 = []
for i in range(n1):
    list1.append(int(input()))
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)
    list3.append(int(input()))
    temp = []
    for j in input().split():
        temp.append(int(j))
    list4.append(temp)

k1 = 0
b1 = False
while b1==False:
    n = int(list1[k1])
    ref_1 = list2[k1]
    m = int(list3[k1])
    ref_2 = list4[k1]
    dp1 = {}
    max1 = 0
    dp1[0] = ref_1[0]
    if dp1[0] > max1:
        max1 = dp1[0]
    for i in range(1,n):
        dp1[i] = ref_1[i]+dp1[i-1]
        if dp1[i] > max1:
            max1 = dp1[i]

    dp2 = {}
    max2 = 0
    dp2[0] = ref_2[0]
    if dp2[0] > max2:
        max2 = dp2[0]
    for i in range(1,m):
        dp2[i] = ref_2[i]+dp2[i-1]
        if dp2[i] > max2:
            max2 = dp2[i]
    print(max1+max2)
    k1+=1
    if k1==len(list1):
        break
