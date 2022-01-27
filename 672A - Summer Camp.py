n1 = int(input())
str1 = ""
for i in range(1,500):
    if len(str1) >= n1:
        print(str1[n1-1])
        break
    str1+=str(i)
