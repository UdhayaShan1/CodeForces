n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_digit = list1[k1]
    if ref_digit == 1:
        print(0)
        k1+=1
        continue
    if ref_digit == 2:
        print(1)
        k1+=1
        continue
    if ref_digit == 3:
        print(2)
        k1+=1
        continue
    if ref_digit % 2==0:
        print(2)
        k1+=1
        continue
    if ref_digit % 2 != 0:
        print(3)
        k1+=1
        continue
    
