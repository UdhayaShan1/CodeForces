n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    remainder_list = []
    list3 = [[],[]]
    for i in ref:
        if i % 2 == 0:
            list3[0].append(i)
        else:
            list3[1].append(i)
    list4 = []
    zero_list3 = list3[0]
    one_list3 = list3[-1]
    for i in zero_list3:
        for j in one_list3:
            if abs(i-j) == 1:
                list4.append([i,j])
 
    left_over_zero = len(list3[0])%2
    left_over_one = len(list3[1])%2
    pairs = (left_over_one + left_over_zero) / 2
    if pairs <= len(list4):
        print("YES")
    else:
        print("NO")   
    k1+=1
    if k1==len(list2):
        break
