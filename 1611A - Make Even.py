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
    indices_odd = [i for i, x in enumerate(str(ref_digit)) if int(x) % 2 == 0]
    if len(indices_odd) == 0:
        print(-1)
        k1+=1
        continue
    if int(str(ref_digit)[-1]) % 2 == 0:
        print(0)
        k1+=1
        continue
    if int(str(ref_digit)[0]) % 2 == 0:
        print(1)
        k1+=1
        continue
    print(2)
    k1+=1
    continue
