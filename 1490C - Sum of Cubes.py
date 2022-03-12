from bisect import bisect_left
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
ref_cubes = []
for i in range(1,10000):
    ref_cubes.append(i**3)
 
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_int = list1[k1]
    if ref_int == 1:
        k1+=1
        print("NO")
        continue
    flag = 0
    for i in ref_cubes:
        if ref_int > i:
            remainder = ref_int - i
            res = BinarySearch(ref_cubes, remainder)
            if res == -1:
                continue
            else:
                flag+=1
                break
        else:
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")
    k1+=1
