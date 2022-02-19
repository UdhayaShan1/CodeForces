n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
 
list2 = list1.copy()
list2.sort()
index = []
 
for i in range(len(list2)):
    if list2[i] != list1[i]:
        index.append(i)
 
if len(index) == 0:
    print("yes")
    print(1,1)
else:
    ref = list1[index[0]:index[-1]+1]
    ref2 = list2[index[0]:index[-1]+1]
    ref = ref[::-1]
    if ref == ref2:
        print("yes")
        print(index[0]+1,index[-1]+1)
    else:
        print("no")
