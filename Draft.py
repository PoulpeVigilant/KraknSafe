import re
#from IsPwRobust import *

txt = "1/0101/2024"
x = re.search("[\x41-\x42]", txt)
y = re.search("[a-z]",txt)
z = re.search("[A-Z]",txt)
u = re.search("^\d{3}",txt)


anyYear = (re.findall("\d{4}",txt))
anyNumber = re.search("\d{2}",txt)
anyDate = re.search("\d{1,2}/\d{2}/\d{4}",txt)
anyWord = re.search("[a-zA-Z]{3}",txt)
anySpec = re.search("([\x20-\x2F][\x3A-\x40][\x5B-\x60][\x7B-\x7E]){3}",txt)

print(anyYear)
""" print(anyNumber)
print(anyDate)
print(anySpec) """

""" PwGenByEntropy = "a8!"
print(entropyOfPw(PwGenByEntropy)) """

