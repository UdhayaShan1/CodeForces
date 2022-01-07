n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ki = list1[k1]
    si = list(list2[k1])
    c1 = False
    count = 0
    while c1==False:
        flag = 0
        to_skip = []
        for i in range(len(si)):
            if i != len(si)-1:
                if i not in to_skip:
                    if si[i] == "A":
                        if si[i+1] == "P":
                            si[i+1] = "A"
                            flag+=1
                            to_skip.append(i+1)
        
        if flag == 0:
            print(count)
            break
        count+=1
    k1+=1
    
