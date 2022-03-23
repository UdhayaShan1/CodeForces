n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1]
    ref = list2[k1]
    if n == 1:
        print("YES")
        k1+=1
        continue
    if len(set(ref)) == 1 and 0 in ref:
        print("NO")
        k1+=1
        continue
    start = 1
    min1 = 0
    c1 = False
    while c1==False:
        to_carry = ref[start-1] - min1
        ref[start] += to_carry
        ref[start-1] = min1
        min1+=1
        start+=1
        if ref[start-1] < min1:
            break
        if start == n:
            break
    count = 0
    for i in range(1,n):
        if ref[i] > ref[i-1]:
            count+=1
    if count == (n-1):
        print("YES")
    else:
        print("NO")
    k1+=1
