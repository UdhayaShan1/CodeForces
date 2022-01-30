n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    n = listn[k1]
    ref_list = list1[k1]
    ref_list.sort()
    ref_list = ref_list[::-1]
    max1 = 0
    for i in range(len(ref_list)+1):
        min1 = min(i,ref_list[i-1])
        if min1 > max1:
            max1 = min1
    print(max1)
    k1+=1
    if k1==len(list1):
        break
