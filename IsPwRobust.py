import math
import re

## On commence par récupérer le mot de passe et ses caractéristiques pour ensuite les analyser.

pwToTest = input()

# The analyze of the PW is done with the unicode value of each it' caracters.

pwLength = len(pwToTest) 

anyUppercase = re.search("[\x41-\x5A]",pwToTest)

anyLowercase = re.search("[\x61-\x7A]",pwToTest)

anyNumbers = re.search("[\x30-\x39]",pwToTest)

anySpecialCar = re.search("[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]",pwToTest) 

# Two functions necessary to get the entropy of the PW.

def getRangeOfCaractersType():
    x = 94
    if anyUppercase == None:
        x -=26
        print("Where are your uppercase caracters ?")
    if anyLowercase == None:
        x -=26
        print("Where are your lowercase caracters ?")
    if anyNumbers == None:
        x -=10
        print("Where are your numbers?")
    if anySpecialCar == None:
        x -= 32
        print("Where are your special caracters ?")
    return x

def entropyOfPw(X): # Cette entropie correspond à l'entropie pour un mot de passe constitué aléatoirement.
    entropy = pwLength*math.log2(X)
    return entropy

print("the pw length is of",pwLength, "caracters")

C = getRangeOfCaractersType()
print("The range of caracters is",C)
print("The entropy of your pw is",entropyOfPw(C),"bits")


