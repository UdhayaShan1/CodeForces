x = input().split()
n = int(x[0])
m = int(x[1])
k = int(x[2])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

first_index = -10000
second_index = -10000

for i in range(m-1,-1,-1):
    if list1[i] == 0:
        continue
    if k>=list1[i]:
        first_index = i
        break

for i in range(m,n):
    if list1[i] == 0:
        continue
    if k>=list1[i]:
        second_index = i
        break

if abs(first_index-(m-1)) <= abs(second_index-(m-1)):
    print((abs(first_index-(m-1)))*10)
else:
    print((abs(second_index-(m-1)))*10)
