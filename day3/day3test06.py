year=int(input("year=:"))
month=int(input("month=:"))
day=int(input("day=:"))
days_in_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) and year%400==0:
    days_in_month[2]=29
days=sum(days_in_month[:month])+day
print(days)