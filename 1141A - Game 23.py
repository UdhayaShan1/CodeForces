x = input().split()
a = int(x[0])
b = int(x[1])
if b % a != 0:
    print(-1)
else:
    diff = b//a
    three = 0
    def cubecheck(num):
        global three
        for i in range(0,50):
            if (3**i) == num:
                three = i
                return True
        return False
    
    flag = 0
    two = 0
    for i in range(0,50):
        if diff % (2**i) == 0:
            if cubecheck(diff // (2**i)) == True:
                two = i
                flag+=1
                break
    if flag > 0 or a == b:
        print(two+three)
    else:
        print(-1)
