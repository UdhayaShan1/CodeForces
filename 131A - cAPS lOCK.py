x = list(input())
upper = 0
for i in x:
    if i.isupper() == True:
        upper+=1
if upper == len(x):
    for i in range(len(x)):
        if x[i].islower() == True:
            x[i] = x[i].upper()
        else:
            x[i] = x[i].lower()
    print(''.join(x))
elif upper == len(x)-1:
    if x[0].islower() == True:
        for i in range(len(x)):
            if x[i].islower() == True:
                x[i] = x[i].upper()
            else:
                x[i] = x[i].lower()
        print(''.join(x))
    else:
        print(''.join(x))
else:
    print(''.join(x))
