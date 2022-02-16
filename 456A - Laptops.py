x = int(input())
list1 = []
list2 = []
for i in range(x):
    y = input().split()
    list1.append(int(y[0]))
    list2.append(int(y[1]))

dict1 = dict(zip(list1,list2))
list1.sort()
flag = 0

for i in range(len(list1)-1):
    if dict1[list1[i]] > dict1[list1[i+1]]:
        flag+=1
        break
if flag > 0:
    print("Happy Alex")
else:
    print("Poor Alex")
