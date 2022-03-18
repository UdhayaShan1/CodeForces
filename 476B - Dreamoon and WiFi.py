import math
n1 = input()
n2 = input()
pos = 0
neg = 0
for i in n1:
    if i == "+":
        pos+=1
    else:
        neg+=1
pos2 = 0
neg2 = 0
ques = 0
for i in n2:
    if i == "+":
        pos2+=1
    elif i == "-":
        neg2+=1
    else:
        ques+=1

if ques == 0:
    if (pos-neg) != (pos2-neg2):
        print(0)
    else:
        print(1)
else:
    value1 = pos-neg
    value2 = pos2-neg2
    remainder = value1-value2
    optimal_pos = (remainder+ques) / 2
    optimal_neg = ques - optimal_pos
    if optimal_pos < 0 or optimal_neg < 0:
        print(0)
    else:
        optimal_start = math.factorial(optimal_pos+optimal_neg) / (math.factorial(optimal_pos)*math.factorial(optimal_neg))
        start = ques
        start2 = 0
        count = 0
        b1 = False
        while b1==False:
            count += math.factorial(start+start2) / (math.factorial(start)*math.factorial(start2))
            start-=1
            start2+=1
            if start < 0:
                break
        print(optimal_start/count)
