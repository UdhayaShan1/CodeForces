n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_int = list1[k1]
    if ref_int == 2:
        print(2)
        k1+=1
        continue
    if ref_int % 2==0:
        print(0)
    else:
        print(1)
    k1+=1
