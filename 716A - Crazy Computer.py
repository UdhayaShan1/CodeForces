x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
y = input().split()
list2 = []
for i in y:
    list2.append(int(i))
n = list1[0]
c = list1[1]
streak = 0
for i in range(len(list2)-1):
    if (list2[i+1] - list2[i]) <= c:
        streak+=1
        continue
    if list2[i+1] - list2[i] > c:
        streak = 0
        continue
    
streak += 1
print(streak)
