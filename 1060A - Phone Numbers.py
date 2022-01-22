n1 = int(input())
str1 = input()
if n1 < 11:
    print(0)
else:
    count_8 = 0
    for i in str1:
        if i == "8":
            count_8+=1
    print(min(count_8,n1//11))
