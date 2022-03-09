n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input())
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref1 = list1[k1]
    ref2 = list2[k1]
    if len(ref1) > len(ref2):
        temp1 = ref1
        temp2 = ref2
        ref1 = temp2
        ref2 = temp1
    c1 = False
    start = 1
    while c1==False:
        flag = -1
        ref = ref1[0:start]
        if len(ref1) % len(ref) == 0:
            count = 0
            for i in range(0,len(ref1),len(ref)):
                if ref1[i:i+len(ref)] == ref:
                    count+=1
            if count == (len(ref1) // len(ref)):
                flag = ref
                break
        start += 1
        if start == len(ref1)+1:
            break
    if flag == -1:
        print(-1)
    else:
        if len(ref2) % len(flag) == 0:
            count = 0
            for i in range(0,len(ref2),len(flag)):
                if ref2[i:i+len(flag)] == flag:
                    count+=1
            if count == (len(ref2) // len(flag)):
                min1 = len(ref1) // len(flag)
                min2 = len(ref2) // len(flag)
                min_final = min(min1,min2)
                max_final = max(min1,min2)
                d1 = False
                start = 1
                while d1==False:
                    if (min_final * start) % max_final == 0:
                        print(start * min_final*flag)
                        break
                    start += 1
                    
            else:
                print(-1)
        else:
            print(-1)
    k1+=1
