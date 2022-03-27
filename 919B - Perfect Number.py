n1 = int(input())
list1 = []
for i in range(19,2*(10**7)):
    temp = 0
    for j in str(i):
        temp += int(j)
    if temp == 10:
        list1.append(i)
print(list1[n1-1])
