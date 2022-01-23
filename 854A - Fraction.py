n1 = int(input())

def check(a,b):
    min1 = min(a,b)
    max1 = max(a,b)
    a = min1
    d1 = False
    flag = 0
    while d1==False:
        if a == 1:
            break
        if max1 % a ==0 and min1 % a == 0:
            flag+=1
            break
        else:
            a-=1
    if flag == 0:
        return True
    else:
        return False
        
if n1 % 2 == 0:
    x = n1/2 -1
    y = n1/2 +1
    b1 = False
    while b1==False:
        if check(x,y) == True:
            print(int(x),int(y))
            break
        else:
            x-=1
            y+=1
else:
    x = int(n1/2)
    y = int(n1/2) +1
    b1 = False
    while b1==False:
        if check(x,y) == True:
            print(int(x),int(y))
            break
        else:
            x-=1
            y+=1
