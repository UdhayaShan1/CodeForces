x = input().split()
n = int(x[0])
a = int(x[1])
b = int(x[2])
 
first = n - a
second = n - a-1
count = 0
b1 = False
while b1==False:
    if second < 0:
        break
    if second <= b:
        count+=1
    second-=1
    
print(count)
