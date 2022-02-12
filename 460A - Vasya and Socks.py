x = input().split()
socks = int(x[0])
m = int(x[1])
days = 1

b1 = False
while b1==False:
    socks -= 1
    if socks <= 0 and days % m != 0:
        print(days)
        break
    if days % m == 0:
        socks += 1
    days+=1
