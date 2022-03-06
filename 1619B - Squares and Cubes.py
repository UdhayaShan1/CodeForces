n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    set1 = {1}
    for i in range(1,ref+1):
        x = i**2
        if x>ref:
            break
        y = i**3
        set1.add(x)
        if y <=ref:
            set1.add(y)
    print(len(set1))
    k1+=1
    if k1==len(list1):
        break
