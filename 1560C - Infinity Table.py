import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    ref1 = math.ceil(ref**0.5)
    if ref <= ref1 ** 2 and ref >= (ref1 ** 2 - (ref1-1)):
        columns = ref1**2 - ref+1
        print(ref1,columns)
    else:
        ref2 = (ref1 ** 2 - (ref1-1))
        rows = ref1 - (ref2 - ref)
        print(rows,ref1)
    k1+=1
    if k1==len(list1):
        break
