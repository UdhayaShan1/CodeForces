n1 = input()
str1 = "abcdefghijklmnopqrstuvwxyz"
i = int(n1[1])-1
j = [i for i, x in enumerate(str1) if x == n1[0]][0]

def check(i,j):
    count = 0
    for k in range(i-1,i+2):
        for z in range(j-1,j+2):
            if k < 0 or z < 0 or k >= 8 or z >= 8:
                continue
            else:
                count+=1
    count-=1
    return count
    
print(check(i,j))
