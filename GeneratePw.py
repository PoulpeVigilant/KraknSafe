import secrets as s
from IsPwRobust import *


def RandomCar():
    return (s.choice([chr(i)  for i in range(32,127)]))

"""
print(RandomCar())
"""

def AutoGenPw():
    PwAuto = ""
    for i in range(15): # longueur défaut pw =15 aléatoire?    s.choice([i for i in range(14,20)])
        PwAuto+= RandomCar()
    return PwAuto

"""
for i in range(10):
    print(AutoGenPw())
"""  

def GenPwByLen():
    PwGenByLen = "a"
    length = int(input())
    for i in range(length):
        PwGenByLen+= RandomCar()
    return PwGenByLen

"""

for i in range(10):
    print(GenPwByLen(length))
"""

# ça fonctionne bien : ) je ne peux juste pas commencer avec un "" vide par propriétés du log.

def GenPwByEntropy():
    PwGenByEntropy = RandomCar()
    entropyWanted = int(input())
    while(entropyOfPw(PwGenByEntropy)<=entropyWanted):
        PwGenByEntropy+= RandomCar()
    return PwGenByEntropy 

"""
print(GenPwByEntropy())
"""