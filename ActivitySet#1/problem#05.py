# Functions

'''
def computepay(h, r):
    pass  # ...


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
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