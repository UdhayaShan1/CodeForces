n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
alphabet = "abcdefghijklmnopqrstuvwxyz" 
b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break
    ref_list = list(list1[k1])
    k2 = 0
    c1 = False
    while c1==False:
        if k2==len(ref_list):
            break
        if k2 % 2 == 0:
            if ref_list[k2] == "a":
                ref_list[k2] = "b"
            else:
                
                ref_list[k2] = "a"
        elif k2 % 2 != 0:
            if ref_list[k2] == "z":
                ref_list[k2] = "y"
            else:
                
                ref_list[k2] = "z"
        k2+=1
    print(''.join(ref_list))
    k1+=1
