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
    ref = list1[k1]
    n = ref[0]
    k = ref[1]
    if n % k == 0:
        print("YES")
        print(*([n//k]*k))
    else:
        if n % 2 == 0:
            if k % 2 != 0:
                ref1 = n - (k-1)*2
                if ref1 % 2 != 0 or ref1 <= 0:
                    print("NO")
                else:
                    list2 = [2] * (k-1)
                    list2.append(n- 2 *(k-1))
                    print("YES")
                    print(*list2)
            else:
                ref1 = n - (k-1)
                if ref1 <= 0 or ref1 % 2 == 0:
                    print("NO")
                else:
                    list2 = [1]*(k-1)
                    list2.append(n - (k-1))
                    print("YES")
                    print(*list2)
        else:
            if k % 2 == 0:
                print("NO")
            else:
                ref1 = n - (k-1)
                if ref1 % 2 == 0 or ref1 <= 0:
                    print("NO")
                else:
                    list2 = [1]*(k-1)
                    list2.append( n - (k-1))
                    print("YES")
                    print(*list2)
    k1+=1      
