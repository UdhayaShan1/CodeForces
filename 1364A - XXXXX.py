n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input().split())
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1 == False:
    if k1 == len(list1):
        break
    ref1 = list1[k1]
    n = int(ref1[0])
    x = int(ref1[1])
    ref2 = list2[k1]
    if sum(ref2) % x != 0:
        print(n)
        k1 += 1
        continue
    test1 = 0
    count1 = 0
    for i in ref2:
        test1 += i
        count1 += 1
        if test1 % x != 0:
            break
    ref3 = ref2.copy()
    ref3 = ref3[::-1]
    test2 = 0
    count2 = 0
    for i in ref3:
        test2 += i
        count2 += 1
        if test2 % x != 0:
            break
    if n - min(count1,count2) == 0:
        print(-1)
    else:
        print(n-min(count1,count2))
    k1 += 1
