x = input().split()
w = int(x[0])
h = int(x[1])
list1 = []
for i in range(2):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
stone1 = list1[0]
stone2 = list1[1]

b1 = False
while b1==False:
    if h == stone1[-1]:
        w -= stone1[0]
    if h == stone2[-1]:
        w-= stone2[0]
    w += h
    h-=1
    if w<0:
        w = 0
    if h == 0:
        print(w)
        break
