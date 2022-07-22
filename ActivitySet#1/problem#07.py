# Strings

text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0.8475')
float(text[pos:])
print(text[pos:])
"""
text = 'X-DSPAM-Confidence:    0.8475'
colonpos = text.find(':')
host = text[colonpos+4:]
number = float(host)
print(number)
"""