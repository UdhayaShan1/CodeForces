x1 = input().split()
x = int(x1[0])
y = int(x1[1])
z = int(x1[2])

if abs(x-y) == 0 and z == 0:
    print(0)
else:
    if z >= abs((x-y)):
        print("?")
    else:
        if (x-y) >0:
            print("+")
        else:
            print("-")
