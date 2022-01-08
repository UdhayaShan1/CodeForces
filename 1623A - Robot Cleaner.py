n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

# n, m, rb, cb, rd,     
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    n = ref_list[0]
    m = ref_list[1]
    rb = ref_list[2]
    cb = ref_list[3]
    rd = ref_list[4]
    cd = ref_list[5]
    dr = 1
    dc = 1
    c1 = False
    count = 0
    while c1==False:
        if rb == rd or cb == cd:
            print(count)
            break
        if rb == n:
            dr = -dr
        if cb == m:
            dc = -dc
        rb = rb + dr
        cb = cb + dc
        count+=1
    k1+=1
