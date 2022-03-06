n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    list2.append([])
    for j in range(temp[0]):
        list2[i].append(input())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    ref1 = list2[k1]
    n = ref[0]
    m = ref[1]
    x = ref[2]
    y = ref[3]
    if x*2 <= y:
        count = 0
        for i in ref1:
            count += len([j for j, x in enumerate(i) if x == "."])
        print(count * x)
    else:
        count = 0
        for i in ref1:
            count_two = 0
            count_one = 0
            dp = {}
            if i[0] == ".":
                dp[0] = 1
            else:
                dp[0] = 0
            
            for j in range(1,len(i)):
                if i[j] == "*":
                    dp[j] = 0
                elif i[j] == "." and i[j-1] == "." and dp[j-1] == 1:
                    dp[j] = 2
                    dp[j-1] = 0
                else:
                    dp[j] = 1
            
            for z in dp.values():
                if z == 2:
                    count_two+=1
                elif z == 1:
                    count_one+=1
 
            count += (count_two * y + count_one * x)
        print(count)
 
    k1+=1
    if k1==len(list2):
        break
