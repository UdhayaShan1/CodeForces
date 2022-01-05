n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        temp = list1[i]
        list1[i] = temp-1
    
final = []
for i in list1:
    final.append(str(i))
print(' '.join(final))
