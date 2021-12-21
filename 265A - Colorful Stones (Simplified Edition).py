n1 = input()
n2 = input()

b1 = False
k1 = 0 
k2 = 0
movement = 1
while b1==False:
    if k2 == len(n2) or k1 == len(n1):
        print(movement)
        break
    if n2[k2] == n1[k1]:
        movement += 1
        k1+=1
        k2+=1
    else:
        k2+=1
