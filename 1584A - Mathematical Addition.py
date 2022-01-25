from fractions import Fraction
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
    u = list1[k1][0]
    v = list1[k1][1]
    ratio = (Fraction(1,(u+v))-Fraction(1,(v)))/ (Fraction(1,u)-Fraction(1,(u+v)))
    print(ratio.numerator,ratio.denominator)
    k1+=1
    if k1==len(list1):
        break
