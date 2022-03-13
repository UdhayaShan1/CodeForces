n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
twofive_list = []
for i in range(0,16):
    twofive_list.append(2050*(10**i))
 
twofive_list = twofive_list[::-1]
 
b1 = False
k1 = 0
while b1==False:
    ref = list1[k1]
    count = 0
    c1 = False
    flag = 0
    while c1==False:
        for i in twofive_list:
            if ref >= i:
                temp_div = ref // i
                count += temp_div
                ref = ref % i
                break
        if ref == 0:
            flag+=1
            break
        if ref < (2050):
            flag = 0
            break
    if flag == 1:
        print(count)
    else:
        print(-1)
    k1+=1
    if k1==len(list1):
        break
