x = input().split()
n = int(x[0])
x = int(x[1])
count = 0

for i in range(1,min(n,x)+1):
    if x % i == 0 and (x/i <= n):
        count+=1

print(count)
