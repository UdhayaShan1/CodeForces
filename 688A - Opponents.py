x = input().split()
n = int(x[0])
d = int(x[1])

list1 = []
for i in range(d):
    list1.append(input())
streak = 0
max1 = 0
for i in range(len(list1)):
    if "0" in list1[i]:
        streak+=1
        if streak > max1:
            max1 = streak
    else:
        streak = 0
print(max1)
