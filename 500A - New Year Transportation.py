x = input().split()
n = int(x[0])
t = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

b1 = False
start = 0

while b1==False:
    if start == t-1:
        print("YES")
        break
    elif start > t-1:
        print("NO")
        break
    start = list1[start]+start
    
