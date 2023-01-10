hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hourly rate:")
r = float(rate)
if(h<=40):
    pay=r*h
    print(pay)
else:
    pay=40*r
    pay=pay+(h-40)*1.5*r
    print(pay)