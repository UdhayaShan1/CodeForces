n1 = input().split()
n = int(n1[0])
m = int(n1[-1])
a=-1
 
b1 = False
count = 0
while b1==False:
    a+=1
    b = n - a**2
    if b<0:
        break
    if (a+b**2) == m:
        count+=1
 
print(count)
