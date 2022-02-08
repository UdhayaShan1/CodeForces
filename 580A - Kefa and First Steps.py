n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
streak = 0
max1 = 0
for i in range(len(list1)-1):
    if list1[i+1] >= list1[i]:
        streak+=1
        if streak+1>max1:
            max1=streak+1
    else:
        streak = 0
print(max1)
