import math
import re

# The functions necessary to get the entropy of the PW.

def GetLengthOfPw(pwToCheck):
    L = len(pwToCheck)
    return L

def GetRangeOfCaractersType(pwToCheck):

    message = ""

    # The analyze of the PW is done with the unicode value of each it' caracters.

    anyUppercase = re.search("[\x41-\x5A]",pwToCheck)

    anyLowercase = re.search("[\x61-\x7A]",pwToCheck)

    anyNumbers = re.search("[\x30-\x39]",pwToCheck)

    #Ici on a notre warning nested jsp quoi
    anySpecialCar = re.search("[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]",pwToCheck) 

    x = 94

    if anyUppercase == None:
        x -=26
        message += "Where are your uppercase caracters ?"
    if anyLowercase == None:
        x -=26
        message += "Where are your lowercase caracters ?"
    if anyNumbers == None:
        x -=10
        message += "Where are your numbers?"
    if anySpecialCar == None:
        x -= 32
        message += "Where are your special caracters ?"
    
    return x

def entropyOfPw(pw):
    pwLength = GetLengthOfPw(pw)
    X = GetRangeOfCaractersType(pw)
    entropy = pwLength*math.log2(X)
    #print("pw entropy:",entropy,"bits")
    return entropy


# Some functions to analyse even more precisely how robust the pw is.


def CheckDataBase(pwToCheck):
    db = open("DataBaseOfPw.txt")
    x = db.read()
    pwDb = x.split()
    isPresent = False
    for pw in pwDb:
        if (pw==pwToCheck):
            isPresent = True
    return isPresent

""" print(CheckDataBase("nico")) """

def CheckDangerousPatterns(pwToCheck):
    anyYear = re.search("\d{4}",pwToCheck)
    anyNumber = re.search("\d{2}",pwToCheck)
    anyDate = re.search("\d{1,2}/\d{2}/\d{4}",pwToCheck) # Warning ?
    anyWord = re.search("[a-zA-Z]{3}",pwToCheck) 
    anySpec = re.search("[[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]]{3}",pwToCheck) # marche pas si différents caractères
    return 0


# On essaie de faire une fonction globale d'analyse, qui nous renvoie toutes les infos.Ne faire que des prints ? mettre tous les messages là ?

""" def CommunicationOfAnalysis(pw):
    print(?)
    CheckDataBase(pw)
    GetRangeOfCaractersType(pw)
    CheckDangerousPatterns(pw)
     """

# Test of entropy Function.

pw = input()
print(entropyOfPw(pw))
