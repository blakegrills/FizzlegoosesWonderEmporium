import random

def Currency(cr, currency) :
    details = ""
    if cr < 4 :
        copRan = int(random.randrange(1, 10, 1))
        silRan = int(random.randrange(1, 5, 1))
        golRan = int(random.randrange(0, 1.1, .1))
    return details    

def ArtObj(cr, artObj) :
    details = ""
    return details    

def SpecialMats(cr, specialMats) :
    details = ""
    return details    

def NormEquip(cr, normEquip) :
    details = ""
    return details    

def MagicEquip(cr, magicEquip) :
    details = ""
    return details    

def Pots(cr, pots) :
    details = ""
    return details    

def Scroll(cr, scroll) :
    details = ""
    return details    

def WandStaff(cr, wandStaff) :
    details = ""
    return details    

def Rod(cr, rod) :
    details = ""
    return details    

def Wonderous(cr, wonderous) :
    details = ""
    return details    

def Artifact(cr, artifact) :
    details = ""
    return details    

def Cursed(cr, cursed) :
    details = ""
    return details    

def Intelligent(cr, intelligent) :
    details = ""
    return details   

def EncouterTreasure(cr, currency = 1, artObj = 1, specialMats = 1, normEquip = 1,
                     magicEquip = 1, pots = 1, scroll = 1, wandStaff = .5, rod = .5,
                     wonderous = .5, artifact = 0, cursed = 0, intelligent = 0) :
    details = ""
    Currency(cr, currency)  
    ArtObj(cr, artObj)  
    SpecialMats(cr, specialMats)  
    NormEquip(cr, normEquip)  
    MagicEquip(cr, magicEquip)   
    Pots(cr, pots)  
    Scroll(cr, scroll)  
    WandStaff(cr, wandStaff)   
    Rod(cr, rod)  
    Wonderous(cr, wonderous)   
    Artifact(cr, artifact)   
    Cursed(cr, cursed)   
    Intelligent(cr, intelligent)

    return details

def HoardTreasure(cr, currency = .5, artObj = .5, specialMats = .5, normEquip = 1,
                  magicEquip = .5, pots = .5, scroll = .5, wandStaff = .25, rod = .25,
                  wonderous = .25, artifact = 0, cursed = 0, intelligent = 0) :
    details = ""
    Currency(cr, currency)  
    ArtObj(cr, artObj)  
    SpecialMats(cr, specialMats)  
    NormEquip(cr, normEquip)  
    MagicEquip(cr, magicEquip)   
    Pots(cr, pots)  
    Scroll(cr, scroll)  
    WandStaff(cr, wandStaff)   
    Rod(cr, rod)  
    Wonderous(cr, wonderous)   
    Artifact(cr, artifact)   
    Cursed(cr, cursed)   
    Intelligent(cr, intelligent)
    return details

print("hoard or encounter?\n")
typeTreasure = ""
typeTreasure << input().lower()
print("\ncr?\n")
cr = 0
cr << int(input())
print("\nFile name?\n")
fileName = ""
fileName << input()
fileName = "%s%s" % (fileName, ".txt")
oFile = open(fileName, "w")

if typeTreasure == "hoard" :
    artifact = 0
    cursed = 0
    intelligent = 0
    print("\nartifact override number?(default: 0)\n")
    artifact << int(input())
    print("\ncursed override number?(default: 0)\n")
    cursed << int(input())
    print("\nintelligent override number?(default: 0)\n")
    intelligent << int(input())
    details = HoardTreasure(cr, currency = .5, artObj = .5, specialMats = .5, normEquip = 1,
                  magicEquip = .5, pots = .5, scroll = .5, wandStaff = .25, rod = .25,
                  wonderous = .25, artifact = artifact, cursed = cursed, intelligent = intelligent)
else :
    artifact = 0
    cursed = 0
    intelligent = 0
    print("\nartifact override number?(default: 0)\n")
    artifact << int(input())
    print("\ncursed override number?(default: 0)\n")
    cursed << int(input())
    print("\nintelligent override number?(default: 0)\n")
    intelligent << int(input())
    details = EncouterTreasure(cr, currency = 1, artObj = 1, specialMats = 1, normEquip = 1,
                     magicEquip = 1, pots = 1, scroll = 1, wandStaff = .5, rod = .5,
                     wonderous = .5, artifact = artifact, cursed = cursed, intelligent = intelligent)
