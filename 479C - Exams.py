n1 = int(input())
list1 = []
dp = {}
for i in range(n1):
    x = input().split()
    ai = int(x[0])
    bi = int(x[1])
    if ai not in dp:
        dp[ai] = []
        dp[ai].append(bi)
    else:
        dp[ai].append(bi)
    dp[ai].sort()

list1 = list(dp.keys())
list1.sort()
first = (dp[list1[0]][-1])
for i in range(1,len(list1)):
    if min(dp[list1[i]]) >= first:
        first = max(dp[list1[i]])
    else:
        first = list1[i]

print(first)
