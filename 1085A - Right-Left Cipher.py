n1 = input()
length = len(n1)
list1 = list(n1)
list2 = [0]*length

b1 = False
if length % 2 == 0:
    while b1==False:
        list2[length-1] = list1[-1]
        list1.pop()
        list1.reverse()
        length-=1
        if length==0:
            print(''.join(list2))
            break
else:
    while b1==False:
        list2[length-1] = list1[0]
        list1.pop(0)
        list1.reverse()
        length-=1
        if length==0:
            print(''.join(list2))
            break
