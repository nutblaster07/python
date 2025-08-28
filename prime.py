import math
num=int(input("enter a no."))
for i in range(2,int(math.sqrt(num))+1):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")
