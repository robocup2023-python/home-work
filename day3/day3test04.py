num=int(input("num=:"))
num_str=str(num)
digits=len(num_str)
if num_str==num_str[::-1]:
    print('是回文数')
else:
    print('不是回文数')