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
    a = ref[0]
    b = ref[1]
    if b == 1:
        print("NO")
    else:
        count = 1
        c1 = False
        while c1==False:
            if a != ((a*b*count) - a):
                break
            count+=1
        print("YES")
        print(a,a*b*count-a,a*b*count)
    k1+=1
    if k1==len(list1):
        break
