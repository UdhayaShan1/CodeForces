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
    if k1==len(listn):
        break
    ref_n = listn[k1]
    ref_list = list1[k1]
    ref_list.sort()
    max1 = max(ref_list)
    if min(ref_list) < 0:
        print("NO")
        k1+=1
        continue
    else:
        print("YES")
        print(len(list(range(0,max(ref_list)+1))))
        x=(list(range(0,max(ref_list)+1)))
        final = []
        for i in x:
            final.append(str(i))
        print(' '.join(final))
        k1+=1
        continue
