x = input().split()
amount = int(x[0])
x = x[1:]
temp = []
for i in x:
    temp.append(int(i))
list1 = temp.copy()

dp = {}
dp[0] = 0
for i in range(1,min(list1)):
    dp[i] = -1

for i in range(min(list1),amount+1):
    temp = []
    for j in list1:
        if i>=j:
            remainder = i-j
            if dp[remainder] == -1:
                temp.append(-1)
            else:
                temp.append(dp[remainder]+1)
    dp[i] = max(temp)

print(dp[amount])
