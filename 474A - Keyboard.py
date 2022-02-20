str1 = "qwertyuiopasdfghjkl;zxcvbnm,./"
str2 = input()
str3 = input()
str4 = ""
for i in str3:
    index = [j for j, x in enumerate(str1) if x == i][0]
    if str2 == "R":
        if index == 0 or index == 10 or index == 20:
            str4 += str1[index]
        else:
            str4+=str1[index-1]
    else:
        if index == 9 or index == 19 or index == 29:
            str4+=str1[index]
        else:
            str4+=str1[index+1]
            
print(str4)
