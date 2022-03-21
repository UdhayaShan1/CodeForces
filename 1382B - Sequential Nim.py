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
    n = list1[k1]
    ref = list2[k1]
    ref = ref[::-1]
    dp = {}
    dp[0] = 1
    for i in range(1,n):
        if ref[i] > 1:
            dp[i] = 1
        else:
            dp[i] = -dp[i-1]
    if dp[n-1] == 1:
        print("First")
    else:
        print("Second")
    k1+=1
    if k1==len(list2):
        break
