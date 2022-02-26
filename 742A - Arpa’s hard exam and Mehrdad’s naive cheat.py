list1 = []
count1 = 0
for i in range(1,20):
    if count1 == 4:
        break
    list1.append(int(str(8**i)[-1]))
    count1+=1
x = int(input())
if x == 0:
    print(1)
else:
    print(list1[x%4 - 1])
