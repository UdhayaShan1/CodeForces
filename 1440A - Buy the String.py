n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    temp = []
    x = input().split()
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    list2.append((input()))

k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    ref_str = list2[k1]
    n = ref_list[0]
    h = ref_list[-1]
    c0 = min(ref_list[1],ref_list[2]+h)
    c1 = min(ref_list[2],ref_list[1]+h)
    count = 0
    for i in ref_str:
        if i == "0":
            count += c0
        else:
            count+= c1
    print(count)
    k1+=1
    if k1==len(list1):
        break
