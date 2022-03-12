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
    if k1==len(list1):
        break
    n = listn[k1]
    ref_list = list1[k1]
    if len(set(ref_list)) == 1:
        print(-1)
        k1+=1
        continue
    max1 = max(ref_list)
    index_max = [i for i, x in enumerate(ref_list) if x == max1]
    final = -1
    for i in index_max:
        if i == 0:
            if ref_list[1] != ref_list[i]:
                final = 0
                break
        elif i == n-1:
            if ref_list[-2] != ref_list[-1]:
                final = n-1
                break
        else:
            if ref_list[i-1] != ref_list[i]:
                final = i
                break
            if ref_list[i+1] != ref_list[i]:
                final = i
                break
    print(final+1)
    k1+=1
