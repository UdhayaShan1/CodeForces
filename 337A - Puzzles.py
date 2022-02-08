x = input().split()
n = int(x[0])
m = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()

b1 = False
min1 = 100000
start = 0
while b1==False:
    for i in range(start,len(list1)):
        ref = list1[i:i+n]
        if len(ref) == n:
            ref2 = max(ref) - min(ref)
            if ref2<min1:
                min1=ref2
    start+=1
    if start == len(list1):
        break

print(min1)
