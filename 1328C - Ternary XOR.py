n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())

k1 = 0
b1 = False
while b1==False:
    flag = 0
    n = list1[k1]
    ref = list2[k1]
    str1 = ""
    str2 = ""
    for i in range(n):
        if flag == 0:
            if ref[i] == "2":
                str1 += "1"
                str2 += "1"
            elif ref[i] == "1":
                flag += 1
                str1 += "0"
                str2 += "1"
            else:
                str1 += "0"
                str2 += "0"
        else:
            if ref[i] == "2":
                str1 += "2"
                str2 += "0"
            elif ref[i] == "1":
                str1 += "1"
                str2 += "0"
            else:
                str1 += "0"
                str2 += "0"
    print(str1)
    print(str2)
    k1+=1
    if k1==len(list2):
        break
