num=int(input("num=:"))
if (num%4==0 and num%100!=0) or (num%400==0):
    print("{}年是闰年".format(num))
else:
    print("{}年不是闰年".format(num))