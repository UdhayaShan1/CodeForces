import math
def prime(x):
    if x == 1:
        return False
    flag = 0
    for i in range(2,math.ceil((x**0.5)+1)):
        if x % i == 0:
            return False
    return True
    
n1 = int(input())

if n1%2 != 0:
    if n1==1:
        print(3)
    else:
        print(1)
else:
        
    b1 = False
    start = 1
    while b1==False:
        if prime((n1*start)+1) == False:
            print(start)
            break
        start+=1
