x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
x = input().split()
list2 = []
for i in x:
    list2.append(int(i))

set1 = set(list2)
if list1[-1] <= len(set1):
    print("YES")
    final = []
    count = 0
    for i in set1:
        count+=1
        final.append(str(list2.index(i)+1))
        if count == list1[-1]:
            break
    print(' '.join(final))
else:
    print("NO")
