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

'''
score = input("Enter Score: ")
score = float(score)

if score <= 1 and score >=0 :
  if (score >=0.9) :
    print('A')
  elif (score >=0.8) :
    print('B')
  elif (score >=0.7) :
    print('C')
  elif (score >=0.6) :
    print('D')
  else :
    print('F')
else :
  print('ERROR')
'''