n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

def check(num1):
    if len(str(num1)) == 1:
        return 1
    str1 = "1"
    for i in str(num1)[1:]:
        if int(i) >= 1:
            str1+=str(1)
            
        else:
            str1+=str(0)
    return str1
    
k1 = 0
b1 = False
while b1==False:
    ref_int = list1[k1]
    count = 0
    c1 = False
    while c1==False:
        if ref_int == 0:
            break
        no1 = check(ref_int)
        ref_int = ref_int - int(no1)
        count+=1
        
    print(count)
    k1+=1
    if k1==len(list1):
        break
