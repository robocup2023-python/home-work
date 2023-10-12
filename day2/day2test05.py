import math
def prime(n):
    if n==2:
        return 1
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return 0
        return 1
for i in range(100,1000):
    if(prime(i)):
        print(i)