n1 = int(input())
x = input().split()
n2 = []
for i in x:
    n2.append(int(i))
b1 = False
k1 = 0
streak = 0
while b1==False:
    temp = []
    max1 = 0
    n2.sort()
    if len(n2) == 1:
        print(1)
        break
    for i in range(len(n2)-1):
        if n2[i+1] == n2[i]:
            streak += 1
        if n2[i+1] != n2[i] or i+1 == len(n2) - 1:
            if streak>max1:
                temp = []
                max1 = streak
                temp.append(n2[i])
                streak = 0
            streak = 0
    if len(temp) == 0:
        print(1)
        break
    
    indices_most = len([i for i, x in enumerate(n2) if x == temp[0]])
    
    print(indices_most)
    break
