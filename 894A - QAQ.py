n1 = input()
finalstr = ""
dp = {}
length = 0
index_A = []
for i in n1:
    if i == "Q" or i == "A":
        finalstr+=i
        length+=1
    if i == "A":
        index_A.append(length-1)
 
for i in range(length):
    dp[i] = 0
    
if length > 0:
    if finalstr[0] == "Q":
        dp[0] = 1
    else:
        dp[0] = 0
    
    for i in range(1,length):
        if finalstr[i] == "Q":
            dp[i] += 1
            dp[i] += dp[i-1]
        else:
            dp[i] += dp[i-1]
    
    count = 0
    for i in index_A:
        before = dp[i]
        after = dp[length-1] - dp[i]
        count += before*after
    
    print(count)
else:
    print(0)
