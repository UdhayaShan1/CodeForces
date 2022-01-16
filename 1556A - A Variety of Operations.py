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
    c = ref_list[0]
    d = ref_list[1]
    if c==d:
        if c == 0:
            print(0)
        else:
            print(1)
        k1+=1
        continue
    if (c+d) % 2 == 0:
        print(2)
        k1+=1
        continue
    print(-1)
    k1+=1
