n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
 
dp = {}
dp[0] = 1
max1 = 1
for i in range(1,len(list1)):
    if list1[i] > list1[i-1]:
        dp[i] = 1
        dp[i] += dp[i-1]
        if dp[i] > max1:
            max1 = dp[i]
    else:
        dp[i] = 1
print(max1)
