n1 = int(input())
list1 = []
list2 = []
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
    ref = list2[k1]
    even = [i for i, x in enumerate(ref) if x % 2 == 0]
    odd = [i for i, x in enumerate(ref) if x % 2 != 0]
    if len(even) % 2 != 0:
        even_1 = even[1:]
        odd_1 = odd[1:]
        for i in range(1,len(even_1),2):
            first = even_1[i-1]
            second = even_1[i]
            print(first+1,second+1)
        for i in range(1,len(odd_1),2):
            first = odd_1[i-1]
            second = odd_1[i]
            print(first+1,second+1)
    else:
        if len(even) > 0:
            even_1 = even[2:]
            for i in range(1,len(even_1),2):
                first = even_1[i-1]
                second = even_1[i]
                print(first+1,second+1)
            for i in range(1,len(odd),2):
                first = odd[i-1]
                second = odd[i]
                print(first+1,second+1)
        else:
            odd_1 = odd[2:]
            for i in range(1,len(even),2):
                first = even[i-1]
                second = even[i]
                print(first+1,second+1)
            for i in range(1,len(odd_1),2):
                first = odd_1[i-1]
                second = odd_1[i]
                print(first+1,second+1)          
    k1+=1
    if k1==len(list2):
        break
