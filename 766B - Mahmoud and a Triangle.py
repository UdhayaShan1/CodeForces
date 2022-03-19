n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()
flag = 0
for i in range(len(list1)-2):
    a = list1[i]
    b = list1[i+1]
    c = list1[i+2]
    if (a+b) > c:
        if (a+c) > b:
            if (b+c) > a:
                flag+=1
                break
if flag == 0:
    print("NO")
else:
    print("YES")
