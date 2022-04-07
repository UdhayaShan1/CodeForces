n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(int(input()))
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)
    temp = []
    for j in input().split():
        temp.append(int(j))
    list3.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref1 = list2[k1]
    ref2 = list3[k1]
    dp = {}
    flag = 0
    for i in range(n):
        if ref1[i] != ref2[i]:
            diff = ref2[i] - ref1[i]
            if diff > 0:
                if 1 not in dp:
                    flag+=1
                    break
            elif diff == 0:
                if 0 not in dp:
                    flag+=1
                    break
            else:
                if -1 not in dp:
                    flag+=1
                    break
        dp[ref1[i]] = 1
    if flag==1:
        print("NO")
    else:
        print("YES")
    k1+=1
    if k1==len(list1):
        break
