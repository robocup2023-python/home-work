for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if pow(a,3)+pow(b,3)+pow(c,3)==i:
        print(i)