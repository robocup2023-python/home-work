def test03(num):
    num_str=str(num)
    num_digits=len(num_str)
    print("位数为{}".format(num_digits))
    for digit in reversed(num_str):
        print(digit,end=' ')
n=input("n=:")
test03(n)
    