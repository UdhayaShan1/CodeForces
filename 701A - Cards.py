n1 = int(input()) /2
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

each = sum(list1) / n1

b1 = False
count = 0
k1 = 0
not_tocheck = []
while b1==False:
    remainder = each - list1[k1]
    index_next = 0
    for i in range(len(list1)):
        if list1[i] == remainder and i != k1:
            if i not in not_tocheck:
                index_next = i
                not_tocheck.append(k1)
                not_tocheck.append(i)
                break
    c1 = False
    print(k1+1,index_next+1)
    while c1==False:
        k1+=1
        if k1 not in not_tocheck:
            break
    if k1>=len(list1):
        break
