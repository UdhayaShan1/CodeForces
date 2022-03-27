n1 = int(input())
if n1 == 1:
    print(0)
elif n1 % 2 != 0:
    print(0)
else:
    print(2*(2)**(n1//2-1))
