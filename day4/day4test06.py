if __name__=="__main__":
    list_=[]
    list=list(range(1000))
    for idx in range(len(list)):
        if list[idx]%2==0:
            list_.append(idx)
    print(list_)
##在使用pop时列表的元素个数改变导致索引错误