n1 = int(input())
x = input()
min1 = 0
count = 0
minus = 0
plus = 0
for i in x:
    if i == "-":
        count -= 1
        minus += 1
        if count < min1:
            min1 = count
    elif i == "+":
        plus += 1
        count += 1
        if count < min1:
            min1 = count

min1 = abs(min1)

print(min1 + (plus - minus))
