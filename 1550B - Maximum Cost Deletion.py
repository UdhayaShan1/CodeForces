n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    list1.append(x)
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    n1 = list1[k1]
    ref = list2[k1]
    n = int(n1[0])
    a = int(n1[1])
    b = int(n1[2])
    if (a+b)*n >= (a*n)+b:
        print((a+b)*n)
    else:
        dp = {}
        check = []
        if ref[0] == "0":
            dp[0] = 1
        else:
            dp[0] = 0
        for i in range(1,n):
            if ref[i] == "0" and i != n-1:
                dp[i] = dp[i-1] + 1
            if ref[i] == "0" and i == n-1:
                dp[i] = dp[i-1] + 1
                check.append(dp[i])
            if ref[i] == "1":
                dp[i] = 0
                if dp[i-1] > 0:
                    check.append(dp[i-1])
                continue
 
        count1 = 0
        for i in check:
            count1 += (a*i) + b
        count1 += (a * len([i for i, x in enumerate(ref) if x == "1"]) + b)
        
        dp = {}
        check = []
        if ref[0] == "1":
            dp[0] = 1
        else:
            dp[0] = 0
        for i in range(1,n):
            if ref[i] == "1" and i != n-1:
                dp[i] = dp[i-1] + 1
            if ref[i] == "1" and i == n-1:
                dp[i] = dp[i-1] + 1
                check.append(dp[i])
            if ref[i] == "0":
                dp[i] = 0
                if dp[i-1] > 0:
                    check.append(dp[i-1])
                continue
 
        count2 = 0
        for i in check:
            count2 += (a*i) + b
        count2 += (a * len([i for i, x in enumerate(ref) if x == "0"]) + b)
        print(max(count1,count2))
     
    k1+=1
    if k1==len(list1):
        break
