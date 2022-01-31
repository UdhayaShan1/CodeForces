n1 = int(input())

list1 = []

list1 = [1,1]
    
b1 = False
temp = 2
while b1==False:
    if temp>n1:
        break
    list1.append(temp)
    temp = list1[-1]+list1[-2]

str1 = ""
for i in range(n1):
    if i+1 in list1:
        str1+="O"
    else:
        str1+="o"
print(str1)
