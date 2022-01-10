x = int(input())
list1 = []
for i in range(x):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    n = ref_list[0]
    k = ref_list[-1]
    str1 = n//3 * "abc"
    str1 += "abc"[0:n%3]
    print(str1)
    k1+=1
    if k1==len(list1):
        break
