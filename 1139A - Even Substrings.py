n1 = int(input())
n2 = int(input())

list1 = [i for i, x in enumerate(str(n2)) if int(x) % 2 == 0]

sum1 = 0

for i in list1:
    sum1+=i+1

print(sum1)
