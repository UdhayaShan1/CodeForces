n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    ref_n = listn[k1]
    dp = {}
    max1 = 0
    for i in range(ref_n-1,-1,-1):
        if i not in dp:
            dp[i] = 0
        if ref_list[i]+(i+1) > ref_n:
            dp[i] += ref_list[i]
            if dp[i] > max1:
                max1 = dp[i]
        else:
            dp[i] += (ref_list[i] + dp[i+ref_list[i]])
            if dp[i] > max1:
                max1 = dp[i]
    print(max1)
    k1+=1
    if k1==len(listn):
        break
