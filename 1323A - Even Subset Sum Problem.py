n1 = int(input())
list1=[]
list2=[]
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref_list = list2[k1]
    even_index = [i for i, x in enumerate(ref_list) if x % 2 == 0]
    if len(even_index) >0:
        print(1)
        print(even_index[0]+1)
    else:
        odd_index = [i for i, x in enumerate(ref_list) if x % 2 != 0]
        if len(odd_index)>1:
            print(2)
            print(odd_index[0]+1,odd_index[1]+1)
        else:
            print(-1)
    k1+=1
    if k1==len(list2):
        break
