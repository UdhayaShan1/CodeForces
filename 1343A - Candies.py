n1 = int(input())
for i in range(n1):
    y = int(input())
    for j in range(2,31):
        if y % (2**(j) - 1) == 0:
            print(y // (2**(j) - 1))
            break
