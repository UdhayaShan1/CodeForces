n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list1 = list1[k1]
    ref_list2 = list2[k1]
    n = ref_list1[0]
    d = ref_list1[1]
    count = 0
    first = ref_list2[0]
    for i in range(len(ref_list2)):
        if ref_list2[i] == 0 or i == 0:
            continue
        temp = ref_list2[i]
        c1 = False
        while c1==False:
            if temp <= 0 or d <= 0 or d < i:
                break
            temp -= 1
            first += 1
            d -= i
    print(first)
    k1+=1
    if k1==len(list1):
        break
