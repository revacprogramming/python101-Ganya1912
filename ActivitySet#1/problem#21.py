import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)


#Conditional Execution 
score = input("Enter Score: ")
s=float(score)
if 0.0<s<1.0:
    if s>=0.9:
        print('A')
    elif s>=0.8:
        print('B')
    elif s>=0.7:
        print('C')
    elif s>=0.6:
        print('D')
    elif s<0.6:
        print('F')
else:
    print("Invalid Input")
    exit()