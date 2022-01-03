from fractions import Fraction
n1 = int(input())
listn = []
for i in range(n1):
    listn.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    if k1==len(listn):
        break
    ref_int = listn[k1]
    if ref_int==1:
        print(0)
        k1+=1
        continue
    c1 = False
    count = 0
    
    while c1==False:
        flag = 0
        
        if ref_int % 2 == 0:
            d1 = False
            while d1==False:
                
                ref_int = Fraction(ref_int,1) * Fraction(1,2)
                count+=1
                if ref_int % 2 != 0:
                    break
            continue
        elif ref_int % 2 != 0:
            flag+=1
        
        if ref_int % 3 == 0:
            d2 = False
            while d2==False:
                
                ref_int = Fraction(ref_int,1) * Fraction(2,3)
                count+=1
                if ref_int % 3 != 0:
                    break
            continue
        elif ref_int % 3 != 0:
            flag+=1
        
        if ref_int % 5 == 0:
            d3 = False
            while d3==False:
                
                ref_int = Fraction(ref_int,1) * Fraction(4,5)
                count+=1
                if ref_int % 5 != 0:
                    break
            continue
        elif ref_int % 5 != 0:
            flag+=1
        
        if flag == 3 and ref_int == 1:
            
            print(count)
            break
        elif flag == 3 and ref_int >1:
            print(-1)
            break
    k1+=1  
