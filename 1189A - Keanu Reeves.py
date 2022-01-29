n1 = int(input())
n2 = input()

no_zero = len([i for i, x in enumerate(n2) if x == "1"])
no_one = len([i for i, x in enumerate(n2) if x == "0"])

if no_one != no_zero:
    print(1)
    print(n2)
else:
    print(2)
    print(n2[0] + " " + n2[1:])
