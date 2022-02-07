x = int(input())

def lucky(num1):
    count = 0
    for i in str(num1):
        if i == "4" or i == "7":
            count+=1
    if count == len(str(num1)):
        return True
    else:
        return False
    
flag = 0
for i in range(1,x+1):
    if x % i == 0:
        if lucky(int(x/i)) == True:
            flag+=1
            break
if flag >= 1:
    print("YES")
else:
    print("NO")
