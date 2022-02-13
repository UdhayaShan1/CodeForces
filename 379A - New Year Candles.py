x = input().split()
a = int(x[0])
b = int(x[1])

count = a
b1 = False
while b1==False:
    if a < b:
        print(count)
        break
    count += (a//b)
    a = a // b + a % b
