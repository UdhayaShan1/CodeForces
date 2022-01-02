n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_str = list1[k1]
    flag = 0
    temp1 = ref_str + "a"
    temp2 = "a" + ref_str
    if temp1 != temp1[::-1]:
        print("YES")
        print(temp1)
        k1+=1
        continue
    if temp2 != temp2[::-1]:
        print("YES")
        print(temp2)
        k1+=1
        continue
    print("NO")
    k1+=1
