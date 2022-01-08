n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(abs(int(j)))
    list2.append(temp)
  
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref_list = list2[k1]
    set_list = list(set(ref_list))
    sum1 = 0
    for i in set_list:
        if len([j for j, x in enumerate(ref_list) if x == i]) > 1 and i != 0:
            sum1+=2
        else:
            sum1+=1
            
    print(sum1)
    k1+=1
    if k1==len(list2):
        break
    
