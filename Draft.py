import re

txt = "B"
x = re.search("[\x41-\x42]", txt)
y = re.search("[a-z]",txt)
z = re.search("[A-Z]",txt)
print(x)
""" print(y)
print(z)"""

print("Hello",x,"how are you?")