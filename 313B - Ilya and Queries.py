n1 = input()
n2 = int(input())
list1 = []
for i in range(n2):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
dp = {}

if n1[0] == n1[1]:
    dp[0] = 1
else:
    dp[0] = 0

for i in range(1,len(n1)-1):
    if n1[i] == n1[i+1]:
        dp[i] = (1+dp[i-1])
    else:
        dp[i] = (0+dp[i-1])
dp[len(n1)-1] = dp[len(n1)-2]+1
dp[-1] = 0

for i in list1:
    a = i[0]-1
    b = i[-1]-1
    print(dp[b-1] - dp[a-1])
