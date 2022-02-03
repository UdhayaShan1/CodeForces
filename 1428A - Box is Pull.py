n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    x1 = ref[0]
    y1 = ref[1]
    x2 = ref[2]
    y2 = ref[3]
    count = 0
    horizontal = abs(x2-x1)
    vertical = abs(y2-y1)
    if horizontal != 0 and vertical != 0:
        count = horizontal + vertical + 2
    else:
        count = horizontal + vertical
    print(count)
    k1+=1
    if k1==len(list1):
        break
