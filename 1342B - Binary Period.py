n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
 
k1 = 0 
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list(list1[k1])
    if len(set(ref)) == 1:
        print(''.join(ref))
        k1+=1
        continue
    c1 = False
    while c1==False:
        flag = 0
        for i in range(len(ref)-1):
            if ref[i] == ref[i+1] and ref[i] == "1":
                ref.insert(i+1,"0")
                flag+=1
                break
            elif ref[i] == ref[i+1] and ref[i] == "0":
                ref.insert(i+1,"1")
                flag+=1
                break
        if flag == 0:
            break
    print(''.join(ref))
    k1+=1
