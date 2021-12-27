n1 = int(input())
t1 = input().split()
list1 = []
for i in t1:
    list1.append(int(i))
n2 = int(input())
t2 = input().split()
list2 = []
for i in t2:
    list2.append(int(i))

print(max(list2),max(list1))
