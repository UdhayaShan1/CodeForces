n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())

k1 = 0
b1 = False
while b1==False:
    str1 = list1[k1]
    dp = {}
    if str1[0] == "0":
        dp[0] = 0
    else:
        dp[0] = 1
    list2 = []
    for i in range(1,len(str1)):
        if str1[i] == "1":
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 0
            list2.append(dp[i-1])
    if dp[len(str1)-1] > 0:
        list2.append(dp[len(str1)-1])
    list2.sort()
    list2 = list2[::-1]
    c1 = False
    while c1==False:
        if 0 not in list2:
            break
        list2.remove(0)

    if len(list2) == 0:
        print(0)
    else:
        count = 0
        for i in range(0,len(list2),2):
            count += list2[i]
        print(count)
    
    k1+=1
    if k1==len(list1):
        break
