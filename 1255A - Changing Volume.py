n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
list2 = [5,2,1]
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    a = ref_list[0]
    b = ref_list[1]
    diff = abs(a-b)
    count = 0
    for i in list2:
        if diff < i:
            continue
        count += diff // i
        diff = diff % i
        continue
    print(count)
    k1+=1
    if k1==len(list1):
        break
