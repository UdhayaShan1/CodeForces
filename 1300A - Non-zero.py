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
    if k1==len(list1):
        break
    ref_n = list1[k1]
    ref_list = list2[k1]
    sum1 = 0
    product1 = 1
    zero_count = 0
    for i in ref_list:
        sum1 +=i
        product1 = product1 * i
        if i == 0:
            zero_count+=1
    if sum1 != 0 and product1 != 0:
        print(0)
        k1+=1
        continue
    
    if sum1 ==0 and product1 != 0:
        print(1)
        k1+=1
        continue
    
    
    
    if sum1 + zero_count == 0:
        print(zero_count+1)
    else:
        print(zero_count)
    k1+=1
    
