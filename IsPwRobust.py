import math
import re
import secrets as s

## On commence par récupérer le mot de passe et ses caractéristiques pour ensuite les analyser.

# Two functions necessary to get the entropy of the PW.

def getRangeOfCaractersType(pwToTest):

    # The analyze of the PW is done with the unicode value of each it' caracters.

    anyUppercase = re.search("[\x41-\x5A]",pwToTest)

    anyLowercase = re.search("[\x61-\x7A]",pwToTest)

    anyNumbers = re.search("[\x30-\x39]",pwToTest)

    #Ici on a notre warning nested jsp quoi
    anySpecialCar = re.search("[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]",pwToTest) 

    x = 94

    if anyUppercase == None:
        x -=26
        #print("Where are your uppercase caracters ?")
    if anyLowercase == None:
        x -=26
        #print("Where are your lowercase caracters ?")
    if anyNumbers == None:
        x -=10
        #print("Where are your numbers?")
    if anySpecialCar == None:
        x -= 32
        #print("Where are your special caracters ?")
    return x

def entropyOfPw(pw):
    pwLength = len(pw)
    #print("pw length is:",pwLength)
    X = getRangeOfCaractersType(pw)
    #print("range of caracters:",X)
    entropy = pwLength*math.log2(X)
    #print("pw entropy:",entropy,"bits")
    return entropy

# Calculs d'entropie

"""
pw = input()
print(entropyOfPw(pw))
"""