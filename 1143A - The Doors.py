n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

zero = 0
one = 0
for i in list1:
    if i == 0:
        zero+=1
    else:
        one+=1

zero_start = 0
one_start = 0
count = 0
for i in list1:
    count+=1
    if i == 0:
        zero_start+=1
    else:
        one_start+=1
    if zero_start >= zero:
        print(count)
        break
    if one_start >= one:
        print(count)
        break
