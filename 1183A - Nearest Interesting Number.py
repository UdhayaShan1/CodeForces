n1 = int(input())

b1 = False
while b1==False:
    str_ver = str(n1)
    total = 0
    for i in str_ver:
        total += int(i)
    if total % 4 == 0:
        print(n1)
        break
    n1+=1
