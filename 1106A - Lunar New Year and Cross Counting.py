n1 =  int(input())
list1 = []
for i in range(n1):
    list1.append(input())
    
def cross_check(i,j):
    if i-1<0 or j-1 <0 or j +1 < 0 or i+1 < 0 or i < 0 or j < 0:
        return 0
    if i-1>=n1 or j-1 >=n1 or j +1 >=n1 or i+1 >=n1 or i >= n1 or j >= n1:
        return 0
    #M(i,j)=M(i−1,j−1)=M(i−1,j+1)=M(i+1,j−1)=M(i+1,j+1)= 'X'.
    if list1[i][j] == list1[i-1][j-1] == list1[i-1][j+1] == list1[i+1][j-1] == list1[i+1][j+1] == "X":
        return 1
    else:
        return 0

count = 0        
for i in range(n1):
    for j in range(n1):
        count += cross_check(i,j)
        
print(count)
        
