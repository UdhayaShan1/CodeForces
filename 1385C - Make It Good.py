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
    if k1==len(list2):
        break
    ref_n = list1[k1]
    ref_list = list2[k1]
    if len(set(ref_list)) == 1:
        print(0)
        k1+=1
        continue
    c1 = False
    start = ref_n-1
    while c1==False:
        if ref_list[start-1] < ref_list[start] or start == 0:
            break
        start-=1
    d1 = False
    while d1==False:
        if ref_list[start-1] > ref_list[start] or start == 0:
            break
        start-=1
    print(start)
    k1+=1
