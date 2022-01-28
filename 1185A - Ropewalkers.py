x = input().split()
list1 = []
for i in x[0:-1]:
    list1.append(int(i))
list1.sort()
a = list1[0]
b = list1[1]
c = list1[2]
d = int(x[-1])
sum1 = 0
diff1 = b-a
diff2 = c-b
if b-a < d:
    sum1 += d -(b-a)
if c-b < d:
    sum1 += d - (c-b)
print(sum1)
