n1 = int(input())
listn = []
list1 = []
for i in range(n1):
    listn.append(int(input()))
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
def composite(num1):
    flag = 0
    c1 = False
    start = 2
    while c1==False:
        if num1 % start == 0:
            flag+=1
            break
        start+=1
        if start == num1:
            break
    if flag >= 1:
        return True
    else:
        return False
        
k1 = 0
b1 = False
while b1==False:
    n = listn[k1]
    ref_list = list1[k1]
    final1 = []
    if composite(sum(ref_list)) == True:
        for i in range(len(ref_list)):
            final1.append(i+1)
        print(len(final1))
        print(*final1)
    else:
        exclusion = []
        final2 = []
        for i in range(len(ref_list)):
            if ref_list[i] % 2 != 0:
                exclusion.append(i)
                break
        for i in range(len(ref_list)):
            if i not in exclusion:
                final2.append(i+1)
        print(len(final2))
        print(*final2)
    k1+=1
    if k1==len(list1):
        break
    
