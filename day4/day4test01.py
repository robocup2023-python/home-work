int_array=[1,2,3,4,5]
str_array=[]
for num in int_array:
    str_array.append(str(num))
str_array_out=",".join(str_array)
print(str_array_out)