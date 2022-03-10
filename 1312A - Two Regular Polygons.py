n1 = int(input())
for i in range(n1):
    x = input().split()
    if max(int(x[0]),int(x[1])) % (min(int(x[0]),int(x[1]))) == 0:
        print("YES")
    else:
        print("NO")
