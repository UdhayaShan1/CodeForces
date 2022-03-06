n1= list(input())
for i in range(len(n1)):
    if i == 0:
        if int(n1[i]) >= 5 and int(n1[i]) != 9:
            (n1[i]) = str(9 - int(n1[i]))
    else:
        if int(n1[i]) >= 5:
            (n1[i]) = str(9 - int(n1[i]))

print(''.join(n1))
