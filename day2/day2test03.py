height=100
distance=0
for i in range(10):
    if i==0:
        distance=height
    else:
        distance=distance+2*height
    height/=2
print("distance=",distance)
print("bounce height=:",height)