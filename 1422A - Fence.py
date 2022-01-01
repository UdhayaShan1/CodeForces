n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    print((ref_list[0]+ref_list[1]+ref_list[2])-1)
    k1+=1
    if k1==len(list1):
        break
