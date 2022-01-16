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
    a = ref_list[0]
    b = ref_list[1]
    c = ref_list[2]
    flag = 0
    if ((a+c)/2 % b) == 0 and ((a+c)/2 / b) > 0:
        print("YES")
        k1+=1
        continue
    if (b * 2 - c) % a == 0 and (b * 2 - c) /a > 0:
        print("YES")
        k1+=1
        continue
    if (b*2 - a) % c == 0 and (b*2 - a) / c > 0:
        print("YES")
        k1+=1
        continue
    else:
        print("NO")
        k1+=1
