x = input().split()
n = int(x[0])
t = int(x[1])
if t == 10 and n == 1:
    print(-1)
else:
    if t == 10:
        str1 = "1"*(n-1)
        str1 += "0"
    else:
        str1 = ""
        for i in range(n):
            str1 += str(t)
    print(str1)
