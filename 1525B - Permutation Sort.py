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
    n = list1[k1]
    ref = list2[k1]
    ops = 0
    ref_temp = ref.copy()
    ref_temp.sort()
    if ref == ref_temp:
        print(0)
    else:
        c1 = False
        while c1==False:
            pos_one = [i for i, x in enumerate(ref) if x == 1][0]
            if pos_one == 0:
                break
            if pos_one != (n-1):
                ref1 = ref[0:n-1]
                ref2 = ref[n-1:]
                ref1.sort()
                ref = ref1 + ref2
                ops+=1
            else:
                ref1 = ref[1:n]
                ref2 = ref[n:]
                ref1.sort()
                ref = [ref[0]] + ref1 + ref2
                ops+=1
                
        ref_temp = ref.copy()
        ref_temp.sort()
        if ref == ref_temp:
            print(ops)
        else:
            print(ops+1)
        
    k1+=1
    if k1==len(list1):
        break
