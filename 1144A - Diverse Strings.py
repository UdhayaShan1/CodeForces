n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_str = list1[k1]
    sorted_set = sorted(set(ref_str))
    if len(ref_str) != len(sorted_set):
        print("No")
        k1+=1
        continue
    str1 = "abcdefghijklmnopqrstuvwxyz"
    start = sorted_set[0]
    end = sorted_set[-1]
    start_index = 0
    end_index = 0
    for i in str1:
        if i == start:
            start_index = str1.index(i)
        elif i == end:
            end_index = str1.index(i)
    flag = 0
    for i in str1[start_index:end_index+1]:
        if i not in sorted_set:
            flag+=1
            break
    if flag>0:
        print("No")
    else:
        print("Yes")
    k1+=1
