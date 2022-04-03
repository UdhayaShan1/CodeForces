x = input().split()
n = int(x[0])
q = int(x[1])
str1 = input()
 
dp = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
dp[0] = 0
dp[1] = ([i for i, x in enumerate(alpha) if x == str1[0]][0]+1)
 
for i in range(2,n+1):
    dp[i] = [j for j, x in enumerate(alpha) if x == str1[i-1]][0]+1 + dp[i-1]
 
 
for i in range(q):
    query = input().split()
    print(dp[int(query[1])] - dp[int(query[0])-1])
