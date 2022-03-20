n1 = int(input())
x = input().split()
list1 = []
neg = 0
biggest_neg = -1000000000000
zero = 0
pos = 0
for i in x:
    if int(i) < 0:
        neg+=1
    elif int(i) == 0:
        zero+=1
    else:
        pos+=1
    if int(i) < 0 and int(i) > biggest_neg:
        biggest_neg = int(i)
    list1.append(int(i))

if neg % 2 != 0 and zero > 0:
    count = 0
    for i in list1:
        if i < 0:
            count += abs(i - (-1))
        elif i > 0:
            count += (i-1)
        else:
            count += 1
elif neg % 2 != 0 and zero == 0:
    count = 0
    for i in list1:
        if i < 0:
            count += abs(i - (-1))
        elif i > 0:
            count += (i-1)
    count += abs(1 - (-1))
else:
    count = 0
    for i in list1:
        if i < 0:
            count += abs(i - (-1))
        else:
            count += abs(1-i)
print(count)
