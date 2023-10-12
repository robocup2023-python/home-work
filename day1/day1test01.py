num_list=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                res=i*100+j*10+k
                num_list.append(res)
print(num_list)