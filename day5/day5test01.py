def caculate(*arg):
    total=sum(arg)
    average=total/len(arg)
    index=[i for i,num in enumerate(arg) if num>average]
    return (average,index)