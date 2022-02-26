n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(list(input()))

k1 = 0
b1 = False

while b1 == False:
    ref = list1[k1]
    turn = 1
    c1 = False
    while c1==False:
        flag = 0
        for i in range(len(ref)-1):
            if ref[i] != ref[i+1]:
                flag+=1
                ref.pop(i)
                ref.pop(i)
                break
        if flag == 1:
            turn += 1
        else:
            if turn % 2 == 0:
                print("DA")
            else:
                print("NET")
            break
    k1+=1
    if k1==len(list1):
        break
