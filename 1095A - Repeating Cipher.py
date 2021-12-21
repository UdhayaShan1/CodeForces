n1 = int(input())
n2 = list(input())
collection = []

b1 = False
k1 = 1
while b1==False:
    if len(n2)==0:
        break
    collection.append(n2[0])
    for i in range(k1):
        n2.pop(0)
    k1+=1
    
print(''.join(collection))
