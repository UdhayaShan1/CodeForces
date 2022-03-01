n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    m = int(ref[1])
    k = int(ref[2])
    each = n // k
    if m <= each:
        print(m)
    else:
        remainder = m - each
        if remainder % (k-1) == 0:
            print(each - (remainder // (k-1)))
        else:
            print(each - ((remainder//(k-1)) + 1 ))
    k1+=1
    if k1==len(list1):
        break
