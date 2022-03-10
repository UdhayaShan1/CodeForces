n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    one_count = len([i for i, x in enumerate(ref) if x == "1"])
    zero_count = len([i for i, x in enumerate(ref) if x == "0"])
    if one_count != zero_count:
        print(min(one_count,zero_count))
    else:
        print(one_count-1)
    k1+=1
    if k1==len(list1):
        break
