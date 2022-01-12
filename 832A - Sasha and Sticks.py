x = input().split()
n = int(x[0])
k = int(x[1])

if n //k % 2 == 0:
    print("NO")
else:
    print("YES")
