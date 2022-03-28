n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    temp.sort()
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    ref = ref[::-1]
    dp = {}
    count = 0
    for i in range(n):
        if ref[i] + 1 not in dp:
            dp[ref[i]+1] = 1
            count += 1
            continue
        if ref[i] not in dp:
            dp[ref[i]] = 1
            count+=1
            continue
    print(count)
    k1+=1
    if k1==len(list2):
        break
