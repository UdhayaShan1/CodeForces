n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    str1 = list1[k1]
    if str1[-2]+str1[-1] == "po":
        print("FILIPINO")
        k1+=1
        continue
    if str1[-4]+str1[-3]+str1[-2]+str1[-1] == "desu" or str1[-4]+str1[-3]+str1[-2]+str1[-1] == "masu":
        print("JAPANESE")
        k1+=1
        continue
    if str1[-5]+str1[-4]+str1[-3]+str1[-2]+str1[-1] == "mnida":
        print("KOREAN")
        k1+=1
        continue
