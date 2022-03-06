n1 = input()
dp = {}
flag = 0
go_ahead = 0
if n1[0] == "1":
    dp[0] = 2
else:
    print("NO")
    go_ahead+=1
if go_ahead == 0:
    for i in range(1,len(n1)):
        if n1[i] == "1":
            dp[i] = 2
        elif n1[i] == "4":
            dp[i] = dp[i-1] - 1
            if dp[i] < 0:
                flag+=1
                break
        else:
            flag+=1
            break
    if flag > 0:
        print("NO")
    else:
        print("YES")
