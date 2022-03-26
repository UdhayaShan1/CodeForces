n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    if ref % 2 == 0:
        print(ref//2,ref//2)
    else:
        largest = 1
        for i in range(2,int(ref**0.5)+5):
            if i == ref:
                break
            if ref % i == 0:
                if i > largest:
                    largest = i
                if ref // i > largest:
                    largest = ref // i
        print(largest,ref-largest)
    k1+=1
    if k1==len(list1):
        break
