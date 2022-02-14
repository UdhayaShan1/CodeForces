n1 = int(input())
list1 = []
for i in range(n1):
    temp = []
    x = input().split()
    for j in x:
        temp.append(int(j))
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    multi = 1
    count = 1
    w = ref_list[0]
    h = ref_list[1]
    n = ref_list[-1]
    c1 = False
    while c1==False:
        if multi >= n:
            print("YES")
            break
        if w % 2 == 0:
            w = w // 2
            multi = 2**count
            count+=1
        elif h % 2 == 0:
            h = h // 2
            multi = 2**count
            count+=1
        else:
            if multi >= n:
                print("YES")
            else:
                print("NO")
            break
    k1+=1
    if k1==len(list1):
        break
