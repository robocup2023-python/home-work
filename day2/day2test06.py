import math
def prime(n):
    if n==2:
        return 1
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return 0
        return 1
n=int(input("n=:"))
i=2
if(prime(n)):
    print(n)
else:
    print(str(n)+"=")
    while(prime(n)==0):
        if  n%i==0:
            print(str(i)+"*")
            n=n/i
            i=2
        else:
            i+=1
print(int(n))