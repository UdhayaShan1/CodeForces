x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
if sum(list1) % len(list1) != 0 or sum(list1) == 0:
    print(-1)
else:
    print(sum(list1)//len(list1))
