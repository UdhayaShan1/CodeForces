n1 = int(input())
str1 = list(input())
count = 0
str2 = ''
for i in range(0,int(len(str1)/2)):
    if str1[i*2] == "a" and str1[i*2+1] == "b":
        continue
    elif str1[i*2] == "b" and str1[i*2+1] == "a":
        continue
    else:
        if str1[i*2] == "a":
            str1[i*2] = "b"
            str1[i*2+1] = "a"
        else:
            str1[i*2] = "a"
            str1[i*2+1] = "b"
        count+=1

print(count)
print(''.join(str1))
