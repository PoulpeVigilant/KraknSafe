import math
import re

# The functions necessary to get the entropy of the PW.

def GetLengthOfPw(pwToCheck):
    L = len(pwToCheck)
    if(L<=12):
        M = "Your password is not long enough"
    else:
        M = "Good Length of password"
    return L,M

def GetRangeOfCaractersType(pwToCheck):

    M = ""

    # The analyze of the PW is done with the unicode value of each it' caracters.

    anyUppercase = re.search("[\x41-\x5A]",pwToCheck)

    anyLowercase = re.search("[\x61-\x7A]",pwToCheck)

    anyNumbers = re.search("[\x30-\x39]",pwToCheck)

    #Ici on a notre warning nested jsp quoi
    anySpecialCar = re.search("[\\x20-\\x2F]|[\\x3A-\\x40]|[\\x5B-\\x60]|[\\x7B-\\x7E]",pwToCheck) 

    x = 94

    if anyUppercase == None:
        x -=26
        M += "Where are your uppercase caracters ?"
    if anyLowercase == None:
        x -=26
        M += "Where are your lowercase caracters ?"
    if anyNumbers == None:
        x -=10
        M += "Where are your numbers?"
    if anySpecialCar == None:
        x -= 32
        M += "Where are your special caracters ?"
    
    return x,M

def entropyOfPw(pw):
    pwLength = GetLengthOfPw(pw)[0]
    X = GetRangeOfCaractersType(pw)[0]
    entropy = pwLength*math.log2(X)
    return entropy


# Some functions to analyse even more precisely how robust the pw is.


def CheckDataBase(pwToCheck):
    M=""
    db = open("DataBaseOfPw.txt")
    x = db.read()
    pwDb = x.split()
    isPresent = False
    for pw in pwDb:
        if (pw==pwToCheck):
            isPresent = False
    if (isPresent == True):
        M+="warning your pw has been found in a common pw db"
    else:
        M+="warning your pw has been found in a common pw db"
    return M

""" print(CheckDataBase("nico")) """

def CheckDangerousPatterns(pwToCheck):
    M=""
    anyYear = re.search(r"\d{4}",pwToCheck)
    if(anyYear!=None):
        M+="warning the pattern of a year has been found:"
    anyNumber = re.search(r"\d{2}",pwToCheck)
    if(anyNumber!=None):
        M+="warning the pattern of a number has been found:"
    anyDate = re.search(r"\d{1,2}\/\d{2}\/\d{4}",pwToCheck) # Warning ?
    if(anyDate!=None):
        M+="warning the pattern of a Date has been found:"
    anyWord = re.search("[a-zA-Z]{3}",pwToCheck)
    if(anyWord!=None):
        M+="warning the pattern of a word has been found"
    anySpec = re.search(r"[\x20-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\x7E]{3}",pwToCheck) # marche pas si différents caractères
    if(anySpec!=None):
        M+="warning the pattern of a repetition of specar has been found"
    return M


# On essaie de faire une fonction globale d'analyse, qui nous renvoie toutes les infos.Ne faire que des prints ? mettre tous les messages là ?

def CommunicationOfAnalysis(pw):
    print("Let's analyse your pw")
    print(GetLengthOfPw(pw)[1])
    print(GetRangeOfCaractersType(pw)[1])
    print(CheckDataBase(pw))
    print(CheckDangerousPatterns(pw))
    return "" 
    

# Test of entropy Function.

pw = input()
print(entropyOfPw(pw))

# Test of analysis function

print(CommunicationOfAnalysis(pw))