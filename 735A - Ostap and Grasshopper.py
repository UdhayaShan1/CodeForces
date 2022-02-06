x = input().split()
n = int(x[0])
k = int(x[1])
list1 = list(input())

pos_grass = 0
pos_insect = 0
for i in list1:
    if i == 'G':
        pos_grass = list1.index(i)
    elif i == "T":
        pos_insect = list1.index(i)

if pos_insect>pos_grass:
    flag = 0
    for i in range(pos_grass+k,n,k):
        if list1[i] == "T":
            flag += 1
            break
        if list1[i] == "#":
            break
    if flag>0:
        print("YES")
    else:
        print("NO")
else:
    flag = 0
    for i in range(pos_grass-k,-1,-k):
        if list1[i] == "T":
            flag += 1
            break
        if list1[i] == "#":
            break
    if flag>0:
        print("YES")
    else:
        print("NO")
