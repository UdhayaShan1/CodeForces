n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    index_one = [i for i, x in enumerate(ref_list) if x == "1"]
    diff_count = 0
    for i in range(len(index_one)-1):
        if index_one[i+1] - index_one[i] > 1:
            diff_count += (index_one[i+1] - index_one[i] - 1)
    print(diff_count)
    k1+=1
    if k1==len(list1):
        break
            
        
