n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x=input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    a = list2[k1]
    print(max(a)-min(a))
    k1+=1
    if k1==len(list2):
        break
