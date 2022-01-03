n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_n = list1[k1]
    ref_str = list2[k1]
    index_character = [i for i, x in enumerate(ref_str) if x.isalpha() == True]
    if len(index_character) == 0:
        print("YES")
        k1+=1
        continue
    else:
        last_index = index_character[-1]
        back_length = len(ref_str)-1 - last_index
        if back_length > len(ref_str) - back_length:
            print("YES")
        else:
            print("NO")
        k1+=1
        continue
