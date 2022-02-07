n1 = int(input())
n2 = int(input())
middle = int((n1+n2)/2)
def ap(no1):
    return (no1/2)*(2+(no1-1))

print(int(ap(abs(middle-n1))+ap(abs(middle-n2))))
