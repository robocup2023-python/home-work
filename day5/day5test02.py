def odd_number(*arg):
    list=[num for i,num in enumerate(arg) if num%2!=0]
    return list