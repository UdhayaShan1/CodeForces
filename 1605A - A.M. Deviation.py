n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0 
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    if ref_list[0]+ref_list[-1] == ref_list[1]*2:
        print(0)
        k1+=1
        continue
    if ref_list[0]<=0:
        temp1 = abs(0-ref_list[0])
        ref_list[-1] = ref_list[-1]-temp1
        ref_list[0] = 0
    else:
        temp1 = ref_list[0] - 0
        ref_list[-1] = ref_list[-1] + temp1
        ref_list[0] = 0
    mean = ref_list[-1] /2
    if ref_list[1]<mean:
        if (ref_list[-1]- 2*ref_list[1]) % 3 == 0:
            print(0)
        else:
            print(1)
    else:
        if (2*ref_list[1] - ref_list[-1]) % 3 ==0:
            print(0)
        else:
            print(1)
    k1+=1   
