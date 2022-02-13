x = input().split()
length = int(x[0])
sum1 = int(x[1])
og_length = length
og_sum1 = sum1

b1 = False
list1 = []
c1 = False

while b1==False:
    start = 1
    c1 = False
    while c1==False:
        if len(list1) == og_length:
            break
        if sum1 == 0:
            list1.append(0)
            continue
        remainder = (length-1) * 9
        if sum1 - start <= remainder:
            list1.append(start)
            sum1-=start
            length -= 1
            start = 0
            continue
        start+=1
    if len(list1) == og_length:
        break

length = og_length
sum1 = og_sum1

b1 = False
list2 = []
while b1==False:
    start = 9
    while c1==False:
        if len(list2) == og_length:
            break
        if sum1 == 0:
            list2.append(0)
            continue
        remainder = (length-1) * 9
        if (sum1 - start) <= remainder and (sum1-start) >= 0:
            list2.append(start)
            length-=1
            sum1 -= start
            start = 9
            continue
        start -= 1
        if start < 0:
            break
    if len(list2) == og_length:
        break
    if start < 0:
        break

flag = 0
no_zero = 0
for i in list1:
    if i > 9 :
        flag+=1
        break
    if i == 0:
        no_zero += 1
        continue
if flag > 0:
    print(-1,-1)
elif no_zero == og_length and og_sum1 != 0:
    print(-1,-1)
elif no_zero == og_length and og_length>1:
    print(-1,-1)
else:
    if len(list2) == 0:
        print(-1,-1)
    else:
        list3 = []
        list4 = []
        for i in list1:
            list3.append(str(i))
        for i in list2:
            list4.append(str(i))
        print(''.join(list3),''.join(list4))
