n1 = input()
dp = {}
for i in n1:
    if i not in dp:
        dp[i] = 1
    else:
        dp[i] += 1
 
count = 0
for i in dp.values():
    if i % 2 !=0 :
        count+=i
if count == 0:
    print("First")
else:
    if (count) % 2 == 0:
        print("Second")
    else:
        print("First")
