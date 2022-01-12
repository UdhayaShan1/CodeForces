n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    total_litre = ref_list[0]
    price_onelitre = ref_list[1]
    price_twolitre = ref_list[-1]
    if total_litre >= 1 and total_litre < 2:
        print(total_litre*price_onelitre)
        k1+=1
        continue
    first_check = total_litre* price_onelitre
    second_check = 0
    sum1 = (total_litre // 2) * price_twolitre
    sum1 = sum1 + (total_litre - (total_litre//2)*2)*price_onelitre
    print(min(first_check,sum1))
    k1+=1
    continue
