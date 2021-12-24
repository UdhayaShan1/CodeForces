n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break
    ref_str = list1[k1]
    if len(ref_str) == 1:
        print("NO")
        k1+=1
        continue
    length = len(ref_str)
    if length % 2 != 0:
        print("NO")
        k1+=1
        continue
    half = int(length /2)
    if ref_str[0:half] == ref_str[half:]:
        print("YES")
    else:
        print("NO")
    k1+=1
