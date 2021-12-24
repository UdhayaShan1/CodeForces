n1 = int(input())
n2 = input().split()
list1 = []
for i in n2:
    list1.append(int(i))

chest = 0
biceps = 0
back = 0
for i in range(len(list1)):
    if i % 3 == 0:
        chest += list1[i]
    elif (i-1) % 3 == 0:
        biceps += list1[i]
    elif (i-2) % 3 ==0:
        back += list1[i]

max1 = max(chest,biceps,back)

if chest == max1:
    print("chest")
elif biceps == max1:
    print("biceps")
else:
    print("back")
