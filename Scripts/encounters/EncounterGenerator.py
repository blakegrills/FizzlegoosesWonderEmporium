import random
import TreasureGenerator
def Abberation(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "small"
    diceNum = 1
    if cr < 8 and cr > 4 :
        size = "medium"
        diceNum = 2
    elif cr == 8 or cr < 17 :
        size = "large"
        diceNum = 3
    else :
        size = "huge"
        diceNum = 4

    if name != None :
        details = "%s%s" % (name, "\nAbberation\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Abberation\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 12 + int(cr*.5)
    dexterity = 10 + int(cr*.333)
    constitution = 12 + int(cr*.333)
    intelligence = 10 + int(cr*.25)
    wisdom = 12 + int(cr*.5)
    charisma = 10 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), alignment, " ", " Move: ", (20 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.2)))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(3, 6, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*.75)
    fortitude = int(cr*.333) + (int((constitution-10)/2))
    reflex = int(cr*.333) + (int((dexterity-10)/2))
    will = int(cr*.666) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 6, 1)
    if attackNum == 1 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " tenticle slam ", diceNum, "d6+", int((int((strength-10)/2))*2), "\n")
    if attackNum == 2 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d4+", int((int((strength-10)/2))*2), "\n")
    elif attackNum == 3:
        details = "%s%s%s%s%s%s%s%s%s%s" % (details, (diceNum + 1), " +", (baseAttack+(int((strength-10)/2))), " tenticle whip ", diceNum, "d3+", int((int((strength-10)/2))*.5), " plus grab", "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " screech ", (diceNum + 3), "d4", " 20ft sonic cone", "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*3)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 5, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Maddening Gaze(Su): Will saving throw DC ", (int(cr/2) + 2 + (int((wisdom-10)/2))), ". Effects any target\nwithin 30ft line of sight.",
                        " Dealing 1d3 intelligence damage.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Sleep Gas(Ex): Fortitude saving throw DC ", (int(cr/2) + (int((wisdom-10)/2))), ". Effects any target\nwithin 15ft cone.",
                        " Causing targets to sleep for 1d6 + 1 rounds.\n")
    if 3 in specialAttack :
        details = "%s%s%s%s%s%s" % (details, "Nightmere(Su): Will saving throw DC ", (int(cr/2) + (int((wisdom-10)/2))), ". Effects any target\nwithin 60ft line of sight who is asleep.",
                        " Allows the Abberation to enter a sleeping persons dreams.\n While inside the nightmare the Abberation has half its normal hitpoints \n",
                            "but all damage it deals is doubled.\n")
    if 4 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Bleeding Barbs(Su): Reflex saving throw DC ", (int(cr/2) + (int((wisdom-10)/2))), ". Fires 4 barbs\nwithin 60ft line of sight.",
                        " Dealing 1d4 bleed damage per barb.\nBarbs may be fired against multiple opponents.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/silver\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 120ft\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Spell Resistance: ", (10 + cr), "\n")
    if 4 in specialAttack :
        details = "%s%s%s%s%s%s" % (details, "Energy Resistance(", temp, ") ", (5 + cr), "\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Ethereal\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Invisibility\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Amorphous (Ex) The creature’s body is malleable and shapeless. It is immune to precision damage (like sneak attacks) and critical hits.\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Amphibious (Ex) Creatures with this special quality have the aquatic subtype, but they can survive indefinitely on land.\n")
    if 10 in specialAttack :
        details = "%s%s" % (details, "Fast Healing 5\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = (cr - 10), specialMats = (cr - 10), normEquip = (cr - 10),
                                                    magicEquip = (cr - 10), pots = (cr - 10), scroll = (cr - 10), wand = (cr - 10), staff = (cr - 10), rod = (cr - 10), ring = (cr - 10),
                                                    wonderous = (cr - 10), artifact = (cr - 10), cursed = cr, intelligent = (cr - 10)))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details

def Dragon(enviroment, cr, temp, name = None) :
    #Prereq
    if cr < 10 :
        if name != None :
            SaveMonster(enviroment, cr, temp, name)
        else :
            Encounter(enviroment, cr, temp)

    #Name, Type and location block
    cr = cr + 2
    details = ""
    size = "large"
    diceNum = 2
    if cr > 13 and cr < 16 :
        size = "huge"
        diceNum = 3
    elif cr == 16 or cr < 19 :
        size = "gargantuan"
        diceNum = 5
    else :
        size = "colossal"
        diceNum = 7

    if name != None :
        details = "%s%s" % (name, "\nDragon\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Dragon\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 16 + int(cr*.75)
    dexterity = 10 - int(cr*.333)
    constitution = 12 + int(cr*.5)
    intelligence = 10 + int(cr*.333)
    wisdom = 12 + int(cr*.333)
    charisma = 10 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: 40", " Fly: ", (60 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.9)))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(6, 9, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*1)
    fortitude = int(cr*.666) + (int((constitution-10)/2))
    reflex = int(cr*.666) + (int((dexterity-10)/2))
    will = int(cr*.666) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 6, 1)
    if attackNum == 1 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d8+", int((int((strength-10)/2))*2), "\n")
    if attackNum == 2 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "2 +", (baseAttack+(int((strength-10)/2))), " claw ", diceNum, "d4+", int((int((strength-10)/2))), "\n")
    elif attackNum == 3:
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " tailslap ", diceNum, "d6+", int((int((strength-10)/2))*1.5), "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " slam ", diceNum, "d12", " then goes prone", "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*4)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 5, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s%s%s%s%s%s%s" % (details, "Breath Attack(Su): Reflex saving throw DC ", (int(cr/2) + 2 + (int((constitution-10)/2))), ". Effects any target\nwithin 60ft cone.",
                        (diceNum+6), "d6 ", temp, " damage.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Sleep Gas(Ex): Fortitude saving throw DC ", (int(cr/2) + (int((constitution-10)/2))), ". Effects any target\nwithin 30ft cone.",
                        " Causing targets to sleep for 1d6 + 1 rounds.\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Poison Fortitude saving throw DC: ", (int(cr/2) + 2 + (int((constitution-10)/2))), " sting frequency 6 rnds, effect 1d4 CON, cure 2 consecutive saves\n")
    if 4 in specialAttack :
        details = "%s%s%s" % (details, "Wind Storm(Su): creates a cylinder of wind 60 feet tall with a radius of 30 feet which can not\n",
            "and slows movement by half when passing through it be penetrated by projectiles\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 10/magic\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 120ft\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Spell Resistance: ", (15 + cr), "\n")
    if 4 in specialAttack :
        details = "%s%s%s%s%s%s" % (details, "Energy Resistance(", temp, ") ", (5 + cr), "\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Blind Sense\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Invisibility\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Fast Swallow\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Fortification (Ex) The monster has an 50 percent chance to treat any critical hit or \nsneak attack as a normal hit, as if wearing moderate fortif ication armor.\n")
    if 10 in specialAttack :
        details = "%s%s" % (details, "Fast Healing 5\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = (cr + 10), specialMats = (cr + 10), normEquip = (cr + 10),
                                                    magicEquip = (cr + 10), pots = (cr + 10), scroll = (cr + 10), wand = (cr + 10), staff = (cr + 10), rod = (cr + 10), ring = (cr + 10),
                                                    wonderous = (cr + 10), artifact = cr, cursed = cr, intelligent = cr))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Undead(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "small"
    diceNum = 1
    if cr < 10 and cr > 1 :
        size = "medium"
    elif cr == 10 or cr < 18 :
        size = "large"
        diceNum = 2
    else :
        size = "huge"
        diceNum = 3

    if name != None :
        details = "%s%s" % (name, "\nUndead\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Undead\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 10 + int(cr*.5)
    dexterity = 10
    constitution = 0
    intelligence = 0
    wisdom = 10 + int(cr*.25)
    charisma = 12 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: ", (20 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.333)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(4, 7, 1)) + (int((charisma-10)/2)*cr))
    baseAttack = int(cr*.5)
    fortitude = int(cr*1) + (int((charisma-10)/2))
    reflex = int(cr*0) + (int((dexterity-10)/2))
    will = int(cr*.666) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 4, 1)
    if attackNum == 1 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " slam ", diceNum, "d8+", int((int((strength-10)/2))*2), "\n")
    elif attackNum == 2 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d4+", int((int((strength-10)/2))), "\n")
    else :
        details = "%s%s%s%s%s%s%s%s%s%s" % (details, 2, " +", (baseAttack+(int((strength-10)/2))), " claw ", diceNum, "d3+", int((int((strength-10)/2))*.5), " plus grab", "\n")


    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*2)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 4, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s%s%s" % (details, "Poison Fortitude saving throw DC: ", (int(cr/2) + 2 + (int((constitution-10)/2))), " sting frequency 3 rnds, effect 1d2 CON, cure 1 consecutive save.\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "Feat of strength: doubles strength for 1d4 + 1 rounds.\n")
    if 3 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Bleeding Barbs(Su): Reflex saving throw DC ", (int(cr/2) + (int((wisdom-10)/2))), ". Fires 3 barbs\nwithin 30ft line of sight.",
                        " Dealing 1d4 bleed damage per barb.\nBarbs may be fired against multiple opponents.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/cold iron\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 120ft\n")
    if 3 in specialAttack :
        details = "%s%s" % (details, "Channel Resistance +4 (Ex) A creature with this special quality (usually an undead) is less easily \naffected by clerics or paladins. A creature with channel resistance adds the bonus listed for that creature to saves made to resist \nthe effects of channel energy, including effects that rely on the use of channel energy (such as the Command Undead feat).\n")
    if 4 in specialAttack :
        details = "%s%s" % (details, "Burrow (Ex) A creature with a burrow speed can tunnel through dirt\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Ethereal\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Regeneration/Acid or Fire\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Fear Aura 15ft (Su) The use of this ability is a free action. The aura functions like\nthe fear spell. A fear aura is an area effect.\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Lifesense (Su) The creature notices and locates living creatures within 60 feet, \njust as if it possessed the blindsight ability.\n")
    if 10 in specialAttack :
        details = "%s%s" % (details, "Fast Healing 3\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = (cr - 50), specialMats = (cr - 50), normEquip = (cr - 10),
                                                    magicEquip = (cr - 10), pots = (cr - 50), scroll = (cr - 50), wand = (cr - 50), staff = (cr - 50), rod = (cr - 50), ring = (cr - 10),
                                                    wonderous = (cr - 50), artifact = (cr - 100), cursed = cr, intelligent = (cr - 100)))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Fey(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "medium"
    diceNum = 1
    if cr < 8 and cr > 4 :
        size = "small"
        diceNum = 1
    else :
        size = "tiny"
        diceNum = 1

    if name != None :
        details = "%s%s" % (name, "\nFey\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Fey\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 10 - int(cr*.1)
    dexterity = 12 + int(cr*.5)
    constitution = 10 + int(cr*.2)
    intelligence = 10 + int(cr*.25)
    wisdom = 12 + int(cr*.25)
    charisma = 12 + int(cr*.5)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, "Move: 15ft", " Fly: ", (30 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.1) + int((charisma-10)/2)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(3, 6, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*.5)
    fortitude = int(cr*.333) + (int((constitution-10)/2))
    reflex = int(cr*.666) + (int((dexterity-10)/2))
    will = int(cr*.666) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 3, 1)
    if attackNum == 1 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " claw ", diceNum, "d4+", int((int((strength-10)/2))*.5), "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d2+", int((int((strength-10)/2))*.5), "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*2)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 4, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Maddening Gaze(Su): Will saving throw DC ", (int(cr/2) + 2 + (int((charisma-10)/2))), ". Effects any target\nwithin 30ft line of sight.",
                        " Dealing 1d3 intelligence damage.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Charming Gaze(Su): Will saving throw DC ", (int(cr/2) + 2 + (int((charisma-10)/2))), ". Effects any target\nwithin 30ft line of sight.",
                        " functions like spell charm person.\n")
    if 3 in specialAttack :
        details = "%s%s" % (details, "Change Shape (Su) A creature with this special quality has the ability to assume \nthe appearance of a specific creature or type of creature (usually a humanoid), \nbut retains most of its own physical qualities. A creature cannot change shape to a \nform more than one size category smaller or larger than its original form. This ability \nfunctions as a polymorph spell, the type of which is listed in the creature’s description, \nbut the creature does not adjust its ability scores (although it gains any other abilities of the creature it mimics).\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 9, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/cold iron\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "Darkvision 60ft\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Spell Resistance: ", (10 + cr), "\n")
    if 4 in specialAttack :
        details = "%s%s" % (details, "low-light vision 60ft\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Mistsight (Ex) The monster can see through fog, mist, and murky water as if they \nwere perfectly clear, ignoring the miss chance for these obstructions, up to its normal range of vision.\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Invisibility\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Thoughtsense(Su) Creatures with this ability automatically detect and locate conscious \ncreatures within the specified range (usually 60 feet). This ability functions similarly to blindsight.\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Create a 60ft radius area of mist for 1d4 minutes.\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = cr, specialMats = cr, normEquip = cr,
                                                    magicEquip = cr, pots = cr, scroll = cr, wand = cr, staff = cr, rod = cr, ring = cr,
                                                    wonderous = cr, artifact = cr, cursed = cr, intelligent = cr))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Animal(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "small"
    diceNum = 1
    if cr < 6 and cr > 4 :
        size = "medium"
        diceNum = 1
    elif cr == 6 or cr < 16 :
        size = "large"
        diceNum = 2
    else :
        size = "huge"
        diceNum = 3

    if name != None :
        details = "%s%s" % (name, "\nAnimal\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Animal\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 12 + int(cr*.5)
    dexterity = 10 + int(cr*.333)
    constitution = 12 + int(cr*.5)
    intelligence = 2
    wisdom = 12 + int(cr*.5)
    charisma = 7 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: ", (20 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.5)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(3, 6, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*.333)
    fortitude = int(cr*.666) + (int((constitution-10)/2))
    reflex = int(cr*.333) + (int((dexterity-10)/2))
    will = int(cr*.666) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 4, 1)
    if attackNum == 1 or attackNum == 3 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d6+", int((int((strength-10)/2))*1.5), "\n")
    if attackNum == 2 or attackNum == 3 :
        details = "%s%s%s%s%s%s%s%s" % (details, "2 +", (baseAttack+(int((strength-10)/2))), " claw ", diceNum, "d4+", int((int((strength-10)/2))), "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"    
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 4, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s" % (details, "Pounce: make a full attack after a charge.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s" % (details, "Poison Fortitude saving throw DC: ", (int(cr/2) + 2 + (int((constitution-10)/2))), " sting frequency 3 rnds, effect 1d2 CON, cure 1 consecutive save.\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Bleeding Strike(Ex): Fortitude saving throw DC ", (int(cr/2) + (int((strength-10)/2))), ". \nadds 1d4 bleed damage to natural attacks.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/mithril\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 90ft\n")
    if 3 in specialAttack :
        details = "%s%s" % (details, "Climb: climb speed equal to move speed\n")
    if 4 in specialAttack :
        details = "%s%s" % (details, "low-light vision 90ft\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Burrow (Ex) A creature with a burrow speed can tunnel through dirt\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Flight: fly speed equal to twice move speed\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Tremorsense (Ex)A creature with tremorsense is sensitive to vibrations in \nthe ground and can automatically pinpoint the location of anything that is in contact with the ground.\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Amphibious (Ex) Creatures with this special quality have the aquatic subtype, but they can survive indefinitely on land.\n")
    if 10 in specialAttack :
        details = "%s%s%s%s" % (details, "Web (Ex) Creatures with the web ability can use webs to support themselves \nand up to one additional creature of the same size. In addition, such creatures can throw a web up to \neight times per day. This is similar to an attack with a net but has a maximum range of 50 feet, \nwith a range increment of 10 feet, and is effective against targets up to one size category larger than the \nweb spinner. An entangled creature can escape with a successful Escape Artist check or burst \nthe web with a Strength check. Both are standard actions with a DC equal to ", (10 + int(cr*2) + (int((constitution-10)/2))), "\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = (cr - 50), artObj = (cr - 50), specialMats = (cr - 50), normEquip = (cr - 50),
                                                    magicEquip = (cr - 50), pots = (cr - 50), scroll = (cr - 50), wand = (cr - 50), staff = (cr - 50), rod = (cr - 50), ring = (cr - 50),
                                                    wonderous = (cr - 50), artifact = (cr - 100), cursed = (cr + 100), intelligent = (cr - 100)))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def MagicalBeast(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "medium"
    diceNum = 1
    if cr < 10 and cr > 4 :
        size = "large"
        diceNum = 2
    elif cr == 10 or cr < 17 :
        size = "huge"
        diceNum = 3
    else :
        size = "gargantuan"
        diceNum = 5

    if name != None :
        details = "%s%s" % (name, "\nMagical Beast\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Magical Beast\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 12 + int(cr*.5)
    dexterity = 10 + int(cr*.333)
    constitution = 12 + int(cr*.333)
    intelligence = 10 + int(cr*.25)
    wisdom = 10 + int(cr*.5)
    charisma = 10 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: ", (30 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.5)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(3, 6, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*.75)
    fortitude = int(cr*.666) + (int((constitution-10)/2))
    reflex = int(cr*.666) + (int((dexterity-10)/2))
    will = int(cr*.333) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 5, 1)
    if attackNum == 1 or attackNum == 3 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " bite ", diceNum, "d6+", int((int((strength-10)/2))*1.5), "\n")
    if attackNum == 2 or attackNum == 3 :
        details = "%s%s%s%s%s%s%s%s" % (details, "2 +", (baseAttack+(int((strength-10)/2))), " claw ", diceNum, "d4+", int((int((strength-10)/2))), "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " gore ", diceNum, "d8+", int((int((strength-10)/2))*2), "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*2)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 5, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s" % (details, "Pounce: make a full attack after a charge.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s" % (details, "Poison Fortitude saving throw DC: ", (int(cr) + 2 + (int((constitution-10)/2))), " sting frequency 3 rnds, effect 1d2 CON, cure 1 consecutive save.\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Bleeding Strike(Ex): Fortitude saving throw DC ", (int(cr/2) + (int((strength-10)/2))), ". \nadds 2d4 bleed damage to natural attacks.\n")
    if 4 in specialAttack :
        details = "%s%s%s%s%s%s%s%s" % (details, "Breath Attack(Su): Reflex saving throw DC ", (int(cr/2) + (int((constitution-10)/2))), ". Effects any target\nwithin 30ft cone.",
                        (diceNum+1), "d4 ", temp, " damage.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/magic\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 90ft\n")
    if 3 in specialAttack :
        details = "%s%s" % (details, "Climb: climb speed equal to move speed\n")
    if 4 in specialAttack :
        details = "%s%s" % (details, "low-light vision 90ft\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Burrow (Ex) A creature with a burrow speed can tunnel through dirt\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Flight: fly speed equal to twice move speed\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s%s%s%s%s" % (details, "Energy Resistance(", temp, ") ", (5 + cr), "\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Blind Sense\n")
    if 10 in specialAttack :
        details = "%s%s" % (details, "Invisibility\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = (cr - 50), artObj = (cr - 50), specialMats = (cr - 50), normEquip = (cr - 50),
                                                    magicEquip = (cr - 50), pots = (cr - 50), scroll = (cr - 50), wand = (cr - 50), staff = (cr - 50), rod = (cr - 50), ring = (cr - 50),
                                                    wonderous = (cr - 50), artifact = (cr - 100), cursed = (cr + 100), intelligent = (cr - 100)))
    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Giant(enviroment, cr, temp, name = None) :
    #Prereq
    if cr < 8 :
        if name != None :
            SaveMonster(enviroment, cr, temp, name)
        else :
            Encounter(enviroment, cr, temp)

    #Name, Type and location block
    details = ""
    size = "large"
    diceNum = 2
    if cr < 16 and cr > 13 :
        size = "huge"
        diceNum = 3
    else :
        size = "gargantuan"
        diceNum = 5


    if name != None :
        details = "%s%s" % (name, "\nGiant\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "Giant\n"
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 16 + int(cr*.5)
    dexterity = 8 + int(cr*.25)
    constitution = 14 + int(cr*.333)
    intelligence = 10 + int(cr*.25)
    wisdom = 10 + int(cr*.25)
    charisma = 6 + int(cr*.25)

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: ", (30 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2) + int(cr*.666)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(5, 8, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*1)
    fortitude = int(cr*.666) + (int((constitution-10)/2))
    reflex = int(cr*.333) + (int((dexterity-10)/2))
    will = int(cr*.333) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 6, 1)
    if attackNum == 1 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " Great Axe ", diceNum, "d12+", int((int((strength-10)/2))*1.5), "\n")
    if attackNum == 2 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((dexterity-10)/2))), " rock throw ", diceNum, "d8+", int((int((strength-10)/2))*2), "\n")
    elif attackNum == 3:
        details = "%s%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " slam ", diceNum + 1, "d10+", int((int((strength-10)/2))*1.5), " plus grab", "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " club ", diceNum - 1, "d8+", int((int((strength-10)/2))), "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr*3)
    specialAttack = []
    if temp == "cold" :
        temp = "ice"
    if temp == "temperate" :
        temp = "acid"
    if temp == "hot" :
        temp = "fire"
    while specialBlocks > 75 :
        specialAttack.append(random.randrange(1, 3, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s" % (details, "Feat of strength: doubles strength for 1d4 + 1 rounds.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s%s%s%s%s" % (details, "Breath Attack(Su): Reflex saving throw DC ", (int(cr/2) + (int((constitution-10)/2))), ". Effects any target\nwithin 30ft cone.",
                        (diceNum+1), "d4 ", temp, " damage.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 50 :
        specialAttack.append(random.randrange(1, 11, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "Damage reduction 5/adamantine\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 90ft\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Spell Resistance: ", (10 + cr), "\n")
    if 4 in specialAttack :
        details = "%s%s%s%s%s%s" % (details, "Energy Resistance(", temp, ") ", (5 + cr), "\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Regeneration/Acid or Fire\n")
    if 6 in specialAttack :
        details = "%s%s" % (details, "Fear Aura 30ft (Su) The use of this ability is a free action. The aura functions like\nthe fear spell. A fear aura is an area effect.\n")
    if 7 in specialAttack :
        details = "%s%s" % (details, "Scent\n")
    if 8 in specialAttack :
        details = "%s%s" % (details, "Blood Rage (Ex) When the creature takes damage in combat, on its next turn it can fly \ninto a rage as a free action. It gains +2 Constitution and +2 Strength, but takes a –2 penalty to its  AC. \nThe rage lasts as long as the battle or 1 minute, whichever is shorter. It cannot end its rage voluntarily.\n")
    if 9 in specialAttack :
        details = "%s%s" % (details, "Ferocity (Ex) A creature with ferocity remains conscious and can continue fighting even \nif its hit point total is below 0. The creature is still staggered and loses 1 hit point each round. A \ncreature with ferocity still dies when its hit point total reaches a negative amount equal to its Constitution score.\n")
    if 10 in specialAttack :
        details = "%s%s" % (details, "Fast Healing 5")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = (cr + 10), specialMats = (cr + 10), normEquip = (cr + 10),
                                                    magicEquip = (cr + 10), pots = (cr + 10), scroll = (cr + 10), wand = (cr + 10), staff = (cr + 10), rod = (cr + 10), ring = (cr + 10),
                                                    wonderous = (cr + 10), artifact = cr, cursed = cr, intelligent = cr))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Humanoid(enviroment, cr, temp, name = None) :
    #Name, Type and location block
    details = ""
    size = "medium"
    diceNum = 1
    subType = ""
    num = random.randrange(1, 11, 1)
    if num == 1 :
        subType = "human"
    elif num == 2 :
        subType = "dwarf"
    elif num == 3 :
        subType = "gnome"
        size = "small"
    elif num == 4 :
        subType = "elf"
    elif num == 5 :
        subType = "orc"
    elif num == 6 :
        subType = "half-orc"
    elif num == 7 :
        subType = "half-elf"
    elif num == 8 :
        subType = "goblin"
        size = "small"
    elif num == 9 :
        subType = "lizardfolk"
    else :
        subType = "changling"
    if name != None :
        details = "%s%s%s%s" % (name, "\nHumanoid(", subType, ")\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")
    else :
        details = "%s%s%s" % ("Humanoid(", subType, ")\n")
        details = "%s%s%s%s%s%s%s%s %s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", temp, enviroment, "\n", "--------------------------------------------\n")

    #Stat Block
    strength = 10 + int(cr*.15)
    dexterity = 10 + int(cr*.15)
    constitution = 10 + int(cr*.15)
    intelligence = 10 + int(cr*.15)
    wisdom = 10 + int(cr*.15)
    charisma = 10 + int(cr*.15)

    if subType == "human" :
        strength = strength + 2
    elif subType == "dwarf" :
        constitution = constitution + 2
    elif subType == "gnome" :
        intelligence = intelligence + 2
    elif subType == "elf" :
        dexterity = dexterity + 2
    elif subType == "orc" :
        strength = strength + 4
    elif subType == "half-orc" :
        strength = strength + 2
    elif subType == "half-elf" :
        dexterity = dexterity + 2
    elif subType == "goblin" :
        dexterity = dexterity + 4
    elif subType == "lizardfolk" :
        constitution = constitution + 4
    else :
        charisma = charisma + 2

    alignment = ""
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "L")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "C")
    alignmentNum = random.randrange(1, 4, 1)
    if alignmentNum == 1:
        alignment = "%s%s" % (alignment, "G")
    elif alignmentNum == 2:
        alignment = "%s%s" % (alignment, "N")
    else :
        alignment = "%s%s" % (alignment, "E")

    details = "%s%s%s%s%s%s%s%s" % (details, "INIT: +", (int((dexterity-10)/2)), " ", alignment, " Move: ", (20 + (diceNum*10)), "ft\n")

    details = "%s%s%s" % (details, " AC: ", (10 + int((dexterity-10)/2)))
    
    details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Str: ", strength, " Dex: ", dexterity, " Con: ", constitution, " Int: ", intelligence, " Wis: ", wisdom, " Cha: ", charisma, "\n")

    health = int((cr*random.randrange(2, 5, 1)) + (int((constitution-10)/2)*cr))
    baseAttack = int(cr*.25)
    fortitude = int(cr*.333) + (int((constitution-10)/2))
    reflex = int(cr*.333) + (int((dexterity-10)/2))
    will = int(cr*.333) + (int((wisdom-10)/2))

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")

    #Attack Block
    attackNum = random.randrange(1, 6, 1)
    if attackNum == 1 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " Great sword ", diceNum + 1, "d6+", int((int((strength-10)/2))*1.5), "\n")
    if attackNum == 2 or attackNum == 5 :
        details = "%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((dexterity-10)/2))), " long Bow ", diceNum, "d8", "\n")
    elif attackNum == 3:
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((strength-10)/2))), " longsword ", diceNum, "d8+", int((int((strength-10)/2))), "\n")
    else :
        details = "%s%s%s%s%s%s%s%s" % (details, "+", (baseAttack+(int((dexterity-10)/2))), " dagger ", diceNum, "d4+", int((int((strength-10)/2))*.5), "\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Attack Block
    specialBlocks = random.randrange(1, 101, 1) + (cr)
    specialAttack = []
    while specialBlocks > 70 :
        specialAttack.append(random.randrange(1, 4, 1))
        specialBlocks = specialBlocks - 10

    if 1 in specialAttack :
        details = "%s%s" % (details, "spellcasting.\n")
    if 2 in specialAttack :
        details = "%s%s%s%s%s" % (details, "Sneak attack:", int(cr*.333), "d6","\n")
    if 3 in specialAttack :
        details = "%s%s%s%s" % (details, "Poison Fortitude saving throw DC: ", (int(cr*.2) + 12), " frequency 3 rnds, effect 1d2 STR, cure 1 consecutive save.\n")

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    #Special Ability Block
    specialAttack = []
    while specialBlocks > 60 :
        specialAttack.append(random.randrange(1, 6, 1))
        specialBlocks = specialBlocks - 5

    if 1 in specialAttack :
        details = "%s%s" % (details, "low-light vision 60ft\n")
    if 2 in specialAttack :
        details = "%s%s" % (details, "darkvision 60ft\n")
    if 3 in specialAttack :
        details = "%s%s" % (details, "Ferocity (Ex) A creature with ferocity remains conscious and can continue fighting even \nif its hit point total is below 0. The creature is still staggered and loses 1 hit point each round. A \ncreature with ferocity still dies when its hit point total reaches a negative amount equal to its Constitution score.\n")
    if 4 in specialAttack :
        details = "%s%s" % (details, "Light Sensitivity (Ex) Creatures with light sensitivity are dazzled in areas of \nbright sunlight or within the radius of a daylight spell.\n")
    if 5 in specialAttack :
        details = "%s%s" % (details, "Sound Mimicry (Ex) The creature perfectly imitates certain sounds or even specific \nvoices. The creature makes a Bluff check opposed by the listener’s Sense Motive check to recognize the mimicry, \nalthough if the listener isn’t familiar with the person or type of creatures mimicked, it takes a –8 penalty on its \nSense Motive check. The creature has a +8 racial bonus on its Bluff check to mimic sounds \n(including accents and speech patterns, if a voice mimic) it has listened to for at least 10 minutes\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = cr, specialMats = cr, normEquip = cr,
                                                    magicEquip = cr, pots = cr, scroll = cr, wand = cr, staff = cr, rod = cr, ring = cr,
                                                    wonderous = cr, artifact = cr, cursed = cr, intelligent = cr))

    details = "%s%s" % (details, "\n--------------------------------------------\n")

    return details
    
def Encounter(enviroment, cr, temp) :
    print("Mass, Single, Weak, Boss")
    encounterDif = ""
    encounterDif = input().lower()
    monType = random.randrange(1, 9, 1)
    if encounterDif == "mass" :
        crMod = random.randrange(2, 7, 1)
        crModLock = cr - crMod
        title = "%s%s%s%s%s%s" % (encounterDif, monType, temp, enviroment, cr, ".txt")
        oFile = open(title, "w")
        while(crMod != 0) :
            if monType == 1 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Abberation(enviroment, cr, temp)
            elif monType == 2 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Dragon(enviroment, cr, temp)
            elif monType == 3 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Undead(enviroment, cr, temp)
            elif monType == 4 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Fey(enviroment, cr, temp)
            elif monType == 5 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Animal(enviroment, cr, temp)
            elif monType == 6 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = MagicalBeast(enviroment, cr, temp)
            elif monType == 7 :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Giant(enviroment, cr, temp)
            else :
                cr = crModLock
                if cr < 1 :
                    cr = 1
                details = Humanoid(enviroment, cr, temp)

            oFile.write(details)
            oFile.write("\n*************************************************************\n")

            crMod = crMod - 1
        oFile.close()
    elif encounterDif == "single" :
        title = "%s%s%s%s%s%s" % (encounterDif, monType, temp, enviroment, cr, ".txt")
        oFile = open(title, "w")
        if monType == 1 :
            details = Abberation(enviroment, cr, temp)
        elif monType == 2 :
            details = Dragon(enviroment, cr, temp)
        elif monType == 3 :
            details = Undead(enviroment, cr, temp)
        elif monType == 4 :
            details = Fey(enviroment, cr, temp)
        elif monType == 5 :
            details = Animal(enviroment, cr, temp)
        elif monType == 6 :
            details = MagicalBeast(enviroment, cr, temp)
        elif monType == 7 :
            details = Giant(enviroment, cr, temp)
        else :
            details = Humanoid(enviroment, cr, temp)

        oFile.write(details)
        oFile.close()
    elif encounterDif == "weak" :
        if cr > 1 :
            cr = cr - 1
        title = "%s%s%s%s%s%s" % (encounterDif, monType, temp, enviroment, cr, ".txt")
        oFile = open(title, "w")
        if monType == 1 :
            details = Abberation(enviroment, cr, temp)
        elif monType == 2 :
            details = Dragon(enviroment, cr, temp)
        elif monType == 3 :
            details = Undead(enviroment, cr, temp)
        elif monType == 4 :
            details = Fey(enviroment, cr, temp)
        elif monType == 5 :
            details = Animal(enviroment, cr, temp)
        elif monType == 6 :
            details = MagicalBeast(enviroment, cr, temp)
        elif monType == 7 :
            details = Giant(enviroment, cr, temp)
        else :
            details = Humanoid(enviroment, cr, temp)

        oFile.write(details)
        oFile.close()
    else :
        cr = cr + 2
        title = "%s%s%s%s%s%s" % (encounterDif, monType, temp, enviroment, cr, ".txt")
        oFile = open(title, "w")
        if monType == 1 :
            details = Abberation(enviroment, cr, temp)
        elif monType == 2 :
            details = Dragon(enviroment, cr, temp)
        elif monType == 3 :
            details = Undead(enviroment, cr, temp)
        elif monType == 4 :
            details = Fey(enviroment, cr, temp)
        elif monType == 5 :
            details = Animal(enviroment, cr, temp)
        elif monType == 6 :
            details = MagicalBeast(enviroment, cr, temp)
        elif monType == 7 :
            details = Giant(enviroment, cr, temp)
        else :
            details = Humanoid(enviroment, cr, temp)

        oFile.write(details)
        oFile.close()

def SaveMonster(enviroment, cr, temp, monsterName) :
    print("\nAbberation, Dragon, Undead, Fey, Animal, MagicalBeast, Giant, Humanoid\n")
    monType = ""
    details = ""
    monType = input().lower()
    if monType == "abberation" :
        details = Abberation(enviroment, cr, temp, name=monsterName)
    elif monType == "dragon" :
        details = Dragon(enviroment, cr, temp, name=monsterName)
    elif monType == "undead" :
        details = Undead(enviroment, cr, temp, name=monsterName)
    elif monType == "fey" :
        details = Fey(enviroment, cr, temp, name=monsterName)
    elif monType == "animal" :
        details = Animal(enviroment, cr, temp, name=monsterName)
    elif monType == "magicalbeast" :
        details = MagicalBeast(enviroment, cr, temp, name=monsterName)
    elif monType == "giant" :
        details = Giant(enviroment, cr, temp, name=monsterName)
    else :
        details = Humanoid(enviroment, cr, temp, name=monsterName)

    nameString = "%s%s%s" % ("~", monsterName, ".txt")
    oFile = open(nameString, "w")
    oFile.write(details)
    oFile.close()

print("(S)ave Monster or (G)enerate Encounter?\n")
encounterType = ""
encounterType = input().lower()
print("\nEnviroment?(Marsh, Desert, Forest, Hills, Mountain, Plains)\n")
enviroment = ""
enviroment = input().lower()
print("\nTemperature?(Cold, Temperate, Hot)\n")
temp = ""
temp = input().lower()
print("\ncr?\n")
cr = 0
cr = int(input())

if encounterType == "s" :
    print("\nMonster name?\n")
    monsterName = ""
    monsterName = input()
    SaveMonster(enviroment, cr, temp, monsterName)
else :
    Encounter(enviroment, cr, temp)