n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
x = input().split()
list2 = []
for i in x:
    list2.append(int(i))

if sum(list2)<=sum(list1):
    print("Yes")
else:
    print("No")
