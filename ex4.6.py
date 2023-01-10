def computepay(h, r):
    if(h<=40):
        pay=r*h
    else:
        pay=(r*h)+(r*0.5*(h-40))
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rat = input("Enter Rate:")
rat = float(rat)
p = computepay(hrs, rat)
print("Pay", p)