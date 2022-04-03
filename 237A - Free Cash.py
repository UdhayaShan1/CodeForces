n1 = int(input())
dp = {}
max1 = 1
for i in range(n1):
    x = input()
    if x not in dp:
        dp[x] = 1
    else:
        dp[x] += 1
        if dp[x] > max1:
            max1 = dp[x]
print(max1)
