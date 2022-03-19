n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
dp = {}
dp[6] = 15
dp[8] = 20
dp[10] = 25
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    flag = 0
    for i in list(dp.keys()):
        if ref % i == 0:
            print(ref//i * dp[i])
            flag += 1
            break
    if flag == 1:
        k1+=1
        continue
    if ref <= 5:
        print(15)
        k1+=1
        continue
    max1 = 100000000000000000000000000000
    temp = [6,8,10]
    for i in temp:
        count = 0
        count += (ref//i * dp[i])
        remainder = ref % i
        if remainder == 9 or remainder == 10:
            count += dp[10]
        elif remainder == 7 or remainder == 8:
            count += dp[8]
        else:
            count += dp[6]
        if count < max1:
            max1 = count
        
        count2 = 0
        count2 += (ref//i - 1)*(dp[i])
        remainder = ref - (ref//i -1)*i
        if remainder <= 10:
            if remainder == 9 or remainder == 10:
                count2 += dp[10]
            elif remainder == 7 or remainder == 8:
                count2 += dp[8]
            else:
                count2 += dp[6]
            if count2 < max1:
                max1 = count2
        else:
            continue
        
        
    print(max1)
    k1+=1
