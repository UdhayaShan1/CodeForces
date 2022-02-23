n1 = list(input())
count = 0
count1 = 0
count2 = 0
count3 = 0
flag = 0
b1 = False
for i in range(len(n1)):
    
    if n1[i:i+3] == ["A","B","A"] or n1[i:i+3] == ["B","A","B"]:
        if flag == 0:
            count3 += 1
            n1[i] = "P"
            n1[i+2] = "P"
            flag+=1
    elif n1[i:i+2] == ["A","B"]:
        count1+=1
    elif n1[i:i+2] == ["B","A"]:
        count2+=1
 
if count1 > 0 and count2 >0:
    print("YES")
elif count3 > 0 and (count1+count2) > 0:
    print("YES")
else:
    print("NO")
