n1 = int(input())
if n1==1:
    print(1)
    print("C")
else:
    count1 = 0
    count2 = 0
    str1 = ["."]*n1
    str2 = ["."]*n1
    for i in range(len(str1)):
        if i % 2 == 0:
            str1[i] = "C"
            count1 += 1
    for i in range(len(str2)):
        if i % 2 != 0:
            str2[i] = "C"
            count2 += 1
    final = 0
    for i in range(n1):
        if i % 2 == 0:
            final += count1
        else:
            final += count2
    print(final)
    for i in range(n1):
        if i % 2 ==0:
            print(''.join(str1))
        else:
            print(''.join(str2))
