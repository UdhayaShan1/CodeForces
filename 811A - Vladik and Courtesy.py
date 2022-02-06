x = input().split()
a = int(x[0])
b = int(x[1])

b1 = False
k1 = 1
while b1==False:
    a-= k1
    k1+=1
    if b<k1:
        print("Valera")
        break
    b-=k1
    k1+=1
    if a<k1:
        print("Vladik")
        break
