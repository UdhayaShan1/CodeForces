n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
list_inside = []
for i in list1:
    if i in list_inside:
        print("YES")
    else:
        print("NO")
        list_inside.append(i)
