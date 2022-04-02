n1 = input()
n2 = input()
 
if n1==n2:
    print(-1)
else:
    min1 = ""
    max1 = ""
    if len(n1) < len(n2):
        print(len(n2))
    elif len(n2) < len(n1):
        print(len(n1))
    else:
        print(len(n1))
