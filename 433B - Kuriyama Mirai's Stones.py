n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
    
dp1 = {}
dp1[0] = list1[0]
for i in range(1,n1):
    dp1[i] = 0
    dp1[i] += (dp1[i-1]+list1[i])

sorted1 = list1.copy()
sorted1.sort()

dp2 = {}
dp2[0] = sorted1[0]
for i in range(1,n1):
    dp2[i] = 0
    dp2[i] += (dp2[i-1]+sorted1[i])
dp1[-1] = 0
dp2[-1] = 0

n2 = int(input())
list2 = []
for i in range(n2):
    list2.append(input().split())

k1 = 0
b1 = False
while b1==False:
    ref = list2[k1]
    type1 = int(ref[0])
    l = int(ref[1])-1
    r = int(ref[2])-1
    if type1 == 1:
        print(dp1[r]-dp1[l-1])
    else:
        print(dp2[r]-dp2[l-1])
    k1+=1
    if k1==len(list2):
        break
