n1 = int(input())
str1 = list(input())
list1 = ["a","e","i","o","u","y"]
 
b1 = False
while b1==False:
    flag = 0
    for i in range(len(str1)-1):
        if str1[i+1] in list1 and str1[i] in list1:
            str1.pop(i+1)
            flag+=1
            break
    if flag == 0:
        print(''.join(str1))
        break
