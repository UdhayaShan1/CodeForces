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
    ref = list1[k1]
    ref.sort()
    a = ref[0]
    b = ref[1]
    c = max(ref) - (a+b)
    print(a,b,c)
    k1+=1
    if k1==len(list1):
        break
