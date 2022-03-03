n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    if ref % 7 == 0:
        print(ref)
        k1+=1
        continue
    start1 = (ref//7) * 7
    diff = 0
    for i in range(len(str(start1))):
        if str(start1)[i] != str(ref)[i]:
            diff+=1
    if diff == 1:
        if len(str(start1)) == len(str(ref)):
            print(start1)
            k1+=1
            continue
    print((ref//7 + 1) * 7)
    k1+=1
    continue
