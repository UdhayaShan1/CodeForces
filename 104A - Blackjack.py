diff = int(input())-10
if diff <= 0 or diff>11:
    print(0)
else:
    dict1 = {}
    for i in range(1,10):
        dict1[i] = 4
    dict1[10] = 15
    dict1[11] = 4
    dict1[1] = 4
    print(dict1[diff]) 
