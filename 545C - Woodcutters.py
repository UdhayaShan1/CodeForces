n1 = int(input())
list1 = []
dp = {}
dp1 = {}
dp2 = {}
for i in range(n1):
    dp[i] = -1
    x = input().split()
    dp1[i] = int(x[0])
    dp2[i] = int(x[1])
 
dp[0] = 1
count = 1

#dp[i] = 1 mean tree already fell to the left, dp [i] = 0 means tree could fall to the right depending on futher check

for i in range(1,n1):
    if dp[i-1] == 1: 
        #prev left fall
        if dp2[i] < (dp1[i]-dp1[i-1]):
            dp[i] = 1
            count += 1
        else:
            dp[i] = 0
    elif dp[i-1] == 0:
        #prev right fall
        if (dp2[i] + dp2[i-1]) < (dp1[i]-dp1[i-1]):
            dp[i-1] = 0
            dp[i] = 1
            count += 2
        elif dp2[i-1] < (dp1[i]-dp1[i-1]):
            dp[i-1] = 0
            count+=1
            dp[i] = 0
        elif dp2[i] < (dp1[i]-dp1[i-1]):
            dp[i] = 1
            count+=1
        else:
            dp[i] = 0
 
if dp[n1-1] == 0:
    count+=1
print(count)
