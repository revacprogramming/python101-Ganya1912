# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h > 40 :
 pay=(r*40)+(1.5*r*(h-40))
else :
    pay=(r*h)
print(pay)
