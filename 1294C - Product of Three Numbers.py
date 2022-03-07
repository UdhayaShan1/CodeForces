n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    list2 = []
    c1 = False
    dp = {}
    start = 2
    while c1==False:
        if ref % start == 0:
            if start not in dp:
                dp[start] = 1
            else:
                dp[start] += 1
            ref = ref // start
        else:
            start += 1
        if start == int(ref**0.5)+1:
            break
        if ref<2:
            break
    for i,j in dp.items():
        start = 1
        d1 = False
        while d1==False:
            list2.append(i**start)
            dp[i] -= start
            start += 1
            if dp[i] < start:
                break
    if len(list2) >= 2:
        if int((list1[k1]) / (list2[0]*list2[1])) == list2[0] or int((list1[k1]) / (list2[0]*list2[1])) == list2[1]:
            print("NO")
        else:
            if int((list1[k1]) / (list2[0]*list2[1])) == 1:
                print("NO")
            else:
                print("YES")
                print(list2[0],list2[1],int((list1[k1]) / (list2[0]*list2[1])))
               
    else:
        print("NO")
    k1+=1
    if k1==len(list1):
        break
