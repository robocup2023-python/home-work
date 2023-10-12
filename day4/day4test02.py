##假设已有数组
array=[1,3,5,7,9]
num=int(input("num=:"))
if num>=array[-1]:
    array.append(num)
else:
    for i in range(len(array)):
        if num<array[i]:
            array.insert(i,num)
            break
print("插入后的数组:",array)