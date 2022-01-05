n1 = int(input())

for i in range(n1):
    x = input().split()
    temp = 1
    for j in x:
        temp *= int(j)
    print(temp)
