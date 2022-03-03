n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    if ref > 45:
        print(-1)
        k1+=1
        continue
    list2 = []
    c1 = False
    start = 9
    while c1==False:
        if ref == 0 or start < 0:
            break
        if ref - start >= 0:
            list2.append(start)
            ref-=start
            start-=1
        else:
            start -= 1
 
    finalstr = ""
    for i in list2:
        finalstr += str(i)
    finalstr = list(finalstr)
    finalstr.sort()
    print(''.join(finalstr))
    k1+=1
