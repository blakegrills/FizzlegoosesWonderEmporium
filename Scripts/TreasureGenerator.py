import random

def Currency(cr, currency) :
    details = ""
    possibility = currency * random.randrange(1, 101, 1)
    if possibility > 34 :
        if cr < 4 :
            copRan = int(random.randrange(1, 11, 1))
            silRan = int(random.randrange(1, 6, 1))
            golRan = int(random.randrange(0, 2, 1))
            details = "%s%s" % (details, "\n-Coins--------------------------------------\n")
            details = "%s%s%s%s%s%s%s" % (details, "copper coins: ", (copRan * 17), "\nsilver coins: ", (silRan * 8), "\ngold coins: ", (int(golRan * 10)))
            details = "%s%s" % (details, "\n-Art-Objects--------------------------------\n")
        elif cr > 3 and cr < 7 :
            copRan = int(random.randrange(1, 11, 1))
            silRan = int(random.randrange(1, 11, 1))
            golRan = int(random.randrange(0, 21, 1))
            details = "%s%s" % (details, "\n-Coins--------------------------------------\n")
            details = "%s%s%s%s%s%s%s" % (details, "copper coins: ", (copRan * 8), "\nsilver coins: ", (silRan * 13), "\ngold coins: ", (golRan * 6))
            details = "%s%s" % (details, "\n-Art-Objects--------------------------------\n")
        elif cr > 6 and cr < 13 :
            copRan = int(random.randrange(1, 11, 1))
            silRan = int(random.randrange(5, 55, 5))
            golRan = int(random.randrange(10, 110, 10))
            plaRan = int(random.randrange(0, 6, 1))
            details = "%s%s" % (details, "\n-Coins--------------------------------------\n")
            details = "%s%s%s%s%s%s%s%s%s" % (details, "copper coins: ", (copRan * 6), "\nsilver coins: ", (silRan * 19), "\ngold coins: ", (golRan * 13), "\nplatinum pieces: ", (int(plaRan * 5)))
            details = "%s%s" % (details, "\n-Art-Objects--------------------------------\n")
        elif cr > 12 and cr < 18 :
            copRan = int(random.randrange(1, 11, 1))
            silRan = int(random.randrange(15, 70, 5))
            golRan = int(random.randrange(100, 520, 20))
            plaRan = int(random.randrange(0, 26, 5))
            details = "%s%s" % (details, "\n-Coins--------------------------------------\n")
            details = "%s%s%s%s%s%s%s%s%s" % (details, "copper coins: ", (copRan * 11), "\nsilver coins: ", (silRan * 12), "\ngold coins: ", (golRan * 16), "\nplatinum pieces: ", (int(plaRan * 5)))
            details = "%s%s" % (details, "\n-Art-Objects--------------------------------\n")
        else :
            copRan = int(random.randrange(1, 11, 1))
            silRan = int(random.randrange(15, 70, 5))
            golRan = int(random.randrange(100, 520, 20))
            plaRan = int(random.randrange(5, 26, 5))
            details = "%s%s" % (details, "\n-Coins--------------------------------------\n")
            details = "%s%s%s%s%s%s%s%s%s" % (details, "copper coins: ", (copRan * 17), "\nsilver coins: ", (silRan * 21), "\ngold coins: ", (2*cr*golRan * 16), "\nplatinum pieces: ", (cr*int(plaRan * 5)))
            details = "%s%s" % (details, "\n-Art-Objects--------------------------------\n")

    return details    

def ArtObj(cr, artObj) :
    details = ""
    artObjList = ["Alabaster", "Amber", "Amethyst", "Aquamarine", "Azurite", "Bejeweled sword of state", "Black Pearl", "Bloodstone", "Book of lost songs by a famous bard", 
                    "Brilliant Green Emerald", "Bronze flagon with warrior images", "Bronze statuette of a warrior", "Carnelian", "Carved ivory scroll case", 
                    "Carved jade idol", "Carved saint's femur", "Carved stone idol", "Chrysoberyl", "Chrysoprase", "Citrine", "Copper and glass decanter", 
                    "Copper brazier with religious markings", "Copper scepter with gold inlay", "Coral", "Crystal egg with silver stand", "Crystal skull", 
                    "Crystallized dragon heart", "Darkwood and platinum music box", "Decorated electrum plate", "Decorated gold plate", "Decorated silver plate", 
                    "Deep Blue Spinel", "Elaborate copper wind chimes", "Elaborate silver wind chimes", "Electrum censer with silver filigree", "Emerald", 
                    "Engraved gold scarab", "Engraved jade scarab", "Engraved mithral scarab", "Engraved platinum scarab", "Garnet", "Gilded demon skull", 
                    "Glowing metallic meteor", "Gold and ivory decanter", "Gold and mithral baby rattle", "Gold and mithral chess set", "Gold and platinum orrery", 
                    "Gold and platinum statuette of a deity", "Gold and silver chess set", "Gold and silver hand mirror", "Gold baby rattle", "Gold bejeweled royal orb", 
                    "Gold bowl with dragon engravings", "Gold candelabra with holy symbol", "Gold cauldron with alchemical symbols", "Gold censer with platinum inlay", 
                    "Gold censer with silver filigree", "Gold chalice with griffon carvings", "Gold chess set", "Gold cup with royal crest", 
                    "Gold decanter with grape vine patterns", "Gold flagon with religious markings", "Gold flute", "Gold holy symbol", "Gold idol with strange carvings", 
                    "Gold mask", "Gold puzzle box", "Gold statue of a dragon", "Gold statue of a lion", "Gold urn containing hero's ashes", "Green Spinel", 
                    "Helm carved from a pit fiend skull", "Hematite", "Holy text penned by a saint", "Ivory", "Ivory bowl with animal carvings", 
                    "Ivory drinking horn with copper ends", "Ivory drinking horn with silver ends", "Jade", "Jasper", "Jet", "Jeweled egg with epic sorcerer's blood", 
                    "Lapis Lazuli", "Large Diamond", "Large Ruby", "Malachite", "Marble idol", "Milky Quartz", "Mithral hourglass with diamond dust", 
                    "Mithral scepter with gold inlay", "Moonstone", "Obsidian", "Onyx", "Opal", "Painted paper fan with silver slats", "Painted silk fan with electrum slats", 
                    "Painting of a beloved queen by a master", "Painting of a noblewoman", "Painting of a princess", "Painting of a queen", "Painting of a queen by a master", 
                    "Peridot", "Platinum bowl with arcane engravings", "Platinum cauldron with odd symbols", "Platinum censer with ornate markings", 
                    "Platinum chalice blessed by a saint", "Platinum chalice with angel carvings", "Platinum cup with royal crest", "Platinum flagon with religious markings", 
                    "Platinum holy symbol", "Platinum idol with mysterious markings", "Platinum mask", "Platinum scepter with gold inlay", "Platinum statuette of a deity", 
                    "Polished darkwood chalice", "Porcelain mask", "Preserved beast head on a plaque", "Red Spinel", "Rhodochrosite", "Rose Quartz", "Saltwater Pearl", "Sapphire", 
                    "Sard", "Sardonyx", "Set of six ivory dice", "Set of six silver dice", "Shell", "Silver and glass decanter", "Silver baby rattle", 
                    "Silver bowl with lion engravings", "Silver brazier with religious markings", "Silver candelabra with holy symbol", "Silver cauldron with animal symbols", 
                    "Silver chalice with dragon carvings", "Silver chess set", "Silver comb with gold handle", "Silver comb with ornate handle", "Silver cup with royal crest", 
                    "Silver egg with dragon figurine", "Silver flagon with religious markings", "Silver hand mirror", "Silver holy symbol", "Silver mask", "Silver noble family seal", 
                    "Silver scepter with eagle symbols", "Silver statue of a dragon", "Small Diamond", "Small Ruby", "Smoky Quartz", "Star Sapphire", "Tigereye", "Topaz", 
                    "Tourmaline", "Turquoise", "Zircon"]
    maxVal = int((cr+1)/2)+1
    numArtObj = random.randrange(1, maxVal, 1)
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
        if cr < 4 :
            while numArtObj > 0 :
                value = random.randrange(1, 50, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, 155, 1))], " (", value * 10, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 8 :
            while numArtObj > 0 :
                value = random.randrange(1, 50, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, 155, 1))], " (", value * 15, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 12 :
            while numArtObj > 0 :
                value = random.randrange(1, 50, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, 155, 1))], " (", value * 30, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 16 :
            while numArtObj > 0 :
                value = random.randrange(1, 75, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, 155, 1))], " (", value * 45, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        else :
            while numArtObj > 0 :
                value = random.randrange(1, 100, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, 155, 1))], " (", value * 60, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")

            
    return details    

def SpecialMats(cr, specialMats) :
    details = ""
    specialMatsList = ["cold iron", "darkwood", "silver", "mithril", "adamantine", "silversheen", "sky metal", "spire steel", "cold-forged steel", "fire-forged steel", "living steel", "forging stone", "wyr root"]
    if cr < 4 :
        specialMatsCount = random.randrange(0, cr, 1)
    elif cr < 8 :
        specialMatsCount = random.randrange(0, int(cr*1.5), 1)
    elif cr < 12 :
        specialMatsCount = random.randrange(0, int(cr*2), 1)
    elif cr < 16 :
        specialMatsCount = random.randrange(0, int(cr*2.5), 1)
    else :
        specialMatsCount = random.randrange(0, int(cr*3), 1)
    possibility = specialMats * random.randrange(1, 101, 1)
    if possibility > 34 :
        while specialMatsCount > 0 :
            details = "%s%s%s%s" % (details, int(cr*.75), " lbs of", specialMatsList[random.randrange(0, 13, 1)])
    details = "%s%s" % (details, "\n-Normal-Equipment---------------------------\n")
    return details    

def NormEquip(cr, normEquip) :
    details = ""
    normEquipList = ["Altar", "Amphora of Common Wine", "Amphora of Vinegar", "Andirons and Spit", "Anvil", "Armchair", "Artisan's Tools", "Backpack", "Bag of  Marbles", "Bag of  Pitons", "Bag of  Sling Bullets", 
                        "Bag of Chalk", "Bag of Chestnuts", "Bag of Common Spice", "Bag of Dried Mushrooms", "Bag of Iron Nails", "Bag of Rare Spice", "Bag of Salt", "Bag of Wheat", "Ballista", "Barrel", 
                        "Barrel of Ale", "Barrel of Oil", "Basket", "Bastard Sword", "Battleaxe", "Bed", "Bedroll", "Bench", "Bolt of Canvas", "Bolt of Linen", "Bolt of Silk", "Bookcase", "Bottle of Brandywine", 
                        "Bottle of Common Wine", "Bottle of Fine Wine", "Bottle of Good Wine", "Bottle of Honey", "Bottle of Olive Oil", "Bottle of Spiced Wine", "Bottle of Vinegar", "Bow Saw", "Box of  Arrowheads", 
                        "Box of  Candles", "Box of Charcoal", "Box of Firewood", "Breastplate", "Bucket", "Cabinet", "Canopy Bed", "Carriage", "Cart", "Cauldron", "Chain Shirt", "Chainmail", "Chair", "Chandelier", 
                        "Chariot", "Cheap Wig", "Chest", "Chisel", "Clay Pitcher", "Clay Tankard", "Club", "Cold Weather Outfit", "Common Wig", "Composite Longbow", "Composite Longbow (+ Str bonus)", 
                        "Composite Shortbow", "Composite Shortbow (+ Str bonus)", "Courtier's Outfit", "Crowbar", "Dagger", "darkwood lute", "Dart", "Desk", "Explorer's Outfit", "Fishing Net", "Flask of Oil", 
                        "Flint and Steel", "Game Board", "Glaive", "Glasscutter", "Grappling Hook", "Greataxe", "Greatsword", "Grindstone", "Halberd", "Hammer", "Handaxe", "Handsaw", "Heavy Catapult", "Heavy Crossbow", 
                        "Heavy Flail", "Heavy Mace", "Heavy Steel Shield", "Heavy Wooden Shield", "Hemp Rope", "High Boots", "Iron Bar", "Iron Pot", "Ladder", "Lamp", "Large Cage", "Large Carpet", "Large Chest", 
                        "Large Iron Box", "Large Wooden Chest", "Leather Armor", "Light Catapult", "Light Crossbow", "Light Flail", "Light Hammer", "Light Mace", "Light Wooden Shield", "Loaf of Bread", "Longbow", "Longship", 
                        "Longspear", "Longsword", "Loom", "Low Boots", "lyre", "Manacles", "Merchant's Scale", "Miner's Pick", "Morningstar", "Mortar and Pestle", "Noble's Outfit", "Padded Armor", "Pair of Dice", "Pair of Oars", 
                        "Pan Flute", "Pavilion Tent", "Pitchfork", "Piton", "Plain Tapestry", "Pole", "Portable Ram", "Pouch of Tobacco", "Quarterstaff", "Rack of Firewood", "Rake", "Rapier", "Riding Saddle", "Rope Ladder", 
                        "Rope Net", "Round Table", "Rug", "Sack", "Sack of Animal Feed", "Sack of Apples", "Sack of Wheat", "Sai", "Salted Ham", "Sap", "Sarcophagus", "Scale Mail", "Scroll Case", "Scythe", "Sedan Chair", 
                        "Sewing Needle", "Shears", "Shortbow", "Shortspear", "Shortsword", "Shrine", "Sickle", "Siege Ram", "Signet Ring", "Sled", "Sledge", "Sling", "Small Cage", "Small Carpet", "Small Cask of Ale", 
                        "Small Cask of Common Spice", "Small Cask of Dried Figs", "Small Cask of Molasses", "Small Cask of Oil", "Small Cask of Pickled Fish", "Small Cask of Sausages", "Small Cask of Tobacco", "Small Cask of Wax", 
                        "Small Glass Rod", "Small Hunting Trap", "Small Iron Box", "Small Magnet", "Small Wooden Chest", "Snowshoes", "Spade", "Spear", "Spinning Wheel", "Studded Leather Armor", "Table", "Tent", "Thieves' Tools", 
                        "Throne", "Tiny Lead Box", "Tiny Wooden Box", "Tongs", "Tower Shield", "Trebuchet", "Trident", "Vial of Exotic Ink", "Vial of Ink", "Wagon", "Wardrobe", "Warhammer", "Waterskin", "Weapon Rack", 
                        "Wedge of Cheese", "Wheel of Cheese", "Whetsone", "Whip", "Wood Axe", "Wooden Drum", "Wooden Holy Symbol", "Wool Cloak", "Workbench"]
    possibility = normEquip * random.randrange(1, 101, 1)
    normContain = []
    counter = 0
    if cr < 5 :
        counter = cr
    elif cr < 10 :
        counter = int(cr*1.5)
    elif cr < 15 :
        counter = int(cr*2)
    else :
        counter = int(cr*3)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Magic-Equipment----------------------------\n")
    return details    

def MagicEquip(cr, magicEquip) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Potions------------------------------------\n")
    return details    

def Pots(cr, pots) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Scrolls------------------------------------\n")
    return details    

def Scroll(cr, scroll) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Wand/Staff---------------------------------\n")
    return details    

def WandStaff(cr, wandStaff) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Rods---------------------------------------\n")
    return details    

def Rod(cr, rod) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Wonderous----------------------------------\n")
    return details    

def Wonderous(cr, wonderous) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Artifact-----------------------------------\n")
    return details    

def Artifact(cr, artifact) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Cursed-------------------------------------\n")
    return details    

def Cursed(cr, cursed) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    details = "%s%s" % (details, "\n-Intelligent--------------------------------\n")
    return details    

def Intelligent(cr, intelligent) :
    details = ""
    possibility = artObj * random.randrange(1, 101, 1)
    if possibility > 34 :
    return details   

def EncouterTreasure(cr, currency = 100, artObj = 100, specialMats = 100, normEquip = 100,
                     magicEquip = 100, pots = 100, scroll = 100, wandStaff = 100, rod = 100,
                     wonderous = 100, artifact = 100, cursed = 100, intelligent = 100) :
    details = ""
    detail = ""
    details = Currency(cr, currency)  
    detail = ArtObj(cr, artObj)  
    detail = SpecialMats(cr, specialMats)  
    detail = NormEquip(cr, normEquip)  
    detail = MagicEquip(cr, magicEquip)   
    detail = Pots(cr, pots)  
    detail = Scroll(cr, scroll)  
    detail = WandStaff(cr, wandStaff)   
    detail = Rod(cr, rod)  
    detail = Wonderous(cr, wonderous)   
    detail = Artifact(cr, artifact)   
    detail = Cursed(cr, cursed)   
    detail = Intelligent(cr, intelligent)

    return details

def HoardTreasure(cr, currency = 100, artObj = 100, specialMats = 100, normEquip = 100,
                  magicEquip = 100, pots = 100, scroll = 100, wandStaff = 100, rod = 100,
                  wonderous = 100, artifact = 100, cursed = 100, intelligent = 100) :
    details = ""
    details = Currency(cr, currency)  
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
typeTreasure = input().lower()
print("\ncr?\n")
cr = 0
cr = int(input())
print("\nFile name?\n")
fileName = ""
fileName = input()
fileName = "%s%s" % (fileName, ".txt")
oFile = open(fileName, "w")

if typeTreasure == "hoard" :
    artifactVal = 0
    cursedVal = 0
    intelligentVal = 0
    print("\nartifact override number?(default: 0)\n")
    artifactVal = int(input())
    print("\ncursed override number?(default: 0)\n")
    cursedVal = int(input())
    print("\nintelligent override number?(default: 0)\n")
    intelligentVal = int(input())
    details = HoardTreasure(cr, artifact = artifactVal, cursed = cursedVal, intelligent = intelligentVal)
    oFile.write(details)
    oFile.close()
else :
    artifactVal = 0
    cursedVal = 0
    intelligentVal = 0
    print("\nartifact override number?(default: 0)\n")
    artifactVal = int(input())
    print("\ncursed override number?(default: 0)\n")
    cursedVal = int(input())
    print("\nintelligent override number?(default: 0)\n")
    intelligentVal = int(input())
    details = EncouterTreasure(cr, artifact = artifactVal, cursed = cursedVal, intelligent = intelligentVal)
    oFile.write(details)
    oFile.close()
