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
    ref_list = list1[k1]
    a = ref_list[0]
    b = ref_list[1]
    c = ref_list[2]
    c1 = False
    count = 0
    while c1==False:
        if b < 1 or c < 2:
            break
        b-=1
        c-=2
        count+=3
    d1 = False
    while d1==False:
        if b < 2 or a < 1:
            break
        b-=2
        a-=1
        count+=3
    print(count)
    k1+=1
    if k1==len(list1):
        break
