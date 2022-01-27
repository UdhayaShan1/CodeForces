n1 = int(input())
temp1 = n1
temp2 = n1
b1 = False
count1 = 0
while b1==False:
    if str(temp1)[-1] == "0":
        break
    temp1+=1
    count1+=1
count2 = 0
while b1==False:
    if str(temp2)[-1] == "0":
        break
    temp2-=1
    count2+=1

if count1 >= count2:
    print(temp2)
else:
    print(temp1)

    
