import math
import re

## On commence par récupérer le mot de passe et ses caractéristiques pour ensuite les analyser.

pwToTest = input()

#print(type(pwToTest)) mon input est un string.
#print(pwToTest)

pwLength = len(pwToTest) # Qu'importe le string et son contenu, je récupère bien le nombre de caractères du mdp

# L'ensemble des éléments nécessaire à l'analyse des pw : regex

# The research is done with the unicode value of the caracters.

anyUppercase = re.search("[\x41-\x5A]",pwToTest)

anyLowercase = re.search("[\x61-\x7A]",pwToTest)

anyNumbers = re.search("[\x30-\x39]",pwToTest)

anySpecialCar = re.search("[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]",pwToTest) 

def getRangeOfCaractersType(): #Encore un souci avec cette fonction qui ne veut pas.
    x = 0
    if anyUppercase != None:
        x +=26
    if anyLowercase != None:
        x +=26
    if anyNumbers != None:
        x +=10
    if anySpecialCar != None:
        x += 32
    return x

def entropyOfPw(X): # Cette entropie correspond au site proton, mais pas à celle de Keepass.
    entropy = pwLength*math.log2(X)
    return entropy

print(pwLength)
print(anySpecialCar)
print(anyUppercase)
print(anyLowercase)
print(anyNumbers)

C = getRangeOfCaractersType()
print(C)
print(entropyOfPw(C))


