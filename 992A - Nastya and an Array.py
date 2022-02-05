n1 = int(input())
x = input().split()
list1 = []
for i in x:
    if int(i) == 0:
        continue
    list1.append(int(i))

count = len(set(list1))

print(count)
