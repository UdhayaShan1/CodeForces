n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    r_index = [-1]+[i for i, x in enumerate(ref) if x == "R"]+[len(ref)]
    max1 = 0
    for i in range(1,len(r_index)):
        if r_index[i] - r_index[i-1] > max1:
            max1 = r_index[i] - r_index[i-1]
    print(max1)
    k1+=1
    if k1==len(list1):
        break
