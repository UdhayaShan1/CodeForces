n1 = int(input())
x = input().split()
list1 = []
for j in x:
    list1.append(int(j))

b1 = False
while b1==False:
    count = 0
    for i in list1:
        count+=1
        if len([j for j, x in enumerate(list1) if x == i]) > 1:
            c1 = False
            while c1==False:
                list1.remove(i)
                if len([k for k, x in enumerate(list1) if x == i]) == 1:
                    break
            break
    if count == len(list1):
        break

print(len(list1))

listfinal = []
for i in list1:
    listfinal.append(str(i))
print(' '.join(listfinal))
           
