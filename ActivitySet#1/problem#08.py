# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue


      
   
    count=count+1
    a=line.find('0')
    b=line[a:]
    c=float(b)
    total=total+c
   
print('Average spam confidence:',total/count
