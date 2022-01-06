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
    n = ref_list[0]
    k = ref_list[-1]
    max1 = 0
    if n <=1:
        max1 = 0
        if k <= max1:
            print(*list(range(1,n+1)))
        else:
            print(-1)
        k1+=1
        continue
    elif n % 2 == 0:
        temp1 = ((n-2) / (2))+1
        max1 = 0 + (temp1-1)*(1)
        if k > max1:
            print(-1)
            k1+=1
            continue
        else:
            c1 = False
            temp2 = (list(range(1,n+1)))
            k2 = 2
            count = 0
            while c1==False:
                if count == k:
                    break
                if k2==len(temp2):
                    break
                temp_digit = temp2[k2]
                temp_digit2 = temp2[k2-1]
                temp2[k2] = temp_digit2
                temp2[k2-1] = temp_digit
                k2+=2
                count += 1
                
                
            print(*temp2)
            k1+=1
            continue
    else:
        temp1 = (((n-1)/2)+1)
        max1 = 0 + (temp1-1)*(1)
        if k > max1:
            print(-1)
            k1+=1
            continue
        else:
            d1 = False
            temp2 = (list(range(1,n+1)))
            k2 = 2
            count = 0
            while d1==False:
                if count == k:
                    break
                if k2==len(temp2)+1:
                    break
                temp_digit = temp2[k2]
                temp_digit2 = temp2[k2-1]
                temp2[k2] = temp_digit2
                temp2[k2-1] = temp_digit
                count+=1
                k2+=2
                
            print(*temp2)
            k1+=1
            continue
