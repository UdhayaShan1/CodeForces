n1 = int(input())
for i in range(n1):
    x = int(int(input())/2)
    if x % 2 != 0:
        print("NO")
    else:
        print("YES")
        temp = []
        count = 2
        sum1 = 0
        for i in range(x):
            sum1+=count
            temp.append(count)
            count+=2
            
        count1 = 1
        sum2 = count1
        for i in range(x-1):
            sum2+=count1
            temp.append(count1)
            count1+=2
            
        temp.append(sum1 - sum2+1)
        print(*temp)
