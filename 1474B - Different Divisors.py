from bisect import bisect_right
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
def primecheck(num):
    if num <= 3:
        return True
    for i in range(2,int((num)**0.5+5)):
        if i == num:
            break
        if num % i == 0:
            return False
    return True
        
 
list2 = []
for i in range(1,45000):
    if primecheck(i) == True:
        list2.append(i)
 
b1 = False
k1 = 0
while b1==False:
    ref = list1[k1]
    list3 = [1]
    b1 = False
    while b1==False:
        if len(list3) == 3:
            break
        check = list3[-1] + ref
        min_val = list2[bisect_right(list2, check-1)]
        list3.append(min_val)
    product = 1
    for i in list3:
        product*=i
    print(product)
    k1+=1
    if k1==len(list1):
        break
