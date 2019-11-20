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
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, artObjList.__len__(), 1))], " (", value * 10, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 8 :
            while numArtObj > 0 :
                value = random.randrange(1, 50, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, artObjList.__len__(), 1))], " (", value * 15, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 12 :
            while numArtObj > 0 :
                value = random.randrange(1, 50, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, artObjList.__len__(), 1))], " (", value * 30, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        elif cr < 16 :
            while numArtObj > 0 :
                value = random.randrange(1, 75, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, artObjList.__len__(), 1))], " (", value * 45, " gp)\n")
                numArtObj -= 1
            details = "%s%s" % (details, "\n-Special-Materials--------------------------\n")
        else :
            while numArtObj > 0 :
                value = random.randrange(1, 100, 1)
                details = "%s%s%s%s%s" % (details, artObjList[(random.randrange(0, artObjList.__len__(), 1))], " (", value * 60, " gp)\n")
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
            details = "%s%s%s%s%s" % (details, int(cr*.75), " lbs of", specialMatsList[random.randrange(0, specialMatsList.__len__(), 1)], "\n")
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
        counter = cr*2
    elif cr < 10 :
        counter = int(cr*4.5)
    elif cr < 15 :
        counter = int(cr*6.5)
    else :
        counter = int(cr*10)
    if possibility > 34 :
        while counter > 0 :
            normContain.append(random.randrange(0, normEquipList.__len__(), 1))
            counter -= 1
        for i in range(0, normEquipList.__len__()) :
            if normEquipList[i] in normContain :
                count = normContain.count(normEquipList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", normEquipList[i], "\n")
    details = "%s%s" % (details, "\n-Magic-Equipment----------------------------\n")
    return details    

def MagicEquip(cr, magicEquip) :
    details = ""
    magicEquipList = ["Adamantine Battleaxe (3010 gp)", "Adamantine Battleaxe (3010 gp) (inscription provides clue to function)", "Adamantine Battleaxe (3010 gp) (sheds light)", "Adamantine Breastplate (10200 gp)", 
                        "Adamantine Dagger (3002 gp)", "Adamantine Dagger (3002 gp) (sheds light)", "Adamantine Scale Mail (10050 gp)", "Banded Mail (+1 armor) (1400 gp)", 
                        "Banded Mail (+1 armor, Benevolent) (3400 gp)", "Banded Mail (+1 armor, Fortification (light)) (4400 gp)", "Banded Mail (+1 armor, Ghost Touch) (16400 gp)", 
                        "Banded Mail (+1 armor, Mirrored) (4400 gp)", "Banded Mail (+1 armor, Putrid) (11400 gp)", "Banded Mail (+1 armor, Shadow) (5150 gp)", "Banded Mail (+1 armor, Spell Storing) (4400 gp)", 
                        "Banded Mail (+2 armor) (4400 gp)", "Banded Mail (+2 armor, Spell Resistance (13)) (16400 gp)", "Banded Mail (+3 armor) (9400 gp)", "Banded Mail (+4 armor, Defiant) (25400 gp)", 
                        "Banded Mail (+4 armor, Poison-resistant) (18650 gp)", "Banded Mail of Luck (18900 gp)", "Bastard Sword (+1 weapon) (sheds light) (2335 gp)", "Bastard Sword (+1 weapon, Ki Focus) (8335 gp)", 
                        "Battleaxe (+1 weapon) (2310 gp)", "Battleaxe (+1 weapon) (sheds light) (2310 gp)", "Battleaxe (+2 weapon) (8310 gp)", "Battleaxe (+2 weapon) (sheds light) (8310 gp)", 
                        "Battlement Shield (16180 gp)", "Bolas (+1 weapon) (2305 gp)", "Bolas (+1 weapon) (design provides clue to function) (2305 gp)", 
                        "Bolas (+1 weapon) (inscription provides clue to function) (2305 gp)", "Bolas (+1 weapon) (sheds light) (2305 gp)", "Bolas (+1 weapon, Thundering) (8305 gp)", "Bolas (+2 weapon) (8305 gp)", 
                        "Bolas (+2 weapon) (sheds light) (8305 gp)", "Breastplate (+1 armor) (1350 gp)", "Breastplate (+1 armor, Expeditious) (5350 gp)", "Breastplate (+1 armor, Grinding) (4350 gp)", 
                        "Breastplate (+1 armor, Impervious) (4350 gp)", "Breastplate (+1 armor, Warding) (4350 gp)", "Breastplate (+2 armor) (4350 gp)", "Breastplate (+4 armor, Bolstering) (25350 gp)", 
                        "Breastplate (+4 armor, Warding) (25350 gp)", "Buccaneer's Breastplate (23850 gp)", "Buckler (+1 shield) (1155 gp)", "Buckler (+1 shield, Arrow Catching) (4155 gp)", 
                        "Buckler (+1 shield, Defiant) (4155 gp)", "Buckler (+1 shield, Grinding) (4155 gp)", "Buckler (+1 shield, Mirrored) (4155 gp)", "Buckler (+2 shield) (4155 gp)", 
                        "Buckler (+2 shield, Rallying) (9155 gp)", "Buckler (+3 shield, Bashing) (16155 gp)", "Buckler (+3 shield, Clangorous) (16155 gp)", "Buckler (+4 shield) (16155 gp)", 
                        "Burglar's Buckler (4655 gp)", "Caster's Shield (3153 gp)", "Celestial Armor (22400 gp)", "Chain Shirt (+1 armor) (1250 gp)", "Chain Shirt (+1 armor, Bitter) (4250 gp)", 
                        "Chain Shirt (+1 armor, Brawling) (4250 gp)", "Chain Shirt (+1 armor, Fortification (moderate)) (16250 gp)", "Chain Shirt (+1 armor, Ghost Touch) (16250 gp)", 
                        "Chain Shirt (+1 armor, Grinding) (4250 gp)", "Chain Shirt (+1 armor, Mirrored) (4250 gp)", "Chain Shirt (+1 armor, Radiant) (8750 gp)", "Chain Shirt (+2 armor) (4250 gp)", 
                        "Chain Shirt (+3 armor) (9250 gp)", "Chain Shirt (+3 armor, Dastard) (16250 gp)", "Chain Shirt (+4 armor) (16250 gp)", "Chainmail (+1 armor) (1300 gp)", 
                        "Chainmail (+1 armor, Bitter) (4300 gp)", "Chainmail (+1 armor, Dastard) (4300 gp)", "Chainmail (+1 armor, Deathless) (4300 gp)", "Chainmail (+1 armor, Fortification (light)) (4300 gp)", 
                        "Chainmail (+1 armor, Stanching) (4300 gp)", "Chainmail (+2 armor) (4300 gp)", "Chainmail (+2 armor, Glamered) (7000 gp)", "Chainmail (+3 armor, Mirrored) (16300 gp)", 
                        "Chainmail (+3 armor, Stanching) (16300 gp)", "Chainmail (+4 armor, Benevolent) (18300 gp)", "Club (+1 weapon) (2300 gp)", "Club (+1 weapon) (design provides clue to function) (2300 gp)", 
                        "Club (+1 weapon) (inscription provides clue to function) (2300 gp)", "Club (+1 weapon) (sheds light) (2300 gp)", "Club (+1 weapon, Corrosive) (sheds light) (8300 gp)", 
                        "Club (+1 weapon, Frost) (8300 gp)", "Club (+1 weapon, Seaborne) (8300 gp)", "Club (+1 weapon, Valiant) (inscription provides clue to function) (8300 gp)", 
                        "Club (+1 weapon, Valiant) (sheds light) (8300 gp)", "Club (+2 weapon) (8300 gp)", "Cold Iron Masterwork Longsword (330 gp)", 
                        "Cold Iron Masterwork Longsword (330 gp) (design provides clue to function)", "Cold Iron Masterwork Longsword (330 gp) (sheds light)", 
                        "Composite Longbow (+1 Str bonus) (+1 weapon) (2500 gp)", "Composite Longbow (+1 Str bonus) (+1 weapon) (inscription provides clue to function) (2500 gp)", 
                        "Composite Longbow (+1 Str bonus) (+1 weapon, Shock) (sheds light) (8500 gp)", "Composite Longbow (+1 weapon) (2400 gp)", "Composite Longbow (+2 Str bonus) (+1 weapon) (2600 gp)", 
                        "Composite Longbow (+2 Str bonus) (+2 weapon) (8600 gp)", "Composite Longbow (+2 weapon) (sheds light) (8400 gp)", "Composite Longbow (+3 Str bonus) (+2 weapon) (8700 gp)", 
                        "Composite Longbow (+4 Str bonus) (+1 weapon) (2800 gp)", "Composite Longbow (+4 Str bonus) (+1 weapon) (sheds light) (2800 gp)", "Composite Shortbow (+1 Str bonus) (+1 weapon) (2450 gp)", 
                        "Composite Shortbow (+1 Str bonus) (+1 weapon) (sheds light) (2450 gp)", "Composite Shortbow (+1 Str bonus) (+1 weapon, Thundering) (8450 gp)", 
                        "Composite Shortbow (+1 Str bonus) (+2 weapon, Bane) (design provides clue to function) (18450 gp)", "Composite Shortbow (+1 weapon) (2375 gp)", 
                        "Composite Shortbow (+1 weapon) (inscription provides clue to function) (2375 gp)", "Composite Shortbow (+1 weapon) (sheds light) (2375 gp)", 
                        "Composite Shortbow (+2 Str bonus) (+1 weapon) (2525 gp)", "Composite Shortbow (+2 Str bonus) (+1 weapon) (sheds light) (2525 gp)", 
                        "Composite Shortbow (+2 Str bonus) (+1 weapon, Seeking) (8525 gp)", "Composite Shortbow (+2 weapon) (sheds light) (8375 gp)", 
                        "Composite Shortbow (+3 weapon) (inscription provides clue to function) (18375 gp)", "Dagger (+1 weapon) (2302 gp)", "Dagger (+1 weapon) (design provides clue to function) (2302 gp)", 
                        "Dagger (+1 weapon) (sheds light) (2302 gp)", "Dagger (+1 weapon, Ominous) (8302 gp)", "Dagger (+1 weapon, Thundering) (design provides clue to function) (8302 gp)", 
                        "Dagger (+1 weapon, Vicious) (8302 gp)", "Dagger (+2 weapon, Unholy) (32302 gp)", "Dagger (+3 weapon, Frost) (32302 gp)", "Dagger (+3 weapon, Jurist) (32302 gp)", 
                        "Darkleaf Studded Leather Armor (775 gp)", "Darkwood Buckler (203 gp)", "Darkwood Shield (257 gp)", "Dart (+1 weapon) (2300 gp 5 sp)", 
                        "Dart (+1 weapon) (inscription provides clue to function) (2300 gp 5 sp)", "Dart (+1 weapon) (sheds light) (2300 gp 5 sp)", "Dart (+2 weapon) (8300 gp 5 sp)", 
                        "Dart (+2 weapon) (sheds light) (8300 gp 5 sp)", "Disarming Blade (17820 gp)", "Disarming Blade (17820 gp) (sheds light)", "Dragonhide Half-plate (silver dragon) (1500 gp)", 
                        "Dragonhide Plate (3300 gp)", "Dust Bolt (1730 gp)", "Dust Bolt (1730 gp) (design provides clue to function)", "Dust Bolt (1730 gp) (sheds light)", "Dustburst Bullet (196 gp)", 
                        "Dwarven Plate (16500 gp)", "Dwarven Waraxe (+1 weapon) (2330 gp)", "Dwarven Waraxe (+1 weapon) (sheds light) (2330 gp)", "Dwarven Waraxe (+1 weapon, Defending) (8330 gp)", 
                        "Dwarven Waraxe (+2 weapon) (8330 gp)", "Dwarven Waraxe (+2 weapon, Flaming Burst) (32330 gp)", "Dwarven Waraxe (+3 weapon) (18330 gp)", "Eel Hide Leather Armor (1210 gp)", 
                        "Elysian Bronze Full Plate (4500 gp)", "Elysian Bronze Splint Mail (3200 gp)", "Falchion (+1 weapon) (2375 gp)", "Falchion (+1 weapon, Keen) (8375 gp)", "Falchion (+2 weapon) (8375 gp)", 
                        "Falchion (+2 weapon) (sheds light) (8375 gp)", "Fire-forged Steel Half-plate (3600 gp)", "Fortress Shield (19180 gp)", "Frost-forged Steel Full Plate (4500 gp)", 
                        "Frost-forged Steel Scale Mail (2550 gp)", "Full Plate (+1 armor) (2650 gp)", "Full Plate (+1 armor, Bitter) (5650 gp)", "Full Plate (+1 armor, Brawling) (5650 gp)", 
                        "Full Plate (+1 armor, Fortification (moderate)) (17650 gp)", "Full Plate (+1 armor, Mirrored) (5650 gp)", "Full Plate (+1 armor, Poison-resistant) (4900 gp)", 
                        "Full Plate (+2 armor) (5650 gp)", "Full Plate (+3 armor) (10650 gp)", "Full Plate (+3 armor, Poison-resistant) (12900 gp)", "Full Plate (+4 armor) (17650 gp)", 
                        "Full Plate (+4 armor, Champion) (26650 gp)", "Gauntlet (+1 weapon) (2302 gp)", "Gauntlet (+1 weapon) (design provides clue to function) (2302 gp)", 
                        "Gauntlet (+1 weapon) (sheds light) (2302 gp)", "Gauntlet (+1 weapon, Bane (humanoids, human)) (sheds light) (8302 gp)", "Gauntlet (+2 weapon) (sheds light) (8302 gp)", 
                        "Gauntlet (+2 weapon, Shock) (18302 gp)", "Glaive (+1 weapon) (2308 gp)", "Glaive (+2 weapon) (8308 gp)", "Glaive (+2 weapon, Icy Burst) (32308 gp)", "Greataxe (+1 weapon) (2320 gp)", 
                        "Greataxe (+1 weapon) (inscription provides clue to function) (2320 gp)", "Greataxe (+1 weapon) (sheds light) (2320 gp)", "Greataxe (+1 weapon, Bane (animals)) (8320 gp)", 
                        "Greataxe (+1 weapon, Cunning) (sheds light) (8320 gp)", "Greataxe (+1 weapon, Glamered) (6320 gp)", "Greataxe (+1 weapon, Spell Storing) (design provides clue to function) (8320 gp)", 
                        "Greataxe (+2 weapon) (8320 gp)", "Greataxe (+2 weapon) (sheds light) (8320 gp)", "Greataxe (+2 weapon, Ki Focus) (18320 gp)", "Greatclub (+1 weapon) (2305 gp)", 
                        "Greatclub (+1 weapon) (design provides clue to function) (2305 gp)", "Greatclub (+1 weapon) (sheds light) (2305 gp)", "Greatclub (+1 weapon, Bane (undead)) (8305 gp)", 
                        "Greatclub (+1 weapon, Flaming) (8305 gp)", "Greatclub (+2 weapon) (8305 gp)", "Greatclub (+3 weapon, Frost) (32305 gp)", "Greater Burrowing Bullet (3447 gp)", 
                        "Greater Burrowing Bullet (3447 gp) (design provides clue to function)", "Greater Burrowing Bullet (3447 gp) (inscription provides clue to function)", 
                        "Greater Burrowing Bullet (3447 gp) (sheds light)", "Greater Hushing Arrow (1047 gp)", "Greater Hushing Arrow (1047 gp) (inscription provides clue to function)", 
                        "Greater Hushing Arrow (1047 gp) (sheds light)", "Greater Slaying Arrow (aberrations) (4057 gp)", "Greater Slaying Arrow (constructs) (4057 gp) (inscription provides clue to function)", 
                        "Greater Slaying Arrow (fey) (4057 gp)", "Greater Slaying Arrow (humanoids, giants) (4057 gp)", "Greater Slaying Arrow (humanoids, giants) (4057 gp) (inscription provides clue to function)", 
                        "Greater Slaying Arrow (humanoids, human) (4057 gp) (sheds light)", "Greater Slaying Arrow (humanoids, orc) (4057 gp)", "Greater Slaying Arrow (humanoids, reptilian) (4057 gp)", 
                        "Greater Slaying Arrow (magical beasts) (4057 gp) (inscription provides clue to function)", "Greater Slaying Arrow (monstrous humanoids) (4057 gp)", 
                        "Greater Slaying Arrow (outsiders, earth) (4057 gp) (inscription provides clue to function)", "Greater Slaying Arrow (outsiders, lawful) (4057 gp)", "Greatsword (+1 weapon) (2350 gp)", 
                        "Greatsword (+1 weapon) (design provides clue to function) (2350 gp)", "Greatsword (+1 weapon) (inscription provides clue to function) (2350 gp)", 
                        "Greatsword (+1 weapon) (sheds light) (2350 gp)", "Greatsword (+1 weapon, Furious) (8350 gp)", "Greatsword (+1 weapon, Glamered) (6350 gp)", 
                        "Greatsword (+1 weapon, Mighty Cleaving) (8350 gp)", "Greatsword (+1 weapon, Shock) (8350 gp)", "Greatsword (+2 weapon) (8350 gp)", 
                        "Greatsword (+2 weapon) (design provides clue to function) (8350 gp)", "Halberd (+1 weapon) (2310 gp)", "Halberd (+1 weapon) (sheds light) (2310 gp)", "Half-plate (+1 armor) (1750 gp)", 
                        "Half-plate (+1 armor, Balanced) (4750 gp)", "Half-plate (+1 armor, Brawling) (4750 gp)", "Half-plate (+1 armor, Defiant) (4750 gp)", "Half-plate (+1 armor, Glamered) (4450 gp)", 
                        "Half-plate (+1 armor, Titanic) (16750 gp)", "Half-plate (+2 armor) (4750 gp)", "Half-plate (+4 armor, Benevolent) (18750 gp)", "Handaxe (+1 weapon) (2306 gp)", 
                        "Handaxe (+1 weapon) (sheds light) (2306 gp)", "Handaxe (+2 weapon) (8306 gp)", "Heavy Crossbow (+1 weapon) (2350 gp)", "Heavy Crossbow (+1 weapon) (sheds light) (2350 gp)", 
                        "Heavy Crossbow (+1 weapon, Holy) (sheds light) (18350 gp)", "Heavy Crossbow (+2 weapon) (sheds light) (8350 gp)", "Heavy Flail (+1 weapon) (sheds light) (2315 gp)", 
                        "Heavy Mace (+1 weapon) (2312 gp)", "Heavy Mace (+1 weapon) (design provides clue to function) (2312 gp)", "Heavy Mace (+1 weapon) (inscription provides clue to function) (2312 gp)", 
                        "Heavy Mace (+1 weapon) (sheds light) (2312 gp)", "Heavy Mace (+2 weapon) (sheds light) (8312 gp)", "Heavy Steel Shield (+1 shield) (1170 gp)", 
                        "Heavy Steel Shield (+1 shield, Animated) (9170 gp)", "Heavy Steel Shield (+1 shield, Bashing) (4170 gp)", "Heavy Steel Shield (+1 shield, Blinding) (4170 gp)", 
                        "Heavy Steel Shield (+1 shield, Clangorous) (4170 gp)", "Heavy Steel Shield (+1 shield, Grinding) (4170 gp)", "Heavy Steel Shield (+1 shield, Impervious) (4170 gp)", 
                        "Heavy Steel Shield (+1 shield, Radiant) (8670 gp)", "Heavy Steel Shield (+1 shield, Ramming) (4170 gp)", "Heavy Steel Shield (+1 shield, Wild) (16170 gp)", 
                        "Heavy Steel Shield (+2 shield) (4170 gp)", "Heavy Steel Shield (+2 shield, Spell Resistance (13)) (16170 gp)", "Heavy Steel Shield (+3 shield) (9170 gp)", 
                        "Heavy Steel Shield (+4 shield, Poison-resistant) (18420 gp)", "Heavy Wooden Shield (+1 shield) (1157 gp)", "Heavy Wooden Shield (+1 shield, Arrow Catching) (4157 gp)", 
                        "Heavy Wooden Shield (+1 shield, Defiant) (4157 gp)", "Heavy Wooden Shield (+1 shield, Fortification (light)) (4157 gp)", "Heavy Wooden Shield (+1 shield, Merging) (9157 gp)", 
                        "Heavy Wooden Shield (+1 shield, Ramming) (4157 gp)", "Heavy Wooden Shield (+1 shield, Spell Resistance (15)) (16157 gp)", "Heavy Wooden Shield (+2 shield) (4157 gp)", 
                        "Heavy Wooden Shield (+4 shield, Impervious) (25157 gp)", "Hide (+1 armor) (1165 gp)", "Hide (+1 armor, Bitter) (4165 gp)", "Hide (+1 armor, Dastard) (4165 gp)", 
                        "Hide (+1 armor, Grinding) (4165 gp)", "Hide (+1 armor, Rallying) (6165 gp)", "Hide (+2 armor) (4165 gp)", "Hide (+2 armor, Creeping) (9165 gp)", "Hide (+3 armor) (9165 gp)", 
                        "Hushing Arrow (547 gp)", "Hushing Arrow (547 gp) (sheds light)", "Javelin of Lightning (1500 gp)", "Javelin of Lightning (1500 gp) (inscription provides clue to function)", 
                        "Lance (+1 weapon) (2310 gp)", "Lance (+1 weapon) (design provides clue to function) (2310 gp)", "Lance (+1 weapon) (inscription provides clue to function) (2310 gp)", 
                        "Lance (+1 weapon) (sheds light) (2310 gp)", "Lance (+1 weapon, Ki Focus) (inscription provides clue to function) (8310 gp)", "Lance (+1 weapon, Throwing) (8310 gp)", 
                        "Lance (+2 weapon) (inscription provides clue to function) (8310 gp)", "Lance of Jousting (4310 gp)", "Lance of Jousting (4310 gp) (design provides clue to function)", 
                        "Lance of Jousting (4310 gp) (sheds light)", "Lash of the Howler (18305 gp)", "Leather Armor (+1 armor) (1160 gp)", "Leather Armor (+1 armor, Bolstering) (4160 gp)", 
                        "Leather Armor (+1 armor, Brawling) (4160 gp)", "Leather Armor (+1 armor, Dastard) (4160 gp)", "Leather Armor (+1 armor, Poison-resistant) (3410 gp)", 
                        "Leather Armor (+1 armor, Spell Resistance (15)) (16160 gp)", "Leather Armor (+1 armor, Warding) (4160 gp)", "Leather Armor (+2 armor) (4160 gp)", 
                        "Leather Armor (+2 armor, Slick) (7910 gp)", "Leather Armor (+3 armor) (9160 gp)", "Leather Armor (+3 armor, Balanced) (16160 gp)", "Leather Armor (+4 armor) (16160 gp)", 
                        "Leather Armor (+4 armor, Bolstering) (25160 gp)", "Leather Armor (+4 armor, Defiant) (25160 gp)", "Light Crossbow (+1 weapon) (2335 gp)", 
                        "Light Crossbow (+1 weapon) (inscription provides clue to function) (2335 gp)", "Light Crossbow (+1 weapon) (sheds light) (2335 gp)", "Light Crossbow (+1 weapon, Distance) (8335 gp)", 
                        "Light Crossbow (+2 weapon, Distance) (sheds light) (18335 gp)", "Light Flail (+1 weapon) (design provides clue to function) (2308 gp)", 
                        "Light Flail (+1 weapon) (inscription provides clue to function) (2308 gp)", "Light Flail (+1 weapon) (sheds light) (2308 gp)", "Light Flail (+2 weapon) (8308 gp)", 
                        "Light Flail (+2 weapon) (inscription provides clue to function) (8308 gp)", "Light Hammer (+1 weapon) (2301 gp)", "Light Hammer (+1 weapon) (sheds light) (2301 gp)", 
                        "Light Mace (+1 weapon) (2305 gp)", "Light Mace (+1 weapon) (design provides clue to function) (2305 gp)", "Light Mace (+1 weapon) (inscription provides clue to function) (2305 gp)", 
                        "Light Mace (+1 weapon) (sheds light) (2305 gp)", "Light Mace (+1 weapon, Ominous) (8305 gp)", "Light Mace (+1 weapon, Valiant) (sheds light) (8305 gp)", 
                        "Light Mace (+1 weapon, Wounding) (18305 gp)", "Light Mace (+2 weapon) (design provides clue to function) (8305 gp)", "Light Pick (+1 weapon) (2304 gp)", 
                        "Light Pick (+1 weapon) (inscription provides clue to function) (2304 gp)", "Light Pick (+1 weapon) (sheds light) (2304 gp)", "Light Steel Shield (+1 shield) (1159 gp)", 
                        "Light Steel Shield (+1 shield, Animated) (9159 gp)", "Light Steel Shield (+1 shield, Arrow Catching) (4159 gp)", "Light Steel Shield (+1 shield, Fortification (light)) (4159 gp)", 
                        "Light Steel Shield (+1 shield, Poison-resistant) (3409 gp)", "Light Steel Shield (+1 shield, Ramming) (4159 gp)", "Light Steel Shield (+2 shield) (4159 gp)", 
                        "Light Steel Shield (+2 shield, Merging) (16159 gp)", "Light Steel Shield (+2 shield, Rallying) (9159 gp)", "Light Steel Shield (+2 shield, Spell Resistance (13)) (16159 gp)", 
                        "Light Steel Shield (+3 shield) (9159 gp)", "Light Steel Shield (+3 shield, Defiant) (16159 gp)", "Light Steel Shield (+3 shield, Impervious) (16159 gp)", 
                        "Light Steel Shield (+4 shield) (16159 gp)", "Light Steel Shield (+4 shield, Arrow Catching) (25159 gp)", "Light Steel Shield (+4 shield, Ramming) (25159 gp)", 
                        "Light Wooden Shield (+1 shield) (1153 gp)", "Light Wooden Shield (+1 shield, Animated) (9153 gp)", "Light Wooden Shield (+1 shield, Fortification (moderate)) (16153 gp)", 
                        "Light Wooden Shield (+1 shield, Impervious) (4153 gp)", "Light Wooden Shield (+1 shield, Spell Resistance (13)) (9153 gp)", "Light Wooden Shield (+2 shield) (4153 gp)", 
                        "Light Wooden Shield (+2 shield, Spell Resistance (13)) (16153 gp)", "Light Wooden Shield (+3 shield) (9153 gp)", "Light Wooden Shield (+3 shield, Grinding) (16153 gp)", 
                        "Light Wooden Shield (+3 shield, Mirrored) (16153 gp)", "Light Wooden Shield (+4 shield) (16153 gp)", "Living Steel Banded Mail (1750 gp)", "Living Steel Breastplate (1200 gp)", 
                        "Living Steel Heavy Shield (120 gp)", "Longbow (+1 weapon) (2375 gp)", "Longbow (+1 weapon) (design provides clue to function) (2375 gp)", "Longbow (+1 weapon) (sheds light) (2375 gp)", 
                        "Longbow (+1 weapon, Bane) (sheds light) (8375 gp)", "Longbow (+1 weapon, Corrosive) (8375 gp)", "Longbow (+2 weapon) (8375 gp)", 
                        "Longbow (+2 weapon) (design provides clue to function) (8375 gp)", "Longbow (+2 weapon) (inscription provides clue to function) (8375 gp)", "Longbow (+2 weapon) (sheds light) (8375 gp)", 
                        "Longbow (+3 weapon) (18375 gp)", "Longbow (+3 weapon, Jurist) (sheds light) (32375 gp)", "Longspear (+1 weapon) (2305 gp)", 
                        "Longspear (+1 weapon) (design provides clue to function) (2305 gp)", "Longspear (+1 weapon) (inscription provides clue to function) (2305 gp)", 
                        "Longspear (+1 weapon) (sheds light) (2305 gp)", "Longspear (+1 weapon, Conductive) (sheds light) (8305 gp)", "Longspear (+1 weapon, Flaming) (8305 gp)", 
                        "Longspear (+1 weapon, Mighty Cleaving) (8305 gp)", "Longspear (+1 weapon, Neutralizing) (8305 gp)", "Longspear (+2 weapon, Quenching) (sheds light) (18305 gp)", 
                        "Longsword (+1 weapon) (2315 gp)", "Longsword (+1 weapon) (design provides clue to function) (2315 gp)", "Longsword (+1 weapon) (inscription provides clue to function) (2315 gp)", 
                        "Longsword (+1 weapon) (sheds light) (2315 gp)", "Longsword (+1 weapon, Courageous) (sheds light) (8315 gp)", "Longsword (+1 weapon, Defending) (8315 gp)", 
                        "Longsword (+1 weapon, Frost) (8315 gp)", "Longsword (+1 weapon, Shock) (8315 gp)", "Longsword (+1 weapon, Spell Storing) (8315 gp)", "Longsword (+2 weapon) (8315 gp)", 
                        "Longsword (+2 weapon) (inscription provides clue to function) (8315 gp)", "Mistmail (2250 gp)", "Mithral Heavy Shield (1020 gp)", "Mithral Shirt (1100 gp)", "Mithral Splint Mail (9200 gp)", 
                        "Morningstar (+1 weapon) (2308 gp)", "Morningstar (+1 weapon) (design provides clue to function) (2308 gp)", "Morningstar (+1 weapon) (sheds light) (2308 gp)", 
                        "Morningstar (+1 weapon, Throwing) (8308 gp)", "Morningstar (+2 weapon) (8308 gp)", "Morningstar (+2 weapon, Anarchic) (inscription provides clue to function) (32308 gp)", 
                        "Nunchaku (+1 weapon) (2302 gp)", "Nunchaku (+1 weapon) (design provides clue to function) (2302 gp)", "Nunchaku (+1 weapon, Conductive) (sheds light) (8302 gp)", 
                        "Nunchaku (+1 weapon, Merciful) (sheds light) (8302 gp)", "Padded Armor (+1 armor) (1155 gp)", "Padded Armor (+1 armor, Bitter) (4155 gp)", "Padded Armor (+1 armor, Dastard) (4155 gp)", 
                        "Padded Armor (+1 armor, Delving) (11155 gp)", "Padded Armor (+1 armor, Mirrored) (4155 gp)", "Padded Armor (+2 armor) (4155 gp)", "Padded Armor (+3 armor) (9155 gp)", 
                        "Padded Armor (+4 armor, Mirrored) (25155 gp)", "Quarterstaff (+1 weapon) (2600 gp)", "Quarterstaff (+1 weapon) (design provides clue to function) (2600 gp)", 
                        "Quarterstaff (+1 weapon) (inscription provides clue to function) (2600 gp)", "Quarterstaff (+1 weapon) (sheds light) (2600 gp)", 
                        "Quarterstaff (+1 weapon, Thundering) (sheds light) (8600 gp)", "Quarterstaff (+1 weapon, Vicious) (sheds light) (8600 gp)", "Quarterstaff (+2 weapon) (sheds light) (8600 gp)", 
                        "Rapier (+1 weapon) (2320 gp)", "Rapier (+1 weapon) (inscription provides clue to function) (2320 gp)", "Rapier (+1 weapon) (sheds light) (2320 gp)", "Rapier (+1 weapon, Flaming) (8320 gp)", 
                        "Rapier (+1 weapon, Limning) (8320 gp)", "Rapier (+2 weapon) (8320 gp)", "Rapier (+2 weapon) (sheds light) (8320 gp)", "Rapier (+3 weapon, Bane (dragons)) (sheds light) (32320 gp)", 
                        "Rapier (+3 weapon, Quenching) (sheds light) (32320 gp)", "Sai (+1 weapon) (2301 gp)", "Sai (+1 weapon) (inscription provides clue to function) (2301 gp)", 
                        "Sai (+1 weapon) (sheds light) (2301 gp)", "Sai (+1 weapon, Corrosive) (8301 gp)", "Sai (+1 weapon, Throwing) (8301 gp)", "Sai (+2 weapon) (inscription provides clue to function) (8301 gp)", 
                        "Sap (+1 weapon) (2301 gp)", "Sap (+1 weapon) (sheds light) (2301 gp)", "Sap (+2 weapon, Holy) (32301 gp)", "Scale Mail (+1 armor) (1200 gp)", "Scale Mail (+1 armor, Defiant) (4200 gp)", 
                        "Scale Mail (+1 armor, Jousting) (4950 gp)", "Scale Mail (+1 armor, Mirrored) (4200 gp)", "Scale Mail (+1 armor, Poison-resistant) (3450 gp)", "Scale Mail (+1 armor, Rallying) (6200 gp)", 
                        "Scale Mail (+1 armor, Stanching) (4200 gp)", "Scale Mail (+2 armor) (4200 gp)", "Scale Mail (+3 armor, Dastard) (16200 gp)", "Scale Mail (+3 armor, Defiant) (16200 gp)",
                        "Scale Mail (+3 armor, Spell Storing) (16200 gp)", "Scale Mail (+4 armor) (16200 gp)", "Screaming Bolt (267 gp)", "Screaming Bolt (267 gp) (inscription provides clue to function)", 
                        "Scythe (+1 weapon) (2318 gp)", "Scythe (+1 weapon) (inscription provides clue to function) (2318 gp)", "Scythe (+1 weapon) (sheds light) (2318 gp)", "Scythe (+1 weapon, Ki Focus) (8318 gp)", 
                        "Scythe (+2 weapon) (8318 gp)", "Scythe (+2 weapon) (design provides clue to function) (8318 gp)", "Scythe (+2 weapon) (sheds light) (8318 gp)", "Scythe (+2 weapon, Corrosive) (18318 gp)", 
                        "Scythe (+3 weapon) (design provides clue to function) (18318 gp)", "Searing Arrow (1516 gp)", "Searing Arrow (1516 gp) (sheds light)", "Shieldsplitter Lance (18310 gp) (sheds light)", 
                        "Shortbow (+1 weapon) (2330 gp)", "Shortbow (+1 weapon) (design provides clue to function) (2330 gp)", "Shortbow (+1 weapon) (inscription provides clue to function) (2330 gp)", 
                        "Shortbow (+1 weapon) (sheds light) (2330 gp)", "Shortbow (+1 weapon, Bane) (8330 gp)", "Shortbow (+1 weapon, Frost) (8330 gp)", "Shortbow (+1 weapon, Shock) (8330 gp)", 
                        "Shortbow (+1 weapon, Thundering) (8330 gp)", "Shortbow (+2 weapon) (inscription provides clue to function) (8330 gp)", "Shortbow (+3 weapon, Cunning) (sheds light) (32330 gp)", 
                        "Shortspear (+1 weapon) (2301 gp)", "Shortspear (+1 weapon) (sheds light) (2301 gp)", "Shortspear (+1 weapon, Jurist) (8301 gp)", "Shortspear (+1 weapon, Limning) (sheds light) (8301 gp)", 
                        "Shortspear (+2 weapon) (8301 gp)", "Shortspear (+2 weapon) (sheds light) (8301 gp)", "Shortspear (+2 weapon, Glorious) (design provides clue to function) (32301 gp)", 
                        "Shortsword (+1 weapon) (2310 gp)", "Shortsword (+1 weapon) (inscription provides clue to function) (2310 gp)", "Shortsword (+1 weapon) (sheds light) (2310 gp)", 
                        "Shortsword (+1 weapon, Bane (aberrations)) (8310 gp)", "Shortsword (+1 weapon, Flaming) (8310 gp)", "Shortsword (+1 weapon, Grayflame) (8310 gp)", 
                        "Shortsword (+1 weapon, Limning) (sheds light) (8310 gp)", "Shortsword (+1 weapon, Mighty Cleaving) (sheds light) (8310 gp)", "Shortsword (+2 weapon) (8310 gp)", 
                        "Shortsword (+2 weapon) (sheds light) (8310 gp)", "Sickle (+1 weapon) (2306 gp)", "Sickle (+1 weapon) (sheds light) (2306 gp)", "Sickle (+2 weapon) (8306 gp)", 
                        "Sickle (+3 weapon, Thundering) (32306 gp)", "Sizzling Arrow (1516 gp)", "Sizzling Arrow (1516 gp) (sheds light)", "Slaying Arrow (humanoids, elf) (2282 gp) (sheds light)", 
                        "Slaying Arrow (humanoids, orc) (2282 gp)", "Slaying Arrow (humanoids, reptilian) (2282 gp)", "Slaying Arrow (magical beasts) (2282 gp)", "Slaying Arrow (monstrous humanoids) (2282 gp)", 
                        "Slaying Arrow (outsiders, lawful) (2282 gp)", "Slaying Arrow (undead) (2282 gp)", "Sleep Arrow (132 gp)", "Sleep Arrow (132 gp) (design provides clue to function)", 
                        "Sleep Arrow (132 gp) (sheds light)", "Sling (+1 weapon) (2300 gp)", "Sling (+1 weapon) (design provides clue to function) (2300 gp)", "Sling (+1 weapon) (sheds light) (2300 gp)", 
                        "Sling (+1 weapon, Frost) (8300 gp)", "Sling (+2 weapon) (inscription provides clue to function) (8300 gp)", "Sling (+2 weapon, Igniting) (32300 gp)", "Spear (+1 weapon) (2302 gp)", 
                        "Spear (+1 weapon) (design provides clue to function) (2302 gp)", "Spear (+1 weapon) (sheds light) (2302 gp)", "Spear (+1 weapon, Bane (outsiders, lawful)) (sheds light) (8302 gp)", 
                        "Spear (+1 weapon, Corrosive) (8302 gp)", "Spear (+1 weapon, Cunning) (8302 gp)", "Spear (+1 weapon, Frost) (sheds light) (8302 gp)", "Spear (+1 weapon, Ominous) (8302 gp)", 
                        "Spear (+2 weapon) (8302 gp)", "Spear (+2 weapon) (inscription provides clue to function) (8302 gp)", "Splint Mail (+1 armor) (1350 gp)", "Splint Mail (+1 armor, Defiant) (4350 gp)", 
                        "Splint Mail (+1 armor, Expeditious) (5350 gp)", "Splint Mail (+1 armor, Invulnerability) (16350 gp)", "Splint Mail (+2 armor) (4350 gp)", "Splint Mail (+2 armor, Shadow) (8100 gp)", 
                        "Splint Mail (+3 armor, Deathless) (16350 gp)", "Studded Leather Armor (+1 armor) (1175 gp)", "Studded Leather Armor (+1 armor, Bolstering) (4175 gp)", 
                        "Studded Leather Armor (+1 armor, Dastard) (4175 gp)", "Studded Leather Armor (+1 armor, Fortification (light)) (4175 gp)", "Studded Leather Armor (+1 armor, Slick) (4925 gp)", 
                        "Studded Leather Armor (+1 armor, Spell Storing) (4175 gp)", "Studded Leather Armor (+2 armor) (4175 gp)", "Studded Leather Armor (+2 armor, Glamered) (6875 gp)", "Tangle Bolt (226 gp)", 
                        "Tangle Bolt (226 gp) (inscription provides clue to function)", "Tangle Bolt (226 gp) (sheds light)", "Tower Shield (+1 shield) (1180 gp)", "Tower Shield (+1 shield, Bashing) (4180 gp)", 
                        "Tower Shield (+1 shield, Impervious) (4180 gp)", "Tower Shield (+2 shield) (4180 gp)", "Tower Shield (+3 shield) (9180 gp)", "Tower Shield (+4 shield, Ramming) (25180 gp)", 
                        "Tracer Bullet (100 gp)", "Tracer Bullet (100 gp) (sheds light)", "Trident (+1 weapon) (2315 gp)", "Trident (+1 weapon) (design provides clue to function) (2315 gp)", 
                        "Trident (+1 weapon) (inscription provides clue to function) (2315 gp)", "Trident (+1 weapon, Ghost Touch) (8315 gp)", "Trident (+3 weapon) (sheds light) (18315 gp)", 
                        "Warhammer (+1 weapon) (2312 gp)", "Warhammer (+1 weapon) (design provides clue to function) (2312 gp)", "Warhammer (+1 weapon) (inscription provides clue to function) (2312 gp)", 
                        "Warhammer (+1 weapon) (sheds light) (2312 gp)", "Warhammer (+1 weapon, Frost) (sheds light) (8312 gp)", "Warhammer (+2 weapon) (8312 gp)", "Warhammer (+2 weapon) (sheds light) (8312 gp)", 
                        "Whip (+1 weapon) (2301 gp)", "Whip (+1 weapon) (inscription provides clue to function) (2301 gp)", "Whip (+1 weapon) (sheds light) (2301 gp)", "Whip (+2 weapon) (sheds light) (8301 gp)", 
                        "Winged Shield (17257 gp)", "Zombie Skin Shield (2159 gp)"]
    possibility = magicEquip * random.randrange(1, 101, 1)
    magicContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*.333)
        elif cr < 10 :
            counter = int(cr*.666)
        elif cr < 15 :
            counter = int(cr*1)
        else :
            counter = int(cr*1.333)
        while counter > 0 :
            magicContain.append(random.randrange(0, magicEquipList.__len__(), 1))
            counter -= 1
        for i in range(0, magicEquipList.__len__()) :
            if magicEquipList[i] in magicContain :
                count = magicContain.count(magicEquipList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", magicEquipList[i], "\n")
    details = "%s%s" % (details, "\n-Potions------------------------------------\n")
    return details    

def Pots(cr, pots) :
    details = ""
    potionList = ["Oil of Ablative Barrier (uc, 300 gp)", "Oil of Align Weapon (cr, 300 gp)", "Oil of Animate Rope (cr, 50 gp)", "Oil of Arcane Lock (cr, 300 gp)", "Oil of Arcane Mark (cr, 25 gp)", 
                    "Oil of Bless Weapon (cr, 50 gp)", "Oil of Continual Flame (cr, 300 gp)", "Oil of Daylight (cr, 750 gp)", "Oil of Dispel Magic (cr, 750 gp)", "Oil of Erase (cr, 50 gp)", 
                    "Oil of Fire Trap (cr, 775 gp)", "Oil of Flame Arrow (cr, 750 gp)", "Oil of Gentle Repose (cr, 300 gp)", "Oil of Grease (cr, 50 gp)", "Oil of Hold Portal (cr, 50 gp)", 
                    "Oil of Keen Edge (cr, 750 gp)", "Oil of Light (cr, 25 gp)", "Oil of Light (cr, 25 gp)", "Oil of Mage Armor (cr, 50 gp)", "Oil of Magic Stone (cr, 50 gp)", "Oil of Magic Vestment (cr, 750 gp)", 
                    "Oil of Magic Weapon (cr, 50 gp)", "Oil of Make Whole (cr, 300 gp)", "Oil of Obscure Object (cr, 300 gp)", "Oil of Purify Food and Drink (cr, 25 gp)", "Oil of Remove Curse (cr, 750 gp)", 
                    "Oil of Remove Paralysis (cr, 300 gp)", "Oil of Rope Trick (cr, 300 gp)", "Oil of Sanctify Corpse (um, 50 gp)", "Oil of Shillelagh (cr, 50 gp)", "Oil of Shrink Item (cr, 750 gp)", 
                    "Oil of Slipstream (apg, 300 gp)", "Oil of Stone Shape (cr, 750 gp)", "Oil of Warp Wood (cr, 300 gp)", "Oil of Wood Shape (cr, 300 gp)", "Potion of Acute Senses (um, 300 gp)", 
                    "Potion of Aid (cr, 300 gp)", "Potion of Ant Haul (apg, 50 gp)", "Potion of Barkskin (cr, 300 gp)", "Potion of Bear's Endurance (cr, 300 gp)", "Potion of Blur (cr, 300 gp)", 
                    "Potion of Bullet Shield (uc, 300 gp)", "Potion of Bull's Strength (cr, 300 gp)", "Potion of Burrow (um, 750 gp)", "Potion of Cat's Grace (cr, 300 gp)", "Potion of Certain Grip (uc, 300 gp)", 
                    "Potion of Cloak of Shade (apg, 50 gp)", "Potion of Corruption Resistance (apg, 300 gp)", "Potion of Countless Eyes (um, 750 gp)", "Potion of Cure Light Wounds (cr, 50 gp)", 
                    "Potion of Cure Light Wounds (cr, 50 gp)", "Potion of Cure Moderate Wounds (cr, 300 gp)", "Potion of Cure Serious Wounds (cr, 750 gp)", "Potion of Darkvision (cr, 300 gp)", 
                    "Potion of Delay Poison (cr, 300 gp)", "Potion of Disguise Other (um, 300 gp)", "Potion of Displacement (cr, 750 gp)", "Potion of Draconic Reservoir (apg, 750 gp)", 
                    "Potion of Eagle's Splendor (cr, 300 gp)", "Potion of Endure Elements (cr, 50 gp)", "Potion of Enlarge Person (cr, 50 gp)", "Potion of Feather Step (apg, 50 gp)", "Potion of Fly (cr, 750 gp)", 
                    "Potion of Fox's Cunning (cr, 300 gp)", "Potion of Gaseous Form (cr, 750 gp)", "Potion of Good Hope (cr, 750 gp)", "Potion of Goodberry (cr, 50 gp)", "Potion of Greater Magic Fang (cr, 750 gp)", 
                    "Potion of Guidance (cr, 25 gp)", "Potion of Haste (cr, 750 gp)", "Potion of Heroism (cr, 750 gp)", "Potion of Hide from Animals (cr, 50 gp)", "Potion of Hide from Undead (cr, 50 gp)", 
                    "Potion of Invigorate (apg, 50 gp)", "Potion of Invisibility (cr, 300 gp)", "Potion of Jump (cr, 50 gp)", "Potion of Keen Senses (apg, 50 gp)", "Potion of Levitate (cr, 300 gp)", 
                    "Potion of Magic Fang (cr, 50 gp)", "Potion of Neutralize Poison (cr, 750 gp)", "Potion of Nondetection (cr, 800 gp)", "Potion of Owl's Wisdom (cr, 300 gp)", "Potion of Pass without Trace (cr, 50 gp)", 
                    "Potion of Protection from Acid (5th) (cr, 750 gp)", "Potion of Protection from Arrows (cr, 300 gp)", "Potion of Protection from Chaos (cr, 50 gp)", "Potion of Protection from Cold (5th) (cr, 750 gp)", 
                    "Potion of Protection from Electricity (5th) (cr, 750 gp)", "Potion of Protection from Evil (cr, 50 gp)", "Potion of Protection from Fire (5th) (cr, 750 gp)", "Potion of Protection from Good (cr, 50 gp)", 
                    "Potion of Protection from Law (cr, 50 gp)", "Potion of Protection from Sonic (5th) (cr, 750 gp)", "Potion of Rage (cr, 750 gp)", "Potion of Reduce Animal (cr, 300 gp)", "Potion of Reduce Person (cr, 50 gp)", 
                    "Potion of Remove Blindness/Deafness (cr, 750 gp)", "Potion of Remove Disease (cr, 750 gp)", "Potion of Remove Fear (cr, 50 gp)", "Potion of Remove Sickness (um, 50 gp)", "Potion of Resist Acid (3rd) (cr, 300 gp)", 
                    "Potion of Resist Cold (3rd) (cr, 300 gp)", "Potion of Resist Electricity (3rd) (cr, 300 gp)", "Potion of Resist Fire (3rd) (cr, 300 gp)", "Potion of Resist Sonic (3rd) (cr, 300 gp)", 
                    "Potion of Resistance (cr, 25 gp)", "Potion of Sanctuary (cr, 50 gp)", "Potion of Shield of Faith (cr, 50 gp)", "Potion of Spider Climb (cr, 300 gp)", "Potion of Stabilize (cr, 25 gp)", 
                    "Potion of Status (cr, 300 gp)", "Potion of Tongues (cr, 750 gp)", "Potion of Touch of the Sea (apg, 50 gp)", "Potion of Undetectable Alignment (cr, 300 gp)", "Potion of Vanish (apg, 50 gp)", 
                    "Potion of Virtue (cr, 25 gp)", "Potion of Water Breathing (cr, 750 gp)", "Potion of Water Walk (cr, 750 gp)"]
    possibility = pots * random.randrange(1, 101, 1)
    potionContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*.5)
        elif cr < 10 :
            counter = int(cr*1.25)
        elif cr < 15 :
            counter = int(cr*2)
        else :
            counter = int(cr*2.75)
        while counter > 0 :
            potionContain.append(random.randrange(0, potionList.__len__(), 1))
            counter -= 1
        for i in range(0, potionList.__len__()) :
            if potionList[i] in potionContain :
                count = potionContain.count(potionList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", potionList[i], "\n")
    details = "%s%s" % (details, "\n-Scrolls------------------------------------\n")
    return details    

def Scroll(cr, scroll) :
    details = ""
    scrollList = ["Scroll of Absorb Toxicity (uc, 1125 gp)", "Scroll of Absorb Toxicity (uc, 700 gp)", "Scroll of Acid Arrow (cr, 150 gp)", "Scroll of Acid Splash (cr, 12 gp 5 gp)", "Scroll of Aid (cr, 150 gp)", 
                    "Scroll of Air Bubble (uc, 25 gp)", "Scroll of Air Walk (cr, 700 gp)", "Scroll of Alarm (cr, 25 gp)", "Scroll of Alter Self (cr, 150 gp)", "Scroll of Animal Growth (cr, 1125 gp)", 
                    "Scroll of Animal Shapes (cr, 3000 gp)", "Scroll of Animal Trance (cr, 150 gp)", "Scroll of Animate Dead (cr, 625 gp)", "Scroll of Animate Plants (cr, 2275 gp)", "Scroll of Animate Rope (cr, 25 gp)", 
                    "Scroll of Ant Haul (apg, 25 gp)", "Scroll of Antimagic Field (cr, 1650 gp)", "Scroll of Antimagic Field (cr, 3000 gp)", "Scroll of Aqueous Orb (apg, 375 gp)", "Scroll of Arcane Lock (cr, 175 gp)", 
                    "Scroll of Arcane Mark (cr, 12 gp 5 sp)", "Scroll of Arcane Sight (cr, 375 gp)", "Scroll of Astral Projection (cr, 3825 gp)", "Scroll of Ball Lightning (apg, 700 gp)", "Scroll of Bane (cr, 25 gp)", 
                    "Scroll of Banishment (cr, 2275 gp)", "Scroll of Barkskin (cr, 150 gp)", "Scroll of Bear's Endurance (cr, 150 gp)", "Scroll of Beast Shape (cr, 375 gp)", "Scroll of Beast Shape III (cr, 1125 gp)", 
                    "Scroll of Beast Shape IV (cr, 1650 gp)", "Scroll of Bleed (cr, 12 gp 5 sp)", "Scroll of Blend (arg, 25 gp)", "Scroll of Bless (cr, 25 gp)", "Scroll of Bless Water (cr, 50 gp)", 
                    "Scroll of Blessing of Courage and Life (apg, 150 gp)", "Scroll of Blight (cr, 1125 gp)", "Scroll of Blood Mist (um, 3000 gp)", "Scroll of Blur (cr, 150 gp)", "Scroll of Break (apg, 25 gp)", 
                    "Scroll of Break Enchantment (cr, 1125 gp)", "Scroll of Bull's Strength (cr, 150 gp)", "Scroll of Burning Hands (cr, 25 gp)", "Scroll of Call Lightning (cr, 375 gp)", "Scroll of Calm Animals (cr, 25 gp)", 
                    "Scroll of Cat's Grace (cr, 150 gp)", "Scroll of Cause Fear (cr, 25 gp)", "Scroll of Changestaff (cr, 2275 gp)", "Scroll of Charm Animal (cr, 25 gp)", "Scroll of Charm Monster (cr, 700 gp)", 
                    "Scroll of Charm Person (cr, 25 gp)", "Scroll of Chill Metal (cr, 150 gp)", "Scroll of Chill Touch (cr, 25 gp)", "Scroll of Circle of Death (cr, 2150 gp)", "Scroll of Cleanse (apg, 1125 gp)", 
                    "Scroll of Cloak of Chaos (cr, 3000 gp)", "Scroll of Color Spray (cr, 25 gp)", "Scroll of Command (cr, 25 gp)", "Scroll of Commune (cr, 1625 gp)", "Scroll of Compel Hostility (uc, 25 gp)", 
                    "Scroll of Comprehend Languages (cr, 25 gp)", "Scroll of Cone of Cold (cr, 1125 gp)", "Scroll of Contagion (cr, 375 gp)", "Scroll of Contagious Flame (apg, 1650 gp)", "Scroll of Control Plants (cr, 3000 gp)", 
                    "Scroll of Control Undead (cr, 2275 gp)", "Scroll of Control Weather (cr, 2275 gp)", "Scroll of Corrosive Touch (um, 25 gp)", "Scroll of Create Demiplane (um, 3000 gp)", 
                    "Scroll of Create Greater Undead (cr, 3150 gp)", "Scroll of Create Water (cr, 12 gp 5 sp)", "Scroll of Creeping Doom (cr, 2275 gp)", "Scroll of Crushing Despair (cr, 700 gp)", 
                    "Scroll of Cure Critical Wounds (cr, 700 gp)", "Scroll of Cure Light Wounds (cr, 25 gp)", "Scroll of Cure Moderate Wounds (cr, 150 gp)", "Scroll of Curse Water (cr, 50 gp)", "Scroll of Darkness (cr, 150 gp)", 
                    "Scroll of Daylight (cr, 375 gp)", "Scroll of Daze (cr, 12 gp 5 gp)", "Scroll of Daze Monster (cr, 150 gp)", "Scroll of Deathwatch (cr, 25 gp)", "Scroll of Debilitating Portent (uc, 700 gp)", 
                    "Scroll of Deeper Darkness (cr, 375 gp)", "Scroll of Delay Poison (cr, 150 gp)", "Scroll of Delayed Blast Fireball (cr, 2275 gp)", "Scroll of Demand (cr, 3000 gp)", "Scroll of Destruction (cr, 2775 gp)", 
                    "Scroll of Detect Chaos (cr, 25 gp)", "Scroll of Detect Evil (cr, 25 gp)", "Scroll of Detect Good (cr, 25 gp)", "Scroll of Detect Law (cr, 25 gp)", "Scroll of Detect Magic (cr, 12 gp 5 gp)", 
                    "Scroll of Detect Magic (cr, 12 gp 5 sp)", "Scroll of Detect Poison (cr, 12 gp 5 sp)", "Scroll of Detect Secret Doors (cr, 25 gp)", "Scroll of Detect Snares and Pits (cr, 25 gp)", 
                    "Scroll of Detect Thoughts (cr, 150 gp)", "Scroll of Detect Undead (cr, 25 gp)", "Scroll of Diagnose Disease (um, 25 gp)", "Scroll of Dictum (cr, 2275 gp)", "Scroll of Dimensional Anchor (cr, 700 gp)", 
                    "Scroll of Dimensional Lock (cr, 3000 gp)", "Scroll of Discern Location (cr, 3000 gp)", "Scroll of Disguise Other (um, 150 gp)", "Scroll of Disguise Self (cr, 25 gp)", "Scroll of Disintegrate (cr, 1650 gp)", 
                    "Scroll of Dismissal (cr, 700 gp)", "Scroll of Dispel Magic (cr, 375 gp)", "Scroll of Disrupt Undead (cr, 12 gp 5 sp)", "Scroll of Distracting Cacophony (um, 375 gp)", "Scroll of Divination (cr, 725 gp)", 
                    "Scroll of Divine Favor (cr, 25 gp)", "Scroll of Divine Power (cr, 700 gp)", "Scroll of Dominate Monster (cr, 3825 gp)", "Scroll of Doom (cr, 25 gp)", "Scroll of Dream (cr, 1125 gp)", 
                    "Scroll of Eagle's Splendor (cr, 150 gp)", "Scroll of Earthquake (cr, 3000 gp)", "Scroll of Elemental Body III (cr, 1650 gp)", "Scroll of Elemental Swarm (cr, 3825 gp)", "Scroll of Endure Elements (cr, 25 gp)", 
                    "Scroll of Energy Drain (cr, 3825 gp)", "Scroll of Enlarge Person (cr, 25 gp)", "Scroll of Entangle (cr, 25 gp)", "Scroll of Entropic Shield (cr, 25 gp)", "Scroll of Erase (cr, 25 gp)", 
                    "Scroll of Ethereal Jaunt (cr, 2275 gp)", "Scroll of Etherealness (cr, 3825 gp)", "Scroll of Euphoric Tranquility (apg, 3000 gp)", "Scroll of Expeditious Retreat (cr, 25 gp)", "Scroll of Eyebite (cr, 1650 gp)", 
                    "Scroll of False Life (cr, 150 gp)", "Scroll of Feather Step (apg, 25 gp)", "Scroll of Find the Path (cr, 1650 gp)", "Scroll of Find Traps (cr, 150 gp)", "Scroll of Finger of Death (cr, 2275 gp)", 
                    "Scroll of Finger of Death (cr, 3000 gp)", "Scroll of Fire Shield (cr, 700 gp)", "Scroll of Fire Storm (cr, 2275 gp)", "Scroll of Fireball (cr, 375 gp)", "Scroll of Flame Strike (cr, 700 gp)", 
                    "Scroll of Flaming Sphere (cr, 150 gp)", "Scroll of Flare (cr, 12 gp 5 gp)", "Scroll of Flare (cr, 12 gp 5 sp)", "Scroll of Flare Burst (apg, 25 gp)", "Scroll of Floating Disk (cr, 25 gp)", 
                    "Scroll of Fly (cr, 375 gp)", "Scroll of Fog Cloud (cr, 150 gp)", "Scroll of Forbid Action (um, 25 gp)", "Scroll of Forcecage (cr, 2775 gp)", "Scroll of Forceful Hand (cr, 1650 gp)", 
                    "Scroll of Foresight (cr, 3825 gp)", "Scroll of Form of the Dragon II (cr, 2275 gp)", "Scroll of Form of the Dragon III (cr, 3000 gp)", "Scroll of Freedom (cr, 3825 gp)", 
                    "Scroll of Freezing Sphere (cr, 1650 gp)", "Scroll of Frightful Aspect (uc, 3000 gp)", "Scroll of Frostbite (um, 25 gp)", "Scroll of Gaseous Form (cr, 375 gp)", "Scroll of Gate (cr, 3825 gp)", 
                    "Scroll of Ghost Sound (cr, 12 gp 5 sp)", "Scroll of Ghost Wolf (arg, 700 gp)", "Scroll of Giant Form I (cr, 2275 gp)", "Scroll of Glitterdust (cr, 150 gp)", "Scroll of Globe of Invulnerability (cr, 1650 gp)", 
                    "Scroll of Glyph of Warding (cr, 575 gp)", "Scroll of Goodberry (cr, 25 gp)", "Scroll of Grace (apg, 150 gp)", "Scroll of Grease (cr, 25 gp)", "Scroll of Greater Arcane Sight (cr, 2275 gp)", 
                    "Scroll of Greater Communal Spell Immunity (uc, 3825 gp)", "Scroll of Greater Create Demiplane (um, 3825 gp)", "Scroll of Greater Dispel Magic (cr, 1650 gp)", "Scroll of Greater Glyph of Warding (cr, 2050 gp)", 
                    "Scroll of Greater Hostile Juxtaposition (uc, 2275 gp)", "Scroll of Greater Invisibility (cr, 700 gp)", "Scroll of Greater Planar Ally (cr, 5500 gp)", "Scroll of Greater Planar Binding (cr, 3000 gp)", 
                    "Scroll of Greater Restoration (cr, 7275 gp)", "Scroll of Greater Scrying (cr, 2275 gp)", "Scroll of Greater Shadow Conjuration (cr, 2275 gp)", "Scroll of Greater Spell Immunity (cr, 3000 gp)", 
                    "Scroll of Greater Teleport (cr, 2275 gp)", "Scroll of Guidance (cr, 12 gp 5 sp)", "Scroll of Gust of Wind (cr, 150 gp)", "Scroll of Harm (cr, 1650 gp)", "Scroll of Haste (cr, 375 gp)", 
                    "Scroll of Heal (cr, 1650 gp)", "Scroll of Hide from Animals (cr, 25 gp)", "Scroll of Hide from Undead (cr, 25 gp)", "Scroll of Hideous Laughter (cr, 150 gp)", "Scroll of Hold Animal (cr, 150 gp)", 
                    "Scroll of Hold Monster (cr, 1125 gp)", "Scroll of Hold Portal (cr, 25 gp)", "Scroll of Holy Aura (cr, 3000 gp)", "Scroll of Holy Word (cr, 2275 gp)", "Scroll of Horrid Wilting (cr, 3000 gp)", 
                    "Scroll of Hydraulic Push (apg, 25 gp)", "Scroll of Hypnotism (cr, 25 gp)", "Scroll of Ice Storm (cr, 700 gp)", "Scroll of Icicle Dagger (um, 25 gp)", "Scroll of Identify (cr, 25 gp)", 
                    "Scroll of Illusion of Calm (uc, 25 gp)", "Scroll of Implosion (cr, 3825 gp)", "Scroll of Imprisonment (cr, 3825 gp)", "Scroll of Incendiary Cloud (cr, 3000 gp)", "Scroll of Inflict Light Wounds (cr, 25 gp)", 
                    "Scroll of Inflict Moderate Wounds (cr, 150 gp)", "Scroll of Inflict Serious Wounds (cr, 375 gp)", "Scroll of Insanity (cr, 2275 gp)", "Scroll of Invisibility (cr, 150 gp)", 
                    "Scroll of Invisibility Sphere (cr, 375 gp)", "Scroll of Irresistible Dance (cr, 3000 gp)", "Scroll of Jump (cr, 25 gp)", "Scroll of Keen Edge (cr, 375 gp)", "Scroll of Knock (cr, 150 gp)", 
                    "Scroll of Legend Lore (cr, 1900 gp)", "Scroll of Lesser Create Demiplane (um, 2275 gp)", "Scroll of Lesser Restoration (cr, 150 gp)", "Scroll of Levitate (cr, 150 gp)", 
                    "Scroll of Liberating Command (uc, 25 gp)", "Scroll of Light (cr, 12 gp 5 gp)", "Scroll of Light (cr, 12 gp 5 sp)", "Scroll of Lightning Bolt (cr, 375 gp)", "Scroll of Liveoak (cr, 1650 gp)", 
                    "Scroll of Longstrider (cr, 25 gp)", "Scroll of Mage Armor (cr, 25 gp)", "Scroll of Mage Hand (cr, 12 gp 5 gp)", "Scroll of Mage's Disjunction (cr, 3825 gp)", "Scroll of Mage's Magnificent Mansion (cr, 2275 gp)", 
                    "Scroll of Mage's Sword (cr, 2275 gp)", "Scroll of Magic Aura (cr, 25 gp)", "Scroll of Magic Circle against Evil (cr, 375 gp)", "Scroll of Magic Circle against Good (cr, 375 gp)", 
                    "Scroll of Magic Circle against Law (cr, 375 gp)", "Scroll of Magic Fang (cr, 25 gp)", "Scroll of Magic Jar (cr, 1125 gp)", "Scroll of Magic Missile (cr, 25 gp)", "Scroll of Magic Weapon (cr, 25 gp)", 
                    "Scroll of Major Image (cr, 375 gp)", "Scroll of Make Whole (cr, 150 gp)", "Scroll of Mass Bull's Strength (cr, 1650 gp)", "Scroll of Mass Cat's Grace (cr, 1650 gp)", 
                    "Scroll of Mass Cure Critical Wounds (cr, 3000 gp)", "Scroll of Mass Cure Serious Wounds (cr, 2275 gp)", "Scroll of Mass Eagle's Splendor (cr, 1650 gp)", "Scroll of Mass Enlarge Person (cr, 700 gp)", 
                    "Scroll of Mass Fly (apg, 2275 gp)", "Scroll of Mass Heal (cr, 3825 gp)", "Scroll of Mass Hold Monster (cr, 3825 gp)", "Scroll of Mass Hold Person (cr, 2275 gp)", "Scroll of Mass Icy Prison (um, 3825 gp)", 
                    "Scroll of Mass Inflict Critical Wounds (cr, 3000 gp)", "Scroll of Mass Inflict Light Wounds (cr, 1125 gp)", "Scroll of Mass Inflict Moderate Wounds (cr, 1650 gp)", 
                    "Scroll of Mass Inflict Serious Wounds (cr, 2275 gp)", "Scroll of Mass Invisibility (cr, 2275 gp)", "Scroll of Maze (cr, 3000 gp)", "Scroll of Mending (cr, 12 gp 5 gp)", "Scroll of Mending (cr, 12 gp 5 sp)", 
                    "Scroll of Meteor Swarm (cr, 3825 gp)", "Scroll of Mind Blank (cr, 3000 gp)", "Scroll of Mind Fog (cr, 1125 gp)", "Scroll of Minor Image (cr, 150 gp)", "Scroll of Miracle (cr, 3825 gp)", 
                    "Scroll of Mirror Image (cr, 150 gp)", "Scroll of Mirror Strike (uc, 25 gp)", "Scroll of Monstrous Physique II (um, 700 gp)", "Scroll of Monstrous Physique III (um, 1125 gp)", "Scroll of Mount (cr, 25 gp)", 
                    "Scroll of Nap Stack (apg, 475 gp)", "Scroll of Neutralize Poison (cr, 700 gp)", "Scroll of Nondetection (cr, 425 gp)", "Scroll of Obscure Object (cr, 150 gp)", "Scroll of Obscuring Mist (cr, 25 gp)", 
                    "Scroll of Obsidian Flow (uc, 700 gp)", "Scroll of Open/Close (cr, 12 gp 5 sp)", "Scroll of Orb of the Void (um, 3000 gp)", "Scroll of Overland Flight (cr, 1125 gp)", 
                    "Scroll of Overwhelming Presence (um, 3825 gp)", "Scroll of Owl's Wisdom (cr, 150 gp)", "Scroll of Pass without Trace (cr, 25 gp)", "Scroll of Phantasmal Revenge (apg, 2275 gp)", 
                    "Scroll of Pillar of Life (apg, 1125 gp)", "Scroll of Plague Storm (um, 2275 gp)", "Scroll of Planar Ally (cr, 2900 gp)", "Scroll of Plane Shift (cr, 2275 gp)", "Scroll of Poison (cr, 700 gp)", 
                    "Scroll of Polar Ray (cr, 3000 gp)", "Scroll of Polymorph (cr, 1125 gp)", "Scroll of Polymorph any Object (cr, 3000 gp)", "Scroll of Power Word Blind (cr, 2275 gp)", "Scroll of Power Word Kill (cr, 3825 gp)", 
                    "Scroll of Power Word Stun (cr, 3000 gp)", "Scroll of Prayer (cr, 375 gp)", "Scroll of Prestidigitation (cr, 12 gp 5 gp)", "Scroll of Prismatic Sphere (cr, 3825 gp)", "Scroll of Prismatic Spray (cr, 2275 gp)", 
                    "Scroll of Prismatic Wall (cr, 3000 gp)", "Scroll of Produce Flame (cr, 25 gp)", "Scroll of Project Image (cr, 2280 gp)", "Scroll of Protection from Chaos (cr, 25 gp)", 
                    "Scroll of Protection from Energy (cr, 375 gp)", "Scroll of Protection from Evil (cr, 25 gp)", "Scroll of Protection from Good (cr, 25 gp)", "Scroll of Protection from Law (cr, 25 gp)", 
                    "Scroll of Protection from Spells (cr, 3500 gp)", "Scroll of Purify Food and Drink (cr, 12 gp 5 sp)", "Scroll of Quench (cr, 375 gp)", "Scroll of Rampart (apg, 2275 gp)", 
                    "Scroll of Ray of Enfeeblement (cr, 25 gp)", "Scroll of Ray of Frost (cr, 12 gp 5 gp)", "Scroll of Ray of Sickening (um, 25 gp)", "Scroll of Read Magic (cr, 12 gp 5 gp)", "Scroll of Read Magic (cr, 12 gp 5 sp)", 
                    "Scroll of Reduce Person (cr, 25 gp)", "Scroll of Regenerate (cr, 2275 gp)", "Scroll of Remove Blindness/Deafness (cr, 375 gp)", "Scroll of Remove Fear (cr, 25 gp)", "Scroll of Remove Sickness (um, 25 gp)", 
                    "Scroll of Repel Metal or Stone (cr, 3000 gp)", "Scroll of Repel Vermin (cr, 700 gp)", "Scroll of Repulsion (cr, 1650 gp)", "Scroll of Resinous Skin (uc, 375 gp)", "Scroll of Resist Energy (cr, 150 gp)", 
                    "Scroll of Resistance (cr, 12 gp 5 sp)", "Scroll of Resurrection (cr, 12275 gp)", "Scroll of Returning Weapon (uc, 150 gp)", "Scroll of Reverse Gravity (cr, 2275 gp)", "Scroll of Reverse Gravity (cr, 3000 gp)", 
                    "Scroll of Rope Trick (cr, 150 gp)", "Scroll of Sanctuary (cr, 25 gp)", "Scroll of Scintillating Pattern (cr, 3000 gp)", "Scroll of Scorching Ray (cr, 150 gp)", "Scroll of Screen (cr, 3000 gp)", 
                    "Scroll of Scrying (cr, 1125 gp)", "Scroll of Seamantle (apg, 3000 gp)", "Scroll of See Invisibility (cr, 150 gp)", "Scroll of Sequester (cr, 2275 gp)", "Scroll of Serenity (um, 1125 gp)", 
                    "Scroll of Shadow Anchor (arg, 150 gp)", "Scroll of Shadow Weapon (um, 25 gp)", "Scroll of Shambler (cr, 3825 gp)", "Scroll of Shapechange (cr, 3825 gp)", "Scroll of Shard of Chaos (um, 150 gp)", 
                    "Scroll of Shatter (cr, 150 gp)", "Scroll of Shield (cr, 25 gp)", "Scroll of Shield of Faith (cr, 25 gp)", "Scroll of Shield of Law (cr, 3000 gp)", "Scroll of Shield Other (cr, 150 gp)", 
                    "Scroll of Shillelagh (cr, 25 gp)", "Scroll of Shocking Grasp (cr, 25 gp)", "Scroll of Siege of Trees (uc, 2275 gp)", "Scroll of Silent Image (cr, 25 gp)", "Scroll of Simulacrum (cr, 8775 gp)", 
                    "Scroll of Sleep (cr, 25 gp)", "Scroll of Sleet Storm (cr, 375 gp)", "Scroll of Soften Earth and Stone (cr, 150 gp)", "Scroll of Solid Fog (cr, 700 gp)", "Scroll of Soul Bind (cr, 3825 gp)", 
                    "Scroll of Spark (apg, 12 gp 5 sp)", "Scroll of Speak with Animals (cr, 25 gp)", "Scroll of Speak with Dead (cr, 375 gp)", "Scroll of Spear of Purity (um, 150 gp)", "Scroll of Spectral Hand (cr, 150 gp)", 
                    "Scroll of Spell Turning (cr, 2275 gp)", "Scroll of Spider Climb (cr, 150 gp)", "Scroll of Spike Growth (cr, 375 gp)", "Scroll of Spike Stones (cr, 700 gp)", "Scroll of Spiritual Weapon (cr, 150 gp)", 
                    "Scroll of Stabilize (cr, 12 gp 5 sp)", "Scroll of Stinking Cloud (cr, 375 gp)", "Scroll of Stone Fist (apg, 25 gp)", "Scroll of Stone Shield (arg, 25 gp)", "Scroll of Stone Tell (cr, 1650 gp)", 
                    "Scroll of Stoneskin (cr, 950 gp)", "Scroll of Storm of Vengeance (cr, 3825 gp)", "Scroll of Suggestion (cr, 375 gp)", "Scroll of Summon Monster I (cr, 25 gp)", "Scroll of Summon Monster II (cr, 150 gp)", 
                    "Scroll of Summon Monster III (cr, 375 gp)", "Scroll of Summon Monster IX (cr, 3825 gp)", "Scroll of Summon Monster V (cr, 1125 gp)", "Scroll of Summon Monster VII (cr, 2275 gp)", 
                    "Scroll of Summon Monster VIII (cr, 3000 gp)", "Scroll of Summon Nature's Ally I (cr, 25 gp)", "Scroll of Summon Nature's Ally II (cr, 150 gp)", "Scroll of Summon Nature's Ally IX (cr, 3825 gp)", 
                    "Scroll of Summon Nature's Ally VI (cr, 1650 gp)", "Scroll of Summon Nature's Ally VII (cr, 2275 gp)", "Scroll of Summon Nature's Ally VIII (cr, 3000 gp)", "Scroll of Summon Swarm (cr, 150 gp)", 
                    "Scroll of Sun Metal (uc, 25 gp)", "Scroll of Sunbeam (cr, 2275 gp)", "Scroll of Sunburst (cr, 3000 gp)", "Scroll of Symbol of Death (cr, 8000 gp)", "Scroll of Symbol of Insanity (cr, 8000 gp)", 
                    "Scroll of Symbol of Sleep (cr, 2125 gp)", "Scroll of Symbol of Stunning (cr, 7275 gp)", "Scroll of Tar Pool (uc, 1650 gp)", "Scroll of Telekinetic Charge (uc, 700 gp)", 
                    "Scroll of Telekinetic Sphere (cr, 3000 gp)", "Scroll of Telepathic Bond (cr, 1125 gp)", "Scroll of Teleport (cr, 1125 gp)", "Scroll of Teleport Object (cr, 2275 gp)", 
                    "Scroll of Teleportation Circle (cr, 3825 gp)", "Scroll of Temporal Stasis (cr, 8000 gp)", "Scroll of Time Stop (cr, 3825 gp)", "Scroll of Tongues (cr, 375 gp)", "Scroll of Touch of Fatigue (cr, 12 gp 5 gp)", 
                    "Scroll of Touch of Idiocy (cr, 150 gp)", "Scroll of Touch of the Sea (apg, 25 gp)", "Scroll of Transformation (cr, 1650 gp)", "Scroll of Transmute Metal to Wood (cr, 2275 gp)", 
                    "Scroll of Trap the Soul (cr, 23000 gp)", "Scroll of Tree Shape (cr, 150 gp)", "Scroll of Tree Stride (cr, 1125 gp)", "Scroll of True Form (apg, 700 gp)", "Scroll of True Resurrection (cr, 28825 gp)", 
                    "Scroll of True Strike (cr, 25 gp)", "Scroll of Undead Anatomy III (um, 1650 gp)", "Scroll of Unholy Aura (cr, 3000 gp)", "Scroll of Unseen Servant (cr, 25 gp)", "Scroll of Unwitting Ally (apg, 12 gp 5 sp)", 
                    "Scroll of Vanish (apg, 25 gp)", "Scroll of Ventriloquism (cr, 25 gp)", "Scroll of Vermin Shape I (um, 700 gp)", "Scroll of Virtue (cr, 12 gp 5 sp)", "Scroll of Vision (cr, 2525 gp)", 
                    "Scroll of Voice Alteration (um, 25 gp)", "Scroll of Vortex (apg, 2275 gp)", "Scroll of Wall of Ice (cr, 700 gp)", "Scroll of Wall of Iron (cr, 1700 gp)", "Scroll of Wall of Lava (apg, 3000 gp)", 
                    "Scroll of Wall of Stone (cr, 1125 gp)", "Scroll of Wandering Star Motes (apg, 700 gp)", "Scroll of Water Walk (cr, 375 gp)", "Scroll of Web (cr, 150 gp)", "Scroll of Whispering Wind (cr, 150 gp)", 
                    "Scroll of Wind Blades (arg, 1125 gp)", "Scroll of Wish (cr, 3825 gp)", "Scroll of Word of Chaos (cr, 2275 gp)", "Scroll of World Wave (apg, 3825 gp)"]
    possibility = scroll * random.randrange(1, 101, 1)
    scrollContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*.333)
        elif cr < 10 :
            counter = int(cr*.444)
        elif cr < 15 :
            counter = int(cr*.555)
        else :
            counter = int(cr*.666)
        while counter > 0 :
            scrollContain.append(random.randrange(0, scrollList.__len__(), 1))
            counter -= 1
        for i in range(0, scrollList.__len__()) :
            if scrollList[i] in scrollContain :
                count = scrollContain.count(scrollList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", scrollList[i], "\n")
    details = "%s%s" % (details, "\n-Wand---------------------------------------\n")
    return details    

def Wand(cr, wand) :
    details = ""
    wandList = ["Wand of Acid Arrow (cr, 4500 gp)", "Wand of Acid Arrow (cr, 4500 gp) (design provides clue to function)", "Wand of Acid Arrow (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Acid Splash (cr, 375 gp)", "Wand of Acid Splash (cr, 375 gp) (design provides clue to function)", "Wand of Acid Splash (cr, 375 gp) (inscription provides clue to function)", 
                "Wand of Aid (cr, 4500 gp)", "Wand of Aid (cr, 4500 gp) (inscription provides clue to function)", "Wand of Air Walk (cr, 21000 gp)", "Wand of Alarm (cr, 750 gp)", 
                "Wand of Alarm (cr, 750 gp) (design provides clue to function)", "Wand of Alarm (cr, 750 gp) (inscription provides clue to function)", "Wand of Align Weapon (cr, 4500 gp)", 
                "Wand of Alter Self (cr, 4500 gp) (design provides clue to function)", "Wand of Alter Self (cr, 4500 gp) (inscription provides clue to function)", "Wand of Animal Aspect (uc, 4500 gp)", 
                "Wand of Animate Rope (cr, 750 gp)", "Wand of Animate Rope (cr, 750 gp) (inscription provides clue to function)", "Wand of Ant Haul (apg, 750 gp)", "Wand of Arcane Eye (cr, 21000 gp)", 
                "Wand of Arcane Eye (cr, 21000 gp) (inscription provides clue to function)", "Wand of Arcane Mark (cr, 375 gp) (design provides clue to function)", 
                "Wand of Arcane Mark (cr, 375 gp) (inscription provides clue to function)", "Wand of Arcane Sight (cr, 11250 gp)", "Wand of Archon's Aura (um, 11250 gp)", 
                "Wand of Archon's Aura (um, 11250 gp) (design provides clue to function)", "Wand of Ash Storm (um, 11250 gp) (inscription provides clue to function)", "Wand of Aspect of the Bear (apg, 4500 gp)", 
                "Wand of Aspect of the Falcon (apg, 750 gp) (design provides clue to function)", "Wand of Augury (cr, 5750 gp)", "Wand of Ball Lightning (apg, 21000 gp) (design provides clue to function)", 
                "Wand of Bane (cr, 750 gp)", "Wand of Bane (cr, 750 gp) (inscription provides clue to function)", "Wand of Barkskin (cr, 4500 gp)", "Wand of Barkskin (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Barkskin (cr, 4500 gp) (inscription provides clue to function)", "Wand of Bear's Endurance (cr, 4500 gp)", "Wand of Beast Shape I (cr, 11250 gp)", 
                "Wand of Beast Shape I (cr, 11250 gp) (design provides clue to function)", "Wand of Beast Shape I (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Bestow Weapon Proficiency (uc, 4500 gp)", "Wand of Black Tentacles (cr, 21000 gp)", "Wand of Black Tentacles (cr, 21000 gp) (design provides clue to function)", "Wand of Bleed (cr, 375 gp)", 
                "Wand of Bleed (cr, 375 gp) (design provides clue to function)", "Wand of Bless (cr, 750 gp)", "Wand of Bless (cr, 750 gp) (design provides clue to function)", 
                "Wand of Bless (cr, 750 gp) (inscription provides clue to function)", "Wand of Bless Water (cr, 2000 gp)", "Wand of Bless Weapon (cr, 750 gp)", "Wand of Blindness/Deafness (cr, 4500 gp)", 
                "Wand of Blink (cr, 11250 gp)", "Wand of Blur (cr, 4500 gp)", "Wand of Bull's Strength (cr, 4500 gp)", "Wand of Bull's Strength (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Bull's Strength (cr, 4500 gp) (inscription provides clue to function)", "Wand of Burning Gaze (apg, 4500 gp)", "Wand of Burning Gaze (apg, 4500 gp) (design provides clue to function)", 
                "Wand of Burning Hands (cr, 750 gp)", "Wand of Burning Hands (cr, 750 gp) (design provides clue to function)", "Wand of Burning Hands (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Call Lightning (cr, 11250 gp)", "Wand of Call Lightning (cr, 11250 gp) (design provides clue to function)", "Wand of Calm Aniimals (cr, 750 gp)", 
                "Wand of Calm Emotions (cr, 4500 gp) (design provides clue to function)", "Wand of Cat's Grace (cr, 4500 gp)", "Wand of Cat's Grace (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Cat's Grace (cr, 4500 gp) (inscription provides clue to function)", "Wand of Cause Fear (cr, 750 gp)", "Wand of Cause Fear (cr, 750 gp) (design provides clue to function)", 
                "Wand of Cause Fear (cr, 750 gp) (inscription provides clue to function)", "Wand of Charm Animal (cr, 750 gp)", "Wand of Charm Animal (cr, 750 gp) (design provides clue to function)", 
                "Wand of Charm Person (cr, 750 gp)", "Wand of Charm Person (cr, 750 gp) (design provides clue to function)", "Wand of Charm Person (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Chill Metal (cr, 4500 gp)", "Wand of Chill Metal (cr, 4500 gp) (design provides clue to function)", "Wand of Chill touch (cr, 750 gp)", "Wand of Clairaudience/Clairvoyance (cr, 11250 gp)", 
                "Wand of Clairaudience/Clairvoyance (cr, 11250 gp) (inscription provides clue to function)", "Wand of Color Spray (cr, 750 gp)", "Wand of Color Spray (cr, 750 gp) (design provides clue to function)", 
                "Wand of Command (cr, 750 gp)", "Wand of Command (cr, 750 gp) (design provides clue to function)", "Wand of Command (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Command Undead (cr, 4500 gp) (design provides clue to function)", "Wand of Commune with Nature (cr, 30000 gp)", "Wand of Compel Hostility (uc, 750 gp)", 
                "Wand of Compel Hostility (uc, 750 gp) (inscription provides clue to function)", "Wand of Comprehend Languages (cr, 750 gp)", "Wand of Confusion (cr, 21000 gp)", "Wand of Continual Flame (cr, 7000 gp)", 
                "Wand of Corrosive Touch (um, 750 gp)", "Wand of Create Food and Water (cr, 11250 gp)", "Wand of Create Water (cr, 375 gp)", "Wand of Create Water (cr, 375 gp) (design provides clue to function)", 
                "Wand of Crushing Despair (cr, 21000 gp)", "Wand of Crushing Despair (cr, 21000 gp) (design provides clue to function)", "Wand of Cure Critical Wounds (cr, 21000 gp)", 
                "Wand of Cure Critical Wounds (cr, 21000 gp) (inscription provides clue to function)", "Wand of Cure Light Wounds (cr, 750 gp)", "Wand of Cure Light Wounds (cr, 750 gp) (design provides clue to function)", 
                "Wand of Cure Light Wounds (cr, 750 gp) (inscription provides clue to function)", "Wand of Cure Moderate Wounds (cr, 4500 gp)", "Wand of Cure Moderate Wounds (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Cure Moderate Wounds (cr, 4500 gp) (inscription provides clue to function)", "Wand of Cure Serious Wounds (cr, 11250 gp)", "Wand of Cure Serious Wounds (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Cure Serious Wounds (cr, 11250 gp) (inscription provides clue to function)", "Wand of Curse Water (cr, 2000 gp)", "Wand of Dancing Lights (cr, 375 gp)", "Wand of Darkness (cr, 4500 gp)", 
                "Wand of Darkness (cr, 4500 gp) (design provides clue to function)", "Wand of Darkness (cr, 4500 gp) (inscription provides clue to function)", "Wand of Darkvision (cr, 4500 gp)", 
                "Wand of Darkvision (cr, 4500 gp) (inscription provides clue to function)", "Wand of Daylight (cr, 11250 gp)", "Wand of Daylight (cr, 11250 gp) (design provides clue to function)", "Wand of Daze (cr, 375 gp)", 
                "Wand of Daze (cr, 375 gp) (inscription provides clue to function)", "Wand of Daze Monster (cr, 4500 gp)", "Wand of Daze Monster (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Death Knell (cr, 4500 gp)", "Wand of Death Knell (cr, 4500 gp) (design provides clue to function)", "Wand of Deathwatch (cr, 750 gp)", "Wand of Deep Slumber (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Deeper Darkness (cr, 11250 gp)", "Wand of Defensive Shock (um, 4500 gp)", "Wand of Defensive Shock (um, 4500 gp) (inscription provides clue to function)", "Wand of Delay Poison (cr, 4500 gp)", 
                "Wand of Delay Poison (cr, 4500 gp) (design provides clue to function)", "Wand of Desecrate (cr, 5750 gp)", "Wand of Desecrate (cr, 5750 gp) (design provides clue to function)", 
                "Wand of Detect Animals or Plants (cr, 750 gp)", "Wand of Detect Chaos (cr, 750 gp)", "Wand of Detect Evil (cr, 750 gp)", "Wand of Detect Good (cr, 750 gp)", "Wand of Detect Magic (cr, 375 gp)", 
                "Wand of Detect Magic (cr, 375 gp) (design provides clue to function)", "Wand of Detect Magic (cr, 375 gp) (inscription provides clue to function)", "Wand of Detect Poison (cr, 375 gp)", 
                "Wand of Detect Poison (cr, 375 gp) (design provides clue to function)", "Wand of Detect Scrying (cr, 21000 gp) (inscription provides clue to function)", "Wand of Detect Secret Doors (cr, 750 gp)", 
                "Wand of Detect Secret Doors (cr, 750 gp) (design provides clue to function)", "Wand of Detect Thoughts (cr, 4500 gp)", "Wand of Detect Undead (cr, 750 gp) (design provides clue to function)", 
                "Wand of Dimension Door (cr, 21000 gp)", "Wand of Dimensional Anchor (cr, 21000 gp)", "Wand of Diminish Plants (cr, 11250 gp)", "Wand of Disguise Other (um, 4500 gp)", 
                "Wand of Disguise Other (um, 4500 gp) (design provides clue to function)", "Wand of Disguise Other (um, 4500 gp) (inscription provides clue to function)", "Wand of Disguise Self (cr, 750 gp)", 
                "Wand of Disguise Self (cr, 750 gp) (inscription provides clue to function)", "Wand of Dispel Magic (cr, 11250 gp)", "Wand of Dispel Magic (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Dispel Magic (cr, 11250 gp) (inscription provides clue to function)", "Wand of Displacement (cr, 11250 gp)", "Wand of Displacement (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Disrupt Undead (cr, 375 gp)", "Wand of Disrupt Undead (cr, 375 gp) (design provides clue to function)", "Wand of Divination (cr, 22250 gp) (design provides clue to function)", 
                "Wand of Divine Favor (cr, 750 gp)", "Wand of Divine Favor (cr, 750 gp) (design provides clue to function)", "Wand of Divine Favor (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Doom (cr, 750 gp)", "Wand of Dragon's Breath (apg, 21000 gp)", "Wand of Dragon's Breath (apg, 21000 gp) (design provides clue to function)", "Wand of Eagle's Splendor (cr, 4500 gp)", 
                "Wand of Eagle's Splendor (cr, 4500 gp) (design provides clue to function)", "Wand of Eagle's Splendor (cr, 4500 gp) (inscription provides clue to function)", "Wand of Effortless Armor (uc, 4500 gp)", 
                "Wand of Effortless Armor (uc, 4500 gp) (inscription provides clue to function)", "Wand of Elemental Aura (apg, 11250 gp)", "Wand of Elemental Body I (cr, 21000 gp)", "Wand of Elemental Touch (apg, 4500 gp)", 
                "Wand of Elemental Touch (apg, 4500 gp) (design provides clue to function)", "Wand of Elemental Touch (apg, 4500 gp) (inscription provides clue to function)", "Wand of Endure Elements (cr, 750 gp)", 
                "Wand of Enervation (cr, 21000 gp)", "Wand of Enlarge Person (cr, 750 gp)", "Wand of Enlarge Person (cr, 750 gp) (design provides clue to function)", "Wand of Enlarge Person (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Entangle (cr, 750 gp)", "Wand of Entangle (cr, 750 gp) (design provides clue to function)", "Wand of Entangle (cr, 750 gp) (inscription provides clue to function)", "Wand of Enthrall (cr, 4500 gp)", 
                "Wand of Entropic Shield (cr, 750 gp)", "Wand of Entropic Shield (cr, 750 gp) (inscription provides clue to function)", "Wand of Erase (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Expeditious Retreat (cr, 750 gp)", "Wand of Expeditious Retreat (cr, 750 gp) (design provides clue to function)", "Wand of Expeditious Retreat (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Faerie Fire (cr, 750 gp)", "Wand of False Life (cr, 4500 gp)", "Wand of False Life (cr, 4500 gp) (design provides clue to function)", "Wand of Fear (cr, 21000 gp) (design provides clue to function)", 
                "Wand of Feather Fall (cr, 750 gp)", "Wand of Feather Fall (cr, 750 gp) (inscription provides clue to function)", "Wand of Feather Step (apg, 750 gp)", 
                "Wand of Feather Step (apg, 750 gp) (inscription provides clue to function)", "Wand of Find Traps (cr, 4500 gp)", "Wand of Find Traps (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Find Traps (cr, 4500 gp) (inscription provides clue to function)", "Wand of Fire Shield (cr, 21000 gp)", "Wand of Fire Trap (cr, 5750 gp)", "Wand of Fireball (cr, 11250 gp)", 
                "Wand of Fireball (cr, 11250 gp) (inscription provides clue to function)", "Wand of Flame Arrow (cr, 11250 gp)", "Wand of Flame Blade (cr, 4500 gp)", 
                "Wand of Flame Blade (cr, 4500 gp) (design provides clue to function)", "Wand of Flaming Sphere (cr, 4500 gp)", "Wand of Flaming Sphere (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Flare (cr, 375 gp)", "Wand of Flare (cr, 375 gp) (design provides clue to function)", "Wand of Fly (cr, 11250 gp)", "Wand of Fog Cloud (cr, 4500 gp)", 
                "Wand of Fog Cloud (cr, 4500 gp) (design provides clue to function)", "Wand of Fog Cloud (cr, 4500 gp) (inscription provides clue to function)", "Wand of Force Punch (um, 11250 gp)", 
                "Wand of Fox's Cunning (cr, 4500 gp)", "Wand of Fox's Cunning (cr, 4500 gp) (design provides clue to function)", "Wand of Freedom of Movement (cr, 21000 gp)", "Wand of Gaseous Form (cr, 11250 gp)", 
                "Wand of Gentle Repose (cr, 4500 gp)", "Wand of Ghost Sound (cr, 375 gp)", "Wand of Ghost Sound (cr, 375 gp) (inscription provides clue to function)", "Wand of Ghost Wolf (arg, 21000 gp)", 
                "Wand of Ghost Wolf (arg, 21000 gp) (design provides clue to function)", "Wand of Ghoul Touch (cr, 4500 gp)", "Wand of Ghoul Touch (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Ghoul Touch (cr, 4500 gp) (inscription provides clue to function)", "Wand of Giant Vermin (cr, 21000 gp)", "Wand of Glibness (cr, 15750 gp)", 
                "Wand of Glibness (cr, 15750 gp) (design provides clue to function)", "Wand of Glide (apg, 4500 gp)", "Wand of Glide (apg, 4500 gp) (inscription provides clue to function)", 
                "Wand of Glyph of Warding (cr, 21250 gp)", "Wand of Good Hope (cr, 15750 gp)", "Wand of Goodberry (cr, 750 gp)", "Wand of Goodberry (cr, 750 gp) (design provides clue to function)", 
                "Wand of Goodberry (cr, 750 gp) (inscription provides clue to function)", "Wand of Grease (cr, 750 gp)", "Wand of Grease (cr, 750 gp) (design provides clue to function)", 
                "Wand of Grease (cr, 750 gp) (inscription provides clue to function)", "Wand of Greater Darkvision (um, 21000 gp) (inscription provides clue to function)", "Wand of Greater Invisibility (cr, 21000 gp)", 
                "Wand of Greater Invisibility (cr, 21000 gp) (inscription provides clue to function)", "Wand of Greater Magic Fang (cr, 11250 gp)", "Wand of Greater Magic Weapon (cr, 11250 gp)", 
                "Wand of Groundswell (apg, 4500 gp)", "Wand of Guidance (cr, 375 gp)", "Wand of Guidance (cr, 375 gp) (design provides clue to function)", "Wand of Gust of Wind (cr, 4500 gp)", 
                "Wand of Hallucinatory Terrain (cr, 21000 gp)", "Wand of Halt Undead (cr, 11250 gp)", "Wand of Haste (cr, 11250 gp)", "Wand of Haste (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Haste (cr, 11250 gp) (inscription provides clue to function)", "Wand of Heal Mount (cr, 15750 gp)", "Wand of Heat Metal (cr, 4500 gp)", "Wand of Heat Metal (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Helping Hand (cr, 11250 gp)", "Wand of Heroism (cr, 11250 gp)", "Wand of Hide from Animals (cr, 750 gp)", "Wand of Hide from Animals (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Hide from Undead (cr, 750 gp)", "Wand of Hideous Laughter (cr, 750 gp)", "Wand of Hold Person (cr, 4500 gp)", "Wand of Hold Person (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Hold Portal (cr, 750 gp)", "Wand of Holy Smite (cr, 21000 gp) (design provides clue to function)", "Wand of Hostile Levitation (uc, 11250 gp)", 
                "Wand of Hydraulic Torrent (apg, 11250 gp) (inscription provides clue to function)", "Wand of Hypnotic Pattern (cr, 4500 gp)", "Wand of Hypnotism (cr, 750 gp)", 
                "Wand of Hypnotism (cr, 750 gp) (inscription provides clue to function)", "Wand of Ice Storm (cr, 21000 gp)", "Wand of Ice Storm (cr, 21000 gp) (inscription provides clue to function)", 
                "Wand of Icicle Dagger (um, 750 gp)", "Wand of Identify (cr, 750 gp)", "Wand of Identify (cr, 750 gp) (design provides clue to function)", "Wand of Identify (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Ill Omen (apg, 750 gp)", "Wand of Imbue with Spell Ability (cr, 21000 gp)", "Wand of Inflict Critical Wounds (cr, 21000 gp)", "Wand of Inflict Critical Wounds (cr, 21000 gp) (design provides clue to function)", 
                "Wand of Inflict Light Wounds (cr, 750 gp)", "Wand of Inflict Light Wounds (cr, 750 gp) (design provides clue to function)", "Wand of Inflict Light Wounds (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Inflict Moderate Wounds (cr, 4500 gp)", "Wand of Inflict Moderate Wounds (cr, 4500 gp) (design provides clue to function)", "Wand of Inflict Moderate Wounds (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Inflict Serious Wounds (cr, 11250 gp)", "Wand of Inflict Serious Wounds (cr, 11250 gp) (inscription provides clue to function)", "Wand of Invisibility (cr, 4500 gp)", "Wand of Invisibility (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Invisibility (cr, 4500 gp) (inscription provides clue to function)", "Wand of Invisibility Purge (cr, 11250 gp)", "Wand of Invisibility Purge (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Invisibility Sphere (cr, 11250 gp)", "Wand of Jump (cr, 750 gp)", "Wand of Jump (cr, 750 gp) (inscription provides clue to function)", "Wand of Keen Edge (cr, 11250 gp)", 
                "Wand of Know Direction (cr, 375 gp)", "Wand of Lesser Confusion (cr, 750 gp)", "Wand of Lesser Confusion (cr, 750 gp) (design provides clue to function)", "Wand of Lesser Confusion (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Lesser Globe of Invulnerability (cr, 21000 gp)", "Wand of Lesser Planar Ally (cr, 46000 gp)", "Wand of Lesser Restoration (cr, 4500 gp)", "Wand of Lesser Restoration (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Levitate (cr, 4500 gp)", "Wand of Levitate (cr, 4500 gp) (design provides clue to function)", "Wand of Levitate (cr, 4500 gp) (inscription provides clue to function)", "Wand of Light (cr, 375 gp)", 
                "Wand of Light (cr, 375 gp) (inscription provides clue to function)", "Wand of Lightning Bolt (cr, 11250 gp)", "Wand of Lightning Bolt (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Lightning Bolt (cr, 11250 gp) (inscription provides clue to function)", "Wand of Locate Object (cr, 4500 gp)", "Wand of Longstrider (cr, 750 gp)", "Wand of Longstrider (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Lullaby (cr, 375 gp)", "Wand of Lullaby (cr, 375 gp) (design provides clue to function)", "Wand of Mage Armor (cr, 750 gp)", "Wand of Mage Armor (cr, 750 gp) (design provides clue to function)", 
                "Wand of Mage Armor (cr, 750 gp) (inscription provides clue to function)", "Wand of Mage Hand (cr, 375 gp)", "Wand of Mage Hand (cr, 375 gp) (inscription provides clue to function)", 
                "Wand of Magic Aura (cr, 750 gp)", "Wand of Magic Aura (cr, 750 gp) (inscription provides clue to function)", "Wand of Magic Circle against Chaos (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Magic Circle against Good (cr, 11250 gp)", "Wand of Magic Circle against Law (cr, 11250 gp)", "Wand of Magic Fang (cr, 750 gp)", "Wand of Magic Fang (cr, 750 gp) (design provides clue to function)", 
                "Wand of Magic Fang (cr, 750 gp) (inscription provides clue to function)", "Wand of Magic Missile (cr, 750 gp)", "Wand of Magic Missile (cr, 750 gp) (design provides clue to function)", 
                "Wand of Magic Missile (cr, 750 gp) (inscription provides clue to function)", "Wand of Magic Mouth (cr, 1250 gp)", "Wand of Magic Mouth (cr, 1250 gp) (design provides clue to function)", 
                "Wand of Magic Mouth (cr, 1250 gp) (inscription provides clue to function)", "Wand of Magic Stone (cr, 750 gp)", "Wand of Magic Stone (cr, 750 gp) (design provides clue to function)", 
                "Wand of Magic Vestment (cr, 11250 gp)", "Wand of Magic Vestment (cr, 11250 gp) (inscription provides clue to function)", "Wand of Magic Weapon (cr, 750 gp)", 
                "Wand of Magic Weapon (cr, 750 gp) (inscription provides clue to function)", "Wand of Major Image (cr, 11250 gp)", "Wand of Major Image (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Make Whole (cr, 4500 gp) (design provides clue to function)", "Wand of Mass Enlarge Person (cr, 21000 gp)", "Wand of Mass Enlarge Person (cr, 21000 gp) (design provides clue to function)", 
                "Wand of Meld into Stone (cr, 11250 gp)", "Wand of Mending (cr, 375 gp)", "Wand of Mending (cr, 375 gp) (design provides clue to function)", "Wand of Message (cr, 375 gp)", 
                "Wand of Message (cr, 375 gp) (design provides clue to function)", "Wand of Minor Creation (cr, 21000 gp)", "Wand of Minor Image (cr, 4500 gp)", "Wand of Mirror Image (cr, 4500 gp)", 
                "Wand of Modify Memory (cr, 30000 gp)", "Wand of Modify Memory (cr, 30000 gp) (inscription provides clue to function)", "Wand of Mount (cr, 750 gp)", "Wand of Neutralize Poison (cr, 11250 gp)", 
                "Wand of Obscure Object (cr, 750 gp)", "Wand of Obscure Object (cr, 750 gp) (design provides clue to function)", "Wand of Obscuring Mist (cr, 750 gp)", 
                "Wand of Obscuring Mist (cr, 750 gp) (design provides clue to function)", "Wand of Open/Close (cr, 375 gp)", "Wand of Order's Wrath (cr, 21000 gp)", "Wand of Owl's Wisdom (cr, 4500 gp)", 
                "Wand of Owl's Wisdom (cr, 4500 gp) (design provides clue to function)", "Wand of Owl's Wisdom (cr, 4500 gp) (inscription provides clue to function)", "Wand of Phantom Trap (cr, 7000 gp)", 
                "Wand of Poison (cr, 11250 gp)", "Wand of Prayer (cr, 11250 gp)", "Wand of Prayer (cr, 11250 gp) (design provides clue to function)", "Wand of Prayer (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Prestidigitation (cr, 375 gp)", "Wand of Prestidigitation (cr, 375 gp) (design provides clue to function)", "Wand of Prestidigitation (cr, 375 gp) (inscription provides clue to function)", 
                "Wand of Produce Flame (cr, 750 gp)", "Wand of Produce Flame (cr, 750 gp) (design provides clue to function)", "Wand of Protection from Arrows (cr, 4500 gp)", "Wand of Protection from Chaos (cr, 750 gp)", 
                "Wand of Protection from Chaos (cr, 750 gp) (inscription provides clue to function)", "Wand of Protection from Energy (cr, 11250 gp)", "Wand of Protection from Energy (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Protection from Energy (cr, 11250 gp) (inscription provides clue to function)", "Wand of Protection from Evil (cr, 750 gp)", "Wand of Protection from Evil (cr, 750 gp) (design provides clue to function)", 
                "Wand of Protection from Evil (cr, 750 gp) (inscription provides clue to function)", "Wand of Protection from Good (cr, 750 gp)", "Wand of Protection from Good (cr, 750 gp) (design provides clue to function)", 
                "Wand of Protection from Law (cr, 750 gp)", "Wand of Protection from Law (cr, 750 gp) (inscription provides clue to function)", "Wand of Purify Food and Drink (cr, 375 gp)", "Wand of Purify Food and Drink (cr, 375 gp) (design provides clue to function)", 
                "Wand of Purify Food and Drink (cr, 375 gp) (inscription provides clue to function)", "Wand of Pyrotechnics (cr, 4500 gp)", "Wand of Pyrotechnics (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Ray of Enfeeblement (cr, 750 gp)", "Wand of Ray of Enfeeblement (cr, 750 gp) (design provides clue to function)", "Wand of Ray of Exhaustion (cr, 11250 gp)", "Wand of Ray of Frost (cr, 375 gp)", 
                "Wand of Ray of Frost (cr, 375 gp) (design provides clue to function)", "Wand of Ray of Frost (cr, 375 gp) (inscription provides clue to function)", "Wand of Read Magic (cr, 375 gp)", 
                "Wand of Read Magic (cr, 375 gp) (design provides clue to function)", "Wand of Read Magic (cr, 375 gp) (inscription provides clue to function)", "Wand of Reduce Animal (cr, 4500 gp)", 
                "Wand of Reduce Person (cr, 750 gp)", "Wand of Reduce Person (cr, 750 gp) (design provides clue to function)", "Wand of Reduce Person (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Reincarnate (cr, 21000 gp)", "Wand of Remove Curse (cr, 11250 gp)", "Wand of Remove Fear (cr, 750 gp)", "Wand of Remove Fear (cr, 750 gp) (design provides clue to function)", 
                "Wand of Remove Fear (cr, 750 gp) (inscription provides clue to function)", "Wand of Remove Paralysis (cr, 4500 gp)", "Wand of Resilient Sphere (cr, 21000 gp)", "Wand of Resist Energy (cr, 4500 gp)", 
                "Wand of Resist Energy (cr, 4500 gp) (design provides clue to function)", "Wand of Resist Energy (cr, 4500 gp) (inscription provides clue to function)", "Wand of Resistance (cr, 375 gp)", 
                "Wand of Restoration (cr, 71000 gp)", "Wand of Ride the Waves (um, 21000 gp)", "Wand of Rope Trick (cr, 4500 gp)", "Wand of Sanctuary (cr, 750 gp)", "Wand of Sanctuary (cr, 750 gp) (design provides clue to function)", 
                "Wand of Scare (cr, 4500 gp)", "Wand of Scare (cr, 4500 gp) (inscription provides clue to function)", "Wand of Scorching Ray (cr, 4500 gp)", "Wand of Scorching Ray (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Scorching Ray (cr, 4500 gp) (inscription provides clue to function)", "Wand of Scrying (cr, 21000 gp)", "Wand of Searing Light (cr, 11250 gp)", "Wand of Searing Light (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Searing Light (cr, 11250 gp) (inscription provides clue to function)", "Wand of See Invisibility (cr, 4500 gp)", "Wand of See Invisibility (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Sepia Snake Sigil (cr, 36250 gp) (inscription provides clue to function)", "Wand of Share Language (apg, 4500 gp)", "Wand of Shield (cr, 750 gp)", "Wand of Shield (cr, 750 gp) (design provides clue to function)", 
                "Wand of Shield (cr, 750 gp) (inscription provides clue to function)", "Wand of Shield of Faith (cr, 750 gp)", "Wand of Shield of Faith (cr, 750 gp) (design provides clue to function)", 
                "Wand of Shield of Faith (cr, 750 gp) (inscription provides clue to function)", "Wand of Shield Other (cr, 4500 gp)", "Wand of Shield Other (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Shillelagh (cr, 750 gp)", "Wand of Shillelagh (cr, 750 gp) (design provides clue to function)", "Wand of Shock Shield (uc, 750 gp)", "Wand of Shock Shield (uc, 750 gp) (inscription provides clue to function)", 
                "Wand of Shocking Grasp (cr, 750 gp)", "Wand of Shocking Grasp (cr, 750 gp) (inscription provides clue to function)", "Wand of Shout (cr, 21000 gp) (inscription provides clue to function)", 
                "Wand of Silence (cr, 4500 gp)", "Wand of Silence (cr, 4500 gp) (inscription provides clue to function)", "Wand of Silent Image (cr, 750 gp)", "Wand of Silent Image (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Sleep (cr, 750 gp)", "Wand of Sleep (cr, 750 gp) (design provides clue to function)", "Wand of Sleep (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Sleet Storm (cr, 11250 gp) (design provides clue to function)", "Wand of Slow (cr, 11250 gp)", "Wand of Slow (cr, 11250 gp) (design provides clue to function)", "Wand of Snare (cr, 11250 gp)", 
                "Wand of Solid Fog (cr, 21000 gp)", "Wand of Solid Fog (cr, 21000 gp) (inscription provides clue to function)", "Wand of Sound Burst (cr, 4500 gp)", "Wand of Spark (apg, 375 gp)", 
                "Wand of Spark (apg, 375 gp) (design provides clue to function)", "Wand of Spark (apg, 375 gp) (inscription provides clue to function)", "Wand of Speak with Animals (cr, 750 gp)", 
                "Wand of Speak with Animals (cr, 750 gp) (design provides clue to function)", "Wand of Speak with Animals (cr, 750 gp) (inscription provides clue to function)", "Wand of Speak with Dead (cr, 11250 gp)", 
                "Wand of Speak with Dead (cr, 11250 gp) (design provides clue to function)", "Wand of Speak with Dead (cr, 11250 gp) (inscription provides clue to function)", "Wand of Spectral Hand (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Spell Immunity (cr, 21000 gp) (inscription provides clue to function)", "Wand of Spider Climb (cr, 4500 gp)", "Wand of Spider Climb (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Spiritual Weapon (cr, 4500 gp)", "Wand of Spiritual Weapon (cr, 4500 gp) (design provides clue to function)", "Wand of Stabilize (cr, 375 gp)", 
                "Wand of Stabilize (cr, 375 gp) (inscription provides clue to function)", "Wand of Status (cr, 4500 gp)", "Wand of Stinking Cloud (cr, 11250 gp)", "Wand of Stone Fist (apg, 750 gp)", 
                "Wand of Stone Fist (apg, 750 gp) (inscription provides clue to function)", "Wand of Stone Shape (cr, 11250 gp)", "Wand of Stone Shape (cr, 11250 gp) (inscription provides clue to function)", 
                "Wand of Stone Shield (arg, 750 gp)", "Wand of Stoneskin (cr, 33500 gp)", "Wand of Suggestion (cr, 11250 gp)", "Wand of Summon Minor Monster (um, 750 gp)", 
                "Wand of Summon Minor Monster (um, 750 gp) (design provides clue to function)", "Wand of Summon Monster I (cr, 750 gp)", "Wand of Summon Monster I (cr, 750 gp) (design provides clue to function)", 
                "Wand of Summon Monster II (cr, 4500 gp)", "Wand of Summon Monster II (cr, 4500 gp) (design provides clue to function)", "Wand of Summon Monster II (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Summon Monster IV (cr, 21000 gp) (inscription provides clue to function)", "Wand of Summon Nature's Ally I (cr, 750 gp)", "Wand of Summon Nature's Ally I (cr, 750 gp) (design provides clue to function)", 
                "Wand of Summon Nature's Ally II (cr, 4500 gp)", "Wand of Summon Nature's Ally II (cr, 4500 gp) (design provides clue to function)", "Wand of Summon Nature's Ally II (cr, 4500 gp) (inscription provides clue to function)", 
                "Wand of Summon Nature's Ally IV (cr, 21000 gp)", "Wand of Summon Swarm (cr, 4500 gp)", "Wand of Tiny Hut (cr, 11250 gp)", "Wand of Tiny Hut (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Touch of Fatigue (cr, 375 gp)", "Wand of Touch of Fatigue (cr, 375 gp) (design provides clue to function)", "Wand of Touch of Fatigue (cr, 375 gp) (inscription provides clue to function)", 
                "Wand of Touch of Idiocy (cr, 4500 gp)", "Wand of Tree Shape (cr, 4500 gp)", "Wand of Tree Shape (cr, 4500 gp) (inscription provides clue to function)", "Wand of True Strike (cr, 750 gp)", 
                "Wand of True Strike (cr, 750 gp) (design provides clue to function)", "Wand of True Strike (cr, 750 gp) (inscription provides clue to function)", "Wand of Undetectable Alignment (cr, 750 gp) (inscription provides clue to function)", 
                "Wand of Unseen Servant (cr, 750 gp)", "Wand of Urban Grace (arg, 750 gp)", "Wand of Urban Grace (arg, 750 gp) (inscription provides clue to function)", "Wand of Vampiric Touch (cr, 11250 gp)", 
                "Wand of Vampiric Touch (cr, 11250 gp) (inscription provides clue to function)", "Wand of Vanish (apg, 750 gp)", "Wand of Vanish (apg, 750 gp) (design provides clue to function)", 
                "Wand of Vanish (apg, 750 gp) (inscription provides clue to function)", "Wand of Ventriloquism (cr, 750 gp)", "Wand of Ventriloquism (cr, 750 gp) (design provides clue to function)", 
                "Wand of Virtue (cr, 375 gp) (design provides clue to function)", "Wand of Volcanic Storm (um, 21000 gp)", "Wand of Volcanic Storm (um, 21000 gp) (design provides clue to function)", 
                "Wand of Wall of Fire (cr, 21000 gp)", "Wand of Wall of Fire (cr, 21000 gp) (design provides clue to function)", "Wand of Wall of Ice (cr, 21000 gp)", "Wand of Warp Wood (cr, 4500 gp) (design provides clue to function)", 
                "Wand of Water Breathing (cr, 11250 gp)", "Wand of Water Walk (cr, 11250 gp)", "Wand of Water Walk (cr, 11250 gp) (design provides clue to function)", "Wand of Weapon of Awe (apg, 4500 gp)", 
                "Wand of Web (cr, 4500 gp)", "Wand of Web (cr, 4500 gp) (design provides clue to function)", "Wand of Web (cr, 4500 gp) (inscription provides clue to function)", "Wand of Whispering Wind (cr, 4500 gp)", 
                "Wand of Whispering Wind (cr, 4500 gp) (inscription provides clue to function)", "Wand of Wind Wall (cr, 11250 gp)", "Wand of Wind Wall (cr, 11250 gp) (design provides clue to function)", 
                "Wand of Wood Shape (cr, 4500 gp) (design provides clue to function)", "Wand of Zone of Truth (cr, 4500 gp)"]
    possibility = wand * random.randrange(1, 101, 1)
    wandContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*.222)
        elif cr < 10 :
            counter = int(cr*.333)
        elif cr < 15 :
            counter = int(cr*.444)
        else :
            counter = int(cr*.555)
        while counter > 0 :
            wandContain.append(random.randrange(0, wandList.__len__(), 1))
            counter -= (cr*15)
        for i in range(0, wandList.__len__()) :
            if wandList[i] in wandContain :
                count = wandContain.count(wandList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", wandList[i], "\n")
    details = "%s%s" % (details, "\n-Staff--------------------------------------\n")
    return details    

def Staff(cr, staff) :
    details = ""
    staffList = ["Staff of Accompaniment (14800 gp)", "Staff of Accompaniment (14800 gp) (design provides clue to function)", "Staff of Accompaniment (14800 gp) (inscription provides clue to function)", 
                    "Staff of Authority (23000 gp)", "Staff of Authority (23000 gp) (design provides clue to function)", "Staff of Authority (23000 gp) (inscription provides clue to function)", "Staff of Belittling (20000 gp)", 
                    "Staff of Belittling (20000 gp) (design provides clue to function)", "Staff of Blessed Relief (7200 gp)", "Staff of Blessed Relief (7200 gp) (inscription provides clue to function)", 
                    "Staff of Charming (17600 gp)", "Staff of Charming (17600 gp) (design provides clue to function)", "Staff of Charming (17600 gp) (inscription provides clue to function)", "Staff of Courage (19200 gp)", 
                    "Staff of Courage (19200 gp) (design provides clue to function)", "Staff of Courage (19200 gp) (inscription provides clue to function)", "Staff of Eidolons (14400 gp)", 
                    "Staff of Eidolons (14400 gp) (design provides clue to function)", "Staff of Feast and Famine (20800 gp)", "Staff of Feast and Famine (20800 gp) (design provides clue to function)", "Staff of Fire (18950 gp)", 
                    "Staff of Fire (18950 gp) (design provides clue to function)", "Staff of Fire (18950 gp) (inscription provides clue to function)", "Staff of Journeys (27200 gp)", 
                    "Staff of Journeys (27200 gp) (design provides clue to function)", "Staff of Journeys (27200 gp) (inscription provides clue to function)", "Staff of Minor Arcana (8000 gp)", 
                    "Staff of Minor Arcana (8000 gp) (design provides clue to function)", "Staff of Minor Arcana (8000 gp) (inscription provides clue to function)", "Staff of Radiance (23200 gp)", 
                    "Staff of Radiance (23200 gp) (design provides clue to function)", "Staff of Radiance (23200 gp) (inscription provides clue to function)", "Staff of Rigor (20800 gp)", 
                    "Staff of Rigor (20800 gp) (design provides clue to function)", "Staff of Rigor (20800 gp) (inscription provides clue to function)", "Staff of Size Alteration (26150 gp)", 
                    "Staff of Size Alteration (26150 gp) (inscription provides clue to function)", "Staff of Swarming Insects (22800 gp)", "Staff of Swarming Insects (22800 gp) (design provides clue to function)", 
                    "Staff of Swarming Insects (22800 gp) (inscription provides clue to function)", "Staff of the Scout (9600 gp)", "Staff of the Scout (9600 gp) (inscription provides clue to function)", 
                    "Staff of Tricks (8800 gp)", "Staff of Tricks (8800 gp) (design provides clue to function)", "Staff of Tricks (8800 gp) (inscription provides clue to function)", "Staff of Understanding (16000 gp)", 
                    "Staff of Understanding (16000 gp) (design provides clue to function)", "Staff of Understanding (16000 gp) (inscription provides clue to function)"]
    possibility = staff * random.randrange(1, 101, 1)
    staffContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*0)
        elif cr < 10 :
            counter = int(cr*.2)
        elif cr < 15 :
            counter = int(cr*.3)
        else :
            counter = int(cr*.4)
        while counter > 0 :
            staffContain.append(random.randrange(0, staffList.__len__(), 1))
            counter -= (cr*.15)
        for i in range(0, staffList.__len__()) :
            if staffList[i] in staffContain :
                count = staffContain.count(staffList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", staffList[i], "\n")
    details = "%s%s" % (details, "\n-Rods---------------------------------------\n")
    return details

def Rod(cr, rod) :
    details = ""
    rodList = ["Rod of Beguiling (18000 gp) (design provides clue to function)", "Rod of Flame Extinguishing (15000 gp) (inscription provides clue to function)", "Rod of Minor Metamagic (Echoing Spell) (14000 gp)", 
                "Rod of Minor Metamagic (Maximize Spell) (14000 gp) (design provides clue to function)", "Rod of Minor Metamagic (Widen Spell) (14000 gp) (inscription provides clue to function)", 
                "Rod of Ruin (16000 gp)", "Rod of the Python (13000 gp)", "Rod of the Viper (19000 gp)", "Rod of the Viper (19000 gp) (design provides clue to function)", 
                "Rod of the Viper (19000 gp) (inscription provides clue to function)", "Rod of the Wayang (12000 gp)", "Rod of the Wayang (12000 gp) (inscription provides clue to function)", 
                "Rod of Wonder (12000 gp)", "Sapling Rod (16650 gp)"]
    possibility = rod * random.randrange(1, 101, 1)
    rodContain = []
    if possibility > 34 :
        counter = 0
        if cr < 5 :
            counter = int(cr*0)
        elif cr < 10 :
            counter = int(cr*0)
        elif cr < 15 :
            counter = int(cr*.15)
        else :
            counter = int(cr*.25)
        while counter > 0 :
            rodContain.append(random.randrange(0, rodList.__len__(), 1))
            counter -= (cr*.08)
        for i in range(0, rodList.__len__()) :
            if rodList[i] in rodContain :
                count = rodContain.count(rodList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", rodList[i], "\n")
    details = "%s%s" % (details, "\n-ring----------------------------------------\n")
    return details    

def Ring(cr, ring) :
    details = ""
    ringList = ["Ring of Arcane Mastery (20000 gp)", "Ring of Arcane Mastery (20000 gp) (design provides clue to function)", "Ring of Arcane Mastery (20000 gp) (inscription provides clue to function)", 
                "Ring of Arcane Signets (1000 gp)", "Ring of Arcane Signets (1000 gp) (design provides clue to function)", "Ring of Arcane Signets (1000 gp) (inscription provides clue to function)", 
                "Ring of Blinking (27000 gp)", "Ring of Blinking (27000 gp) (design provides clue to function)", "Ring of Blinking (27000 gp) (inscription provides clue to function)", "Ring of Climbing (2500 gp)", 
                "Ring of Climbing (2500 gp) (design provides clue to function)", "Ring of Climbing (2500 gp) (inscription provides clue to function)", "Ring of Energy Shroud (19500 gp)", 
                "Ring of Energy Shroud (19500 gp) (inscription provides clue to function)", "Ring of Evasion (25000 gp)", "Ring of Evasion (25000 gp) (design provides clue to function)", 
                "Ring of Evasion (25000 gp) (inscription provides clue to function)", "Ring of Feather Falling (2200 gp)", "Ring of Feather Falling (2200 gp) (design provides clue to function)", 
                "Ring of Feather Falling (2200 gp) (inscription provides clue to function)", "Ring of Ferocious Action (3000 gp)", "Ring of Ferocious Action (3000 gp) (design provides clue to function)", 
                "Ring of Ferocious Action (3000 gp) (inscription provides clue to function)", "Ring of Grit Mastery (6840 gp)", "Ring of Invisibility (20000 gp)", 
                "Ring of Invisibility (20000 gp) (design provides clue to function)", "Ring of Invisibility (20000 gp) (inscription provides clue to function)", "Ring of Jumping (2500 gp)", 
                "Ring of Jumping (2500 gp) (design provides clue to function)", "Ring of Jumping (2500 gp) (inscription provides clue to function)", "Ring of Maniacal Devices (5000 gp)", 
                "Ring of Protection +1 (2000 gp)", "Ring of Protection +1 (2000 gp) (design provides clue to function)", "Ring of Protection +1 (2000 gp) (inscription provides clue to function)", 
                "Ring of Protection +3 (18000 gp)", "Ring of Protection +3 (18000 gp) (design provides clue to function)", "Ring of Protection +3 (18000 gp) (inscription provides clue to function)", 
                "Ring of Rat Fangs (5000 gp)", "Ring of Rat Fangs (5000 gp) (design provides clue to function)", "Ring of Sacred Mistletoe (6000 gp)", "Ring of Sacred Mistletoe (6000 gp) (design provides clue to function)", 
                "Ring of Spell Knowledge I (1500 gp)", "Ring of Spell Knowledge II (6000 gp)", "Ring of Spell Knowledge II (6000 gp) (design provides clue to function)", "Ring of Spell Knowledge IV (24000 gp)", 
                "Ring of Spell Knowledge IV (24000 gp) (design provides clue to function)", "Ring of Spell Knowledge IV (24000 gp) (inscription provides clue to function)", "Ring of Sustenance (2500 gp)", 
                "Ring of Sustenance (2500 gp) (design provides clue to function)", "Ring of Sustenance (2500 gp) (inscription provides clue to function)", "Ring of Swarming Stabs (6000 gp)", "Ring of Swimming (2500 gp)", 
                "Ring of Swimming (2500 gp) (design provides clue to function)", "Ring of Swimming (2500 gp) (inscription provides clue to function)", "Ring of the Grasping Grave (2000 gp)", 
                "Ring of the Grasping Grave (2000 gp) (design provides clue to function)", "Ring of Wizardry I (20000 gp)", "Ring of Wizardry I (20000 gp) (design provides clue to function)", 
                "Ring of Wizardry I (20000 gp) (inscription provides clue to function)", "Ring of X-ray Vision (25000 gp)", "Ring of X-ray Vision (25000 gp) (design provides clue to function)", 
                "Ring of X-ray Vision (25000 gp) (inscription provides clue to function)", "Minor Ring of Inner Fortitude (18000 gp)", "Minor Ring of Inner Fortitude (18000 gp) (design provides clue to function)", 
                "Minor Ring of Inner Fortitude (18000 gp) (inscription provides clue to function)", "Minor Ring of Spell Storing (18000 gp)", 
                "Minor Ring of Spell Storing (18000 gp) (design provides clue to function)", "Minor Ring of Spell Storing (18000 gp) (inscription provides clue to function)", "Prisoner's Dungeon Ring (250 gp)", 
                "Prisoner's Dungeon Ring (250 gp) (design provides clue to function)", "Prisoner's Dungeon Ring (250 gp) (inscription provides clue to function)", "Superior Ring of Revelation (24000 gp)", 
                "Superior Ring of Revelation (24000 gp) (design provides clue to function)", "Superior Ring of Revelation (24000 gp) (inscription provides clue to function)"]
    possibility = ring * random.randrange(1, 101, 1)
    ringContain = []
    if possibility > 34 :
        counter = 0
        if cr < 4 :
            counter = int(cr*0)
        elif cr < 10 :
            counter = int(cr*.2)
        elif cr < 15 :
            counter = int(cr*.3)
        else :
            counter = int(cr*.4)
        while counter > 0 :
            ringContain.append(random.randrange(0, ringList.__len__(), 1))
            counter -= (cr*.125)
        for i in range(0, ringList.__len__()) :
            if ringList[i] in ringContain :
                count = ringContain.count(ringList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", ringList[i], "\n")
    details = "%s%s" % (details, "\n-Wonderous----------------------------------\n")
    return details  

def Wonderous(cr, wonderous) :
    details = ""
    wonderousList = ["Acrobat Slippers (3000 gp)", "Acrobat Slippers (3000 gp) (design provides clue to function)", "Acrobat Slippers (3000 gp) (inscription provides clue to function)", "Agile Alpenstock (2000 gp)", 
                        "Alchemist's Bullet (330 gp) (sheds light)", "All Tools Vest (1800 gp)", "All Tools Vest (1800 gp) (design provides clue to function)", "Ampoule of False Blood (20000 gp)", 
                        "Amulet of Bullet Protection +1 (1500 gp) (design provides clue to function)", "Amulet of Natural Armor +1 (2000 gp)", "Anatomy Doll (1000 gp)", "Angelskin Leather Armor (1010 gp)", 
                        "Annihilation Spectacles (25000 gp)", "Apple of Eternal Sleep (2500 gp)", "Apprentice's Cheating Gloves (2200 gp)", "Aquatic Cummerbund (2600 gp)", 
                        "Aquatic Cummerbund (2600 gp) (design provides clue to function)", "Armbands of the Brawler (500 gp)", "Armor of Insults (16175 gp)", "Assisting Gloves (180 gp)", 
                        "Assisting Gloves (180 gp) (inscription provides clue to function)", "Avalanche Shield (19170 gp)", "Bag of Holding (type I) (2500 gp)", 
                        "Bag of Holding (type I) (2500 gp) (inscription provides clue to function)", "Bag of Holding (type IV) (10000 gp)", "Bag of Tricks (gray) (3400 gp)", 
                        "Bandages of Rapid Recovery (200 gp) (design provides clue to function)", "Bead of Force (3000 gp)", "Bead of Force (3000 gp) (design provides clue to function)", 
                        "Bead of Newt Prevention (1000 gp)", "Beast-bond Brand (1000 gp)", "Beast-bond Brand (1000 gp) (inscription provides clue to function)", 
                        "Belt of Fallen Heroes (21000 gp) (design provides clue to function)", "Belt of Giant Strength +4 (16000 gp) (inscription provides clue to function)", "Belt of Tumbling (800 gp)", 
                        "Belt of Tumbling (800 gp) (design provides clue to function)", "Beneficial Bandolier (1000 gp)", "Beneficial Bandolier (1000 gp) (design provides clue to function)", "Bladed Belt (2000 gp)", 
                        "Blind Man's Fold (12000 gp)", "Blood Reservoir of Physical Prowess (2000 gp)", "Bodywrap of Mighty Strikes +1 (3000 gp)", 
                        "Bodywrap of Mighty Strikes +1 (3000 gp) (design provides clue to function)", "Book of Extended Summoning (standard) (2750 gp)", "Bookmark of Deception (1500 gp)", 
                        "Boots of Elvenkind (2500 gp) (design provides clue to function)", "Boots of Elvenkind (2500 gp) (inscription provides clue to function)", "Boots of Friendly Terrain (2400 gp)", 
                        "Boots of Friendly Terrain (2400 gp) (inscription provides clue to function)", "Boots of the Cat (1000 gp)", "Boots of the Cat (1000 gp) (inscription provides clue to function)", 
                        "Boots of the Mastodon (10500 gp) (design provides clue to function)", "Boots of the Mire (3500 gp)", "Boots of the Winterlands (2500 gp) (inscription provides clue to function)", 
                        "Boro Bead (1st) (1000 gp)", "Boro Bead (5th) (25000 gp) (inscription provides clue to function)", "Bracers of Armor +1 (1000 gp)", 
                        "Bracers of Armor +1 (1000 gp) (design provides clue to function)", "Bracers of Armor +3 (9000 gp)", "Bracers of Steadiness (2000 gp)", 
                        "Bracers of Steadiness (2000 gp) (design provides clue to function)", "Bracers of Steadiness (2000 gp) (inscription provides clue to function)", "Brooch of Shielding (1500 gp)", 
                        "Broom of Flying (17000 gp)", "Buffering Cap (2000 gp)", "Buffering Cap (2000 gp) (inscription provides clue to function)", "Burglar's Bracers (1000 gp) (design provides clue to function)", 
                        "Candle of Truth (2500 gp)", "Cap of Human Guise (800 gp)", "Cap of Light (900 gp)", "Cap of Light (900 gp) (design provides clue to function)", "Cap of the Free Thinker (12000 gp)", 
                        "Carpet of Flying (5 ft. by 5 ft.) (20000 gp)", "Carpet of Flying (5 ft. by 5 ft.) (20000 gp) (inscription provides clue to function)", "Challenger's Gloves (2200 gp)", "Chaos Emerald (25000 gp)", 
                        "Chime of Opening (3000 gp)", "Cloak of Elvenkind (2500 gp)", "Cloak of Elvenkind (2500 gp) (design provides clue to function)", 
                        "Cloak of Elvenkind (2500 gp) (inscription provides clue to function)", "Cloak of Fangs (2800 gp)", "Cloak of Fangs (2800 gp) (design provides clue to function)", 
                        "Cloak of Fangs (2800 gp) (inscription provides clue to function)", "Cloak of Resistance +1 (1000 gp)", "Cloak of Resistance +1 (1000 gp) (design provides clue to function)", 
                        "Cloak of Resistance +1 (1000 gp) (inscription provides clue to function)", "Cloak of Resistance +4 (16000 gp)", "Cloak of Resistance +5 (25000 gp)", "Cloak of the Hedge Wizard (2500 gp)", 
                        "Concealing Pocket (1000 gp)", "Cowardly Crouching Cloak (1800 gp)", "Cowardly Crouching Cloak (1800 gp) (inscription provides clue to function)", "Darklands Goggles (20000 gp)", 
                        "Dead Man's Headband (3600 gp)", "Dead Man's Headband (3600 gp) (inscription provides clue to function)", "Deathwatch Eyes (2000 gp)", "Dowsing Syrup (1000 gp)", 
                        "Dragoncatch Guisarme (13308 gp) (sheds light)", "Drinking Horn of Bottomless Valor (24000 gp) (design provides clue to function)", "Dust of Appearance (1800 gp)", "Dust of Disappearance (3500 gp)", 
                        "Dust of Disappearance (3500 gp) (inscription provides clue to function)", "Dust of Illusion (1200 gp)", "Eel Hide (1815 gp)", "Elemental Earth Belt (24000 gp)", "Elemental Gem (earth) (2250 gp)", 
                        "Elemental Gem (fire) (2250 gp)", "Elemental Gem (water) (2250 gp)", "Elixir of Dragon Breath (1400 gp)", "Elixir of Fire Breath (1100 gp)", 
                        "Elixir of Fire Breath (1100 gp) (inscription provides clue to function)", "Endless Bandolier (1500 gp)", "Engineer's Workgloves (3000 gp)", "Equestrain Belt (3200 gp)", 
                        "Equestrain Belt (3200 gp) (inscription provides clue to function)", "Exorcist's Aspergillum (8000 gp)", "Eyes of Doom (25000 gp)", "Eyes of the Eagle (2500 gp)", 
                        "Feather Token (tree) (400 gp) (inscription provides clue to function)", "Figurine of Wondrous Power (ivory goats) (21000 gp) (design provides clue to function)", 
                        "Figurine of Wondrous Power (silver raven) (3800 gp)", "Figurine of Wondrous Power (slate spider) (10000 gp)", "Flying Ointment (2250 gp)", 
                        "Flying Ointment (2250 gp) (inscription provides clue to function)", "Gloves of Dueling (15000 gp)", "Gloves of Larceny (2500 gp)", "Gloves of Reconnaissance (2000 gp)", "Glowing Glove (2000 gp)", 
                        "Glyphbane Gloves (9000 gp)", "Goblin Fire Drum (normal) (2000 gp)", "Goblin Fire Drum (normal) (2000 gp) (inscription provides clue to function)", "Goggles of Minute Seeing (2500 gp)", 
                        "Goggles of Minute Seeing (2500 gp) (design provides clue to function)", "Goggles of Minute Seeing (2500 gp) (inscription provides clue to function)", "Goggles of Night (12000 gp)", 
                        "Golem Manual (stone) (22000 gp) (design provides clue to function)", "Golembane Scarab (2500 gp) (design provides clue to function)", "Grave Salt (1100 gp)", "Greater Bracers of Archery (25000 gp)", 
                        "Hand of the Mage (900 gp)", "Hat of Disguise (1800 gp)", "Headband of Knucklebones (27500 gp)", "Headband of Knucklebones (27500 gp) (inscription provides clue to function)", "Heavyload Belt (2000 gp)", 
                        "Helm of Fearsome Mien (5000 gp)", "Helm of Telepathy (27000 gp) (design provides clue to function)", "Horn of Blasting (20000 gp)", "Horn of Fog (2000 gp)", 
                        "Horn of Fog (2000 gp) (design provides clue to function)", "Horseshoes of Speed (3000 gp)", "Hourglass of Last Chances (10000 gp)", "Howling Helm (22600 gp) (inscription provides clue to function)", 
                        "Ioun Stone (pale lavender ellipsoid) (20000 gp)", "Ioun Stone (pale lavender ellipsoid) (20000 gp) (inscription provides clue to function)", "Ioun Stone (pink and green sphere) (8000 gp)", 
                        "Ioun Stone (pink rhomboid) (8000 gp) (inscription provides clue to function)", "Iron Spike of Safe Passage (2000 gp)", "Jellyfish Cape (19200 gp)", "Lenses of Detection (3500 gp)", 
                        "Lion Cloak (12000 gp) (design provides clue to function)", "Manacles of Cooperation (2000 gp)", "Manual of Gainful Exercise +1 (27500 gp) (design provides clue to function)", 
                        "Mask of Stony Demeanor (500 gp)", "Mask of Stony Demeanor (500 gp) (design provides clue to function)", "Maul of the Titans (25305 gp)", "Miser's Mask (3000 gp)", "Muleback Cords (1000 gp)", 
                        "Necklace of Fireballs (type I) (1650 gp) (design provides clue to function)", "Necklace of Fireballs (type VII) (8700 gp)", "Otyugh Hide (2565 gp)", "Page of Spell Knowledge (1st) (1000 gp)", 
                        "Page of Spell Knowledge (1st) (1000 gp) (design provides clue to function)", "Pauldrons of the Serpent (3000 gp) (design provides clue to function)", "Pearl of Power (1st) (1000 gp)", 
                        "Pearl of Power (1st) (1000 gp) (inscription provides clue to function)", "Pearl of the Sirines (15300 gp) (design provides clue to function)", "Periapt of Proof against Poison (27000 gp)", 
                        "Phylactery of Faithfulness (1000 gp)", "Phylactery of Faithfulness (1000 gp) (design provides clue to function)", "Phylactery of Faithfulness (1000 gp) (inscription provides clue to function)", 
                        "Pipes of Dissolution (12000 gp) (design provides clue to function)", "Pipes of Sounding (1800 gp)", "Pirate's Eye Patch (2600 gp) (inscription provides clue to function)", "Plague Mask (27000 gp)", 
                        "Plate Armor of the Deep (24650 gp)", "Preserving Flask (5th) (25000 gp)", "Pyxes of Redirected Focus (1000 gp)", "Quick Runner's Shirt (1000 gp)", 
                        "Quick Runner's Shirt (1000 gp) (inscription provides clue to function)", "Rainbow Lenses (21000 gp) (inscription provides clue to function)", "Robe of Bones (2400 gp)", 
                        "Robe of Bones (2400 gp) (design provides clue to function)", "Robe of Bones (2400 gp) (inscription provides clue to function)", "Robe of Infinite Twine (1000 gp)", 
                        "Robe of Infinite Twine (1000 gp) (design provides clue to function)", "Robe of Infinite Twine (1000 gp) (inscription provides clue to function)", "Robe of Needles (1000 gp)", 
                        "Robe of Needles (1000 gp) (inscription provides clue to function)", "Robe of Scintillating Colors (27000 gp) (design provides clue to function)", "Rope of Climbing (3000 gp)", 
                        "Rope of Climbing (3000 gp) (design provides clue to function)", "Salve of Slipperiness (1000 gp)", "Shatterspike (4315 gp)", "Shatterspike (4315 gp) (design provides clue to function)", 
                        "Shatterspike (4315 gp) (sheds light)", "Shawl of Life-keeping (1000 gp) (design provides clue to function)", "Shroud of Disintegration (3300 gp)", "Slashing Cloak (20000 gp)", 
                        "Sleeves of Many Garments (200 gp)", "Sleeves of Many Garments (200 gp) (inscription provides clue to function)", "Sniper Goggles (20000 gp)", "Spectacles of Understanding (3000 gp)", 
                        "Spellstrike Gloves (8000 gp)", "Stalker's Mask (3500 gp)", "Stalker's Mask (3500 gp) (inscription provides clue to function)", "Stole of Justice (18000 gp)", "Stone of Alarm (2700 gp)", 
                        "Stone of Alarm (2700 gp) (inscription provides clue to function)", "Summon-slave Crystal (10000 gp)", "Treasurer's Seal (10000 gp)", "Vambraces of the Genie (djinni) (18900 gp)", 
                        "Vambraces of the Genie (marid) (18900 gp) (inscription provides clue to function)", "Vampiric Gloves (18000 gp)", "Vest of Stable Mutation (20000 gp)", "Vest of Surgery (3000 gp)", 
                        "Vest of Surgery (3000 gp) (inscription provides clue to function)", "Volatile Vaporizer (2nd) (3000 gp) (design provides clue to function)", "Word Bottle (1500 gp)"]
    possibility = wonderous * random.randrange(1, 101, 1)
    wonderousContain = []
    if possibility > 34 :
        counter = 0
        if cr < 4 :
            counter = int(cr*.222)
        elif cr < 9 :
            counter = int(cr*.444)
        elif cr < 14 :
            counter = int(cr*.666)
        else :
            counter = int(cr*.888)
        while counter > 0 :
            wonderousContain.append(random.randrange(0, wonderousList.__len__(), 1))
            counter -= (cr*15)
        for i in range(0, wonderousList.__len__()) :
            if wonderousList[i] in wonderousContain :
                count = wonderousContain.count(wonderousList[i])
                if count > 0 :
                    details = "%s%s%s%s%s" % (details, count, " x ", wonderousList[i], "\n")
    details = "%s%s" % (details, "\n-Artifact-----------------------------------\n")
    return details    

def Artifact(cr, artifact) :
    details = ""
    lesserList = ["Aegis (Minor Artifact)", "Amulet of Faith (Minor Artifact)", "Argental Font (Minor Artifact)", "Automaton Core (Minor Artifact)", "Azure Pendant (Minor Artifact)", 
                    "Beacon of True Faith (Minor Artifact)", "Bell of Mercy (Minor Artifact)", "Black Iron Axe (Minor Artifact)", "Bone House (Minor Artifact)", "Book of Infinite Spells (Minor Artifact)", 
                    "Branch of Life (Minor Artifact)", "Bullroarers of Outburst (Minor Artifact)", "Crown of the Iron King (Minor Artifact)", "Crown of the Simurgh (Minor Artifact)", 
                    "Cubic Spiral (Minor Artifact)", "Cup of Forbidden Knowledge (Minor Artifact)", "Dark Grimoire (Minor Artifact)", "Deck of Harrowed Tales (Minor Artifact)", 
                    "Deck of Many Things (Minor Artifact)", "Deck of Many Things, Harrow (Minor Artifact)", "Dragon Seal (Minor Artifact)", "Dragon Slayer (Minor Artifact)", "Earth’s Eye (Minor Artifact)", 
                    "Elder Sign (Minor Artifact)", "Elemental Chain (Minor Artifact)", "Enemy of All Enemies (Minor Artifact)", "Fleshhook of Mythic Sustenance (Minor Artifact)", "Fluttered Wing (Minor Artifact)", 
                    "Fortune's Arrow (Minor Artifact)", "Glabrezu Claw (Minor Artifact)", "Greater Ring of Elemental Command (Minor Artifact)", "Hammer of Thunderbolts (Minor Artifact)", 
                    "Harp of Night's Hope (Minor Artifact)", "Helm of Governance (Minor Artifact)", "Hermetic Flask (Minor Artifact)", "Hourglass of Shadows (Minor Artifact)", "Id Portrait (Minor Artifact)", 
                    "Intergalactic Orrery (Minor Artifact)", "Ioun Stone, Amethyst Crescent (Minor Artifact)", "Ioun Stone, Jaundiced Skull (Minor Artifact)", "Ioun Stone, Radiant Blue Sphere (Minor Artifact)", 
                    "Ioun Stone, Sparkling Blue Rhomboid (Minor Artifact)", "Ioun Stone, Spindle of Perfect Knowledge (Minor Artifact)", "Ioun Stone, Vivacious Rose Prism (Minor Artifact)", 
                    "Jaundiced Skull Ioun Stone Minor Artifact", "Knucklebone of Fickle Fortune (Minor Artifact)", "Maleficus Spike (Minor Artifact)", "Mantis Blade (Minor Artifact)", 
                    "Monkey's Paw (Minor Artifact)", "Nexus Crystal (Minor Artifact)", "Pendant of the First Tears (Minor Artifact)", "Perfect Golden Lute (Minor Artifact)", "Philosopher's Stone (Minor Artifact)", 
                    "Phylactery of the Failed (Minor Artifact)", "Raven’s Head (Minor Artifact)", "Reprisal (Minor Artifact)", "Revelation Quill (Minor Artifact)", "Ring of Equilibrium (Minor Artifact)", 
                    "Rod of Spell Sundering (Minor Artifact)", "Runescarred Dragonship (Minor Artifact)", "Runeslave Cauldron (Minor Artifact)", "Runewarded Gauntlets (Minor Artifact)", 
                    "Runewell Amulet (Minor Artifact)", "Runewell, Minor (Minor Artifact)", "Screaming Spear of the Sun (Minor Artifact)", "Sihedron Tome (Minor Artifact)", "Slime Tendril (Minor Artifact)", 
                    "Spear of Shards (Minor Artifact)", "Sphere of Annihilation (Minor Artifact)", "Staff of Eldritch Sovereignty (Minor Artifact)", "Staff of the Magi (Minor Artifact)", 
                    "Storm Kindler's Rod (Minor Artifact)", "Sword of the Mists (Minor Artifact)", "Talisman of Pure Good (Minor Artifact)", "Talisman of Reluctant Wishes (Minor Artifact)", 
                    "Talisman of the Sphere (Minor Artifact)", "Talisman of Ultimate Evil (Minor Artifact)", "Tentacle of the Vaults (Minor Artifact)", "The Enthroned King (Minor Artifact)", 
                    "Torc of the Heavens (Minor Artifact)", "Unending Tome (Minor Artifact)", "Vernal Key (Minor Artifact)", "Vicious Link (Minor Artifact)", "Visionary Lens (Minor Artifact)", 
                    "Warding Box (Minor Artifact)", "Weird Queen's Magpie (Minor Artifact)", "Witherfang (Minor Artifact)"]
    majorList = ["Anathema Archive (Major Artifact)", "Anima Focus (Major Artifact)", "Apocalypse Box (Major Artifact)", "Apollyon Ring (Major Artifact)", "Aqualinth (Major Artifact)", 
                    "Armor of Skulls (Major Artifact)", "Avernus Claw (Major Artifact)", "Axe of Dread (Major Artifact)", "Axe of the Dwarvish Lords (Major Artifact)", "Barding of Pleated Light (Major Artifact)", 
                    "Blackaxe (Major Artifact)", "Bloodstones of the Valiant (Major Artifact)", "Book of the Damned (A&L; Major Artifact)", "Book of the Damned: Daemonic (Major Artifact)", 
                    "Book of the Damned: Demonic (Major Artifact)", "Bottle of the Bound (Major Artifact)", "Bound Blade (Major Artifact)", "Brazen Egg (Major Artifact)", "Briar (Major Artifact)", 
                    "Burning Glaive (Major Artifact)", "Calabash of Last Draughts (Major Artifact)", "Celestial Lens (Major Artifact)", "Chalice of Enchantment (Major Artifact)", 
                    "Chronicle of the Righteous (Major Artifact)", "Cicatrix (Major Artifact)", "Cloud Castle of the Storm King (Major Artifact)", "Codex of the Infinite Planes (Major Artifact)", 
                    "Crook and Flail of Kings (Major Artifact)", "Crown of Fangs (Major Artifact)", "Crown of Infernal Majesty (Major Artifact)", "Dancing Hut of Baba Yaga (Major Artifact)", 
                    "Demon Prince Armor (Major Artifact)", "Demonscope (Major Artifact)", "Deskari's Tooth (Major Artifact)", "Diadem of Nod (Major Artifact)", "Doom Idol (Major Artifact)", 
                    "Dreamstone (Major Artifact)", "Dryad’s Song (Corrupted) Major Artifact)", "Elven Crown (Major Artifact)", "Emperor's Mammoth (Major Artifact)", "Flame of Guidance (Major Artifact)", 
                    "Forge of the Maker (Major Artifact)", "Fork of the Forgotten One (Major Artifact)", "Frozen Heart of Cocytus (Major Artifact)", "Gem of Dreams (Major Artifact)", 
                    "Greatcube of Power (Major Artifact)", "Guardian Key (Major Artifact)", "Handflower of Genocide (Major Artifact)", "Heart of the Herald (Major Artifact)", "Heart's Bane (Major Artifact)", 
                    "Heart's Edge (Major Artifact)", "Helicyon (Major Artifact)", "Horns of Death (Major Artifact)", "Howling Horn (Major Artifact)", "Icecrown (Major Artifact)", 
                    "Idol of the Spider God (Major Artifact)", "Ihystear (Major Artifact)", "Imago Lens (Major Artifact)", "Impossible Eye (Major Artifact)", "Infensus Mucro (Major Artifact)", 
                    "Invidian Eye (Major Artifact)", "Invidious Halberd (Major Artifact)", "Invulnerable Chalice (Major Artifact)", "Jar of Dragon's Teeth (Major Artifact)", 
                    "Jawbone of the Venerable (Major Artifact)", "Legendsbane (Major Artifact)", "Lens of Dimensional Shielding (Major Artifact)", "Linnorm's Lament (Major Artifact)", 
                    "Lung Bloodstone (Major Artifact)", "Mask of the Forgotten Pharaoh (Major Artifact)", "Master's Sword (Major Artifact)", "Mirror of Fascination (Major Artifact)", 
                    "Moaning Diamond (Major Artifact)", "Mother Deck (Major Artifact)", "Netherworld Cauldron (Major Artifact)", "Nimbus of Radiant Truth (Major Artifact)", "Orbs of Dragonkind (Major Artifact)", 
                    "Pauper's Thighbone (Major Artifact)", "Pazuzu’s Scepter (Major Artifact)", "Perfection's Key (Major Artifact)", "Plaguebringer (Major Artifact)", "Primogen Crown Major Artifact", 
                    "Radiance (Major Artifact)", "Ravenous Blade (Major Artifact)", "Riftcarver (Major Artifact)", "Ring of Nine Facets (Major Artifact)", "Robe of the Rifts (Major Artifact)", 
                    "Rune Shield (Major Artifact)", "Runewell of Greed (Major Artifact)", "Saint Cuthbert's Mace", "Sarcophagus of Rebirth (Major Artifact)", "Scepter of Ages (Major Artifact)", 
                    "Scepter of Magical Might (Major Artifact)", "Scepter of the Shining Lord (Major Artifact)", "Scroll of the Planes (Major Artifact)", "Shadowstaff", "Shadowwraith Heart (Major Artifact)", 
                    "Shard of Envy (Major Artifact)", "Shard of Gluttony (Major Artifact)", "Shard of Greed (Major Artifact)", "Shard of Lust (Major Artifact)", "Shard of Pride (Major Artifact)", 
                    "Shard of Sloth (Major Artifact)", "Shard of Wrath (Major Artifact)", "Shield of the Sun", "Shield of the Winged Eye", "Shredskin (Major Artifact)", "Shroud of Flies (Major Artifact)", 
                    "Sihedron (Major Artifact)", "Silver Maiden (Major Artifact)", "Skull of the Viper God", "Skullsoul", "Song of Extinction (Music Box)", "Soulforge (Major Artifact)", 
                    "Spherical Boat (Major Artifact)", "Staff of Changes (Major Artifact)", "Staff of Elemental Castigation (Major Artifact)", "Staff of the Slain (Major Artifact)", 
                    "Stole of the Inheritor (Major Artifact)", "Stormblade (Major Artifact)", "Sword of Envy (Major Artifact)", "Sword of Gluttony (Major Artifact)", "Sword of Greed", 
                    "Sword of Lust (Major Artifact)", "Sword of Pride (Major Artifact)", "Sword of Sloth (Major Artifact)", "Sword of Valor (Major Artifact)", "Sword of Wrath (Major Artifact)", 
                    "Synchrony Device (Major Artifact)", "Tarnhelm (Major Artifact)", "Tathlum (Major Artifact)", "The Briar Blade", "The Gasping Pearl (Major Artifact)", "The Jewel of Everlasting Gold", 
                    "Thorncrown of Blasting", "Throne of Command (Major Artifact)", "Trueforge (Major Artifact)", "Was Scepter (Major Artifact)", "Winter Collector (Major Artifact)"]
    possibility = artifact * random.randrange(1, 101, 1)
    if possibility > 95 and possibility < 99 :
        details = "%s%s" % (details, lesserList[random.randrange(0, lesserList.__len__(), 1)])
    if possibility > 98 :
        details = "%s%s" % (details, majorList[random.randrange(0, majorList.__len__(), 1)])
    details = "%s%s" % (details, "\n-Cursed-------------------------------------\n")
    return details    

def Cursed(cr, cursed) :
    details = ""
    cursedList = ["Incense of obsession", "Ring of clumsiness", "Amulet of inescapable location", "Stone of weight", "Bracers of defenselessness", "Gauntlets of fumbling", "sword, cursed", "Armor of rage", 
                    "Medallion of thought projection", "Flask of curses", "Dust of sneezing and choking", "Helm of opposite alignment", "Potion of poison", "Broom of animated attack", "Robe of powerlessness", 
                    "Vacuous grimoire", "Spear, cursed backbiter", "Armor of arrow attraction", "Net of snaring", "Bag of devouring", "Mace of blood", "Robe of vermin", "Periapt of foul rotting", 
                    "Sword, berserking", "Boots of dancing", "Crystal hypnosis ball", "Necklace of strangulation", "Poisonous cloak", "Scarab of death"]
    possibility = cursed * random.randrange(1, 101, 1)
    if possibility > 89 :
        details = "%s%s" % (details, cursedList[random.randrange(0, cursedList.__len__(), 1)])
    details = "%s%s" % (details, "\n-Intelligent--------------------------------\n")
    return details    

def Intelligent(cr, intelligent) :
    details = ""
    intemIntellList = [["10", "0", "0"], ["11", "+200 gp", "0"], ["12", "+500 gp", "+1"], ["13", "+700 gp", "+1"], ["14", "+1,000 gp", "+2"], ["15", "+1,400 gp", "+2"], ["16", "+2,000 gp", "+3"], 
                        ["17", "+2,800 gp", "+3"], ["18", "+4,000 gp", "+4"], ["19", "+5,200 gp", "+4"], ["20", "+8,000 gp", "+5"]]
    alignmentList = ["Chaotic good", "Chaotic neutral*", "Chaotic evil", "Neutral evil*", "Lawful evil", "Lawful good", "Lawful neutral*", "Neutral good*", "Neutral"]
    sensesList = [["Empathy", "0", "0"], ["Speech", "+500 gp", "0"], ["Telepathy", "+1,000 gp", "+1"], ["Senses (30 ft.)", "0", "0"], ["Senses (60 ft.)", "+500 gp", "0"], 
                    ["Senses (120 ft.)", "+1,000 gp", "0"], ["Darkvision", "+500 gp", "0"], ["Blindsense", "+5,000 gp", "+1"], ["Read languages", "+1,000 gp", "+1"], ["Read magic", "+2,000 gp", "+1"]]
    powersList = [["Item can cast a 0-level spell at will", "+1,000 gp", "+1"], ["Item can cast a 1st-level spell 3/day", "+1,200 gp", "+1"], ["Item can use magic aura on itself at will", "+2,000 gp", "+1"], 
                    ["Item can cast a 2nd-level spell 1/day", "+2,400 gp", "+1"], ["Item has 5 ranks in one skill*", "+2,500 gp", "+1"], 
                    ["Item can sprout limbs and move with a speed of 10 feet", "+5,000 gp", "+1"], ["Item can cast a 3rd-level spell 1/day", "+6,000 gp", "+1"], 
                    ["Item can cast a 2nd-level spell 3/day", "+7,200 gp", "+1"], ["Item has 10 ranks in one skill*", "+10,000 gp", "+2"], 
                    ["Item can change shape into one other form of the same size", "+10,000 gp", "+2"], ["Item can fly, as per the spell, at a speed of 30 feet", "+10,000 gp", "+2"], 
                    ["Item can cast a 4th-level spell 1/day", "+11,200 gp", "+2"], ["Item can teleport itself 1/day", "+15,000 gp", "+2"], ["Item can cast a 3rd-level spell 3/day", "+18,000 gp", "+2"], 
                    ["Item can cast a 4th-level spell 3/day", "+33,600 gp", "+2"]]
    purposeList = [["Defeat/slay diametrically opposed alignment*", "+2"], ["Defeat/slay arcane spellcasters (including spellcasting monsters and those that use spell-like abilities)", "+2"], 
                    ["Defeat/slay divine spellcasters (including divine entities and servitors)", "+2"], ["Defeat/slay non-spellcasters", "+2"], 
                    ["Defeat/slay a particular creature type (see the bane special ability for choices)", "+2"], ["Defeat/slay a particular race or kind of creature", "+2"], 
                    ["Defend a particular race or kind of creature", "+2"], ["Defeat/slay the servants of a specific deity", "+2"], ["Defend the servants and interests of a specific deity", "+2"], 
                    ["Defeat/slay all (other than the item and the wielder)", "2"], ["Choose one", "2"]]
    dedPowersList = [["Item can detect any special purpose foes within 60 feet", "+10,000 gp", "+1"], ["Item can use a 4th-level spell at will", "+56,000 gp", "+2"], 
                        ["Wielder gets +2 luck bonus on attacks, saves, and checks", "+80,000 gp", "+2"], ["Item can use a 5th-level spell at will", "+90,000 gp", "+2"], 
                        ["Item can use a 6th-level spell at will", "+132,000 gp", "+2"], ["Item can use a 7th-level spell at will", "+182,000 gp", "+2"], 
                        ["Item can use true resurrection on wielder, once per month", "+200,000 gp", "+2"]]
    baseEgoModList = [["Up to 1,000 gp", "0"], ["1,001 gp to 5,000 gp", "+1"], ["5,001 gp to 10,000 gp", "+2"], ["10,001 gp to 20,000 gp", "+3"], ["20,001 gp to 50,000 gp", "+4"], ["50,001 gp to 100,000 gp", "+6"], 
                        ["100,001 gp to 200,000 gp", "+8"], ["200,001 gp and higher", "+12"]]
    intMagicEquipList = ["Adamantine Battleaxe (3010 gp)", "Adamantine Battleaxe (3010 gp) (inscription provides clue to function)", "Adamantine Battleaxe (3010 gp) (sheds light)", "Adamantine Breastplate (10200 gp)", 
                            "Adamantine Dagger (3002 gp)", "Adamantine Dagger (3002 gp) (sheds light)", "Adamantine Scale Mail (10050 gp)", "Banded Mail (+1 armor) (1400 gp)", 
                            "Banded Mail (+1 armor, Benevolent) (3400 gp)", "Banded Mail (+1 armor, Fortification (light)) (4400 gp)", "Banded Mail (+1 armor, Ghost Touch) (16400 gp)", 
                            "Banded Mail (+1 armor, Mirrored) (4400 gp)", "Banded Mail (+1 armor, Putrid) (11400 gp)", "Banded Mail (+1 armor, Shadow) (5150 gp)", "Banded Mail (+1 armor, Spell Storing) (4400 gp)", 
                            "Banded Mail (+2 armor) (4400 gp)", "Banded Mail (+2 armor, Spell Resistance (13)) (16400 gp)", "Banded Mail (+3 armor) (9400 gp)", "Banded Mail (+4 armor, Defiant) (25400 gp)", 
                            "Banded Mail (+4 armor, Poison-resistant) (18650 gp)", "Banded Mail of Luck (18900 gp)", "Bastard Sword (+1 weapon) (sheds light) (2335 gp)", "Bastard Sword (+1 weapon, Ki Focus) (8335 gp)", 
                            "Battleaxe (+1 weapon) (2310 gp)", "Battleaxe (+1 weapon) (sheds light) (2310 gp)", "Battleaxe (+2 weapon) (8310 gp)", "Battleaxe (+2 weapon) (sheds light) (8310 gp)", 
                            "Battlement Shield (16180 gp)", "Bolas (+1 weapon) (2305 gp)", "Bolas (+1 weapon) (design provides clue to function) (2305 gp)", 
                            "Bolas (+1 weapon) (inscription provides clue to function) (2305 gp)", "Bolas (+1 weapon) (sheds light) (2305 gp)", "Bolas (+1 weapon, Thundering) (8305 gp)", "Bolas (+2 weapon) (8305 gp)", 
                            "Bolas (+2 weapon) (sheds light) (8305 gp)", "Breastplate (+1 armor) (1350 gp)", "Breastplate (+1 armor, Expeditious) (5350 gp)", "Breastplate (+1 armor, Grinding) (4350 gp)", 
                            "Breastplate (+1 armor, Impervious) (4350 gp)", "Breastplate (+1 armor, Warding) (4350 gp)", "Breastplate (+2 armor) (4350 gp)", "Breastplate (+4 armor, Bolstering) (25350 gp)", 
                            "Breastplate (+4 armor, Warding) (25350 gp)", "Buccaneer's Breastplate (23850 gp)", "Buckler (+1 shield) (1155 gp)", "Buckler (+1 shield, Arrow Catching) (4155 gp)", 
                            "Buckler (+1 shield, Defiant) (4155 gp)", "Buckler (+1 shield, Grinding) (4155 gp)", "Buckler (+1 shield, Mirrored) (4155 gp)", "Buckler (+2 shield) (4155 gp)", 
                            "Buckler (+2 shield, Rallying) (9155 gp)", "Buckler (+3 shield, Bashing) (16155 gp)", "Buckler (+3 shield, Clangorous) (16155 gp)", "Buckler (+4 shield) (16155 gp)", 
                            "Burglar's Buckler (4655 gp)", "Caster's Shield (3153 gp)", "Celestial Armor (22400 gp)", "Chain Shirt (+1 armor) (1250 gp)", "Chain Shirt (+1 armor, Bitter) (4250 gp)", 
                            "Chain Shirt (+1 armor, Brawling) (4250 gp)", "Chain Shirt (+1 armor, Fortification (moderate)) (16250 gp)", "Chain Shirt (+1 armor, Ghost Touch) (16250 gp)", 
                            "Chain Shirt (+1 armor, Grinding) (4250 gp)", "Chain Shirt (+1 armor, Mirrored) (4250 gp)", "Chain Shirt (+1 armor, Radiant) (8750 gp)", "Chain Shirt (+2 armor) (4250 gp)", 
                            "Chain Shirt (+3 armor) (9250 gp)", "Chain Shirt (+3 armor, Dastard) (16250 gp)", "Chain Shirt (+4 armor) (16250 gp)", "Chainmail (+1 armor) (1300 gp)", 
                            "Chainmail (+1 armor, Bitter) (4300 gp)", "Chainmail (+1 armor, Dastard) (4300 gp)", "Chainmail (+1 armor, Deathless) (4300 gp)", "Chainmail (+1 armor, Fortification (light)) (4300 gp)", 
                            "Chainmail (+1 armor, Stanching) (4300 gp)", "Chainmail (+2 armor) (4300 gp)", "Chainmail (+2 armor, Glamered) (7000 gp)", "Chainmail (+3 armor, Mirrored) (16300 gp)", 
                            "Chainmail (+3 armor, Stanching) (16300 gp)", "Chainmail (+4 armor, Benevolent) (18300 gp)", "Club (+1 weapon) (2300 gp)", "Club (+1 weapon) (design provides clue to function) (2300 gp)", 
                            "Club (+1 weapon) (inscription provides clue to function) (2300 gp)", "Club (+1 weapon) (sheds light) (2300 gp)", "Club (+1 weapon, Corrosive) (sheds light) (8300 gp)", 
                            "Club (+1 weapon, Frost) (8300 gp)", "Club (+1 weapon, Seaborne) (8300 gp)", "Club (+1 weapon, Valiant) (inscription provides clue to function) (8300 gp)", 
                            "Club (+1 weapon, Valiant) (sheds light) (8300 gp)", "Club (+2 weapon) (8300 gp)", "Cold Iron Masterwork Longsword (330 gp)", 
                            "Cold Iron Masterwork Longsword (330 gp) (design provides clue to function)", "Cold Iron Masterwork Longsword (330 gp) (sheds light)", 
                            "Composite Longbow (+1 Str bonus) (+1 weapon) (2500 gp)", "Composite Longbow (+1 Str bonus) (+1 weapon) (inscription provides clue to function) (2500 gp)", 
                            "Composite Longbow (+1 Str bonus) (+1 weapon, Shock) (sheds light) (8500 gp)", "Composite Longbow (+1 weapon) (2400 gp)", "Composite Longbow (+2 Str bonus) (+1 weapon) (2600 gp)", 
                            "Composite Longbow (+2 Str bonus) (+2 weapon) (8600 gp)", "Composite Longbow (+2 weapon) (sheds light) (8400 gp)", "Composite Longbow (+3 Str bonus) (+2 weapon) (8700 gp)", 
                            "Composite Longbow (+4 Str bonus) (+1 weapon) (2800 gp)", "Composite Longbow (+4 Str bonus) (+1 weapon) (sheds light) (2800 gp)", "Composite Shortbow (+1 Str bonus) (+1 weapon) (2450 gp)", 
                            "Composite Shortbow (+1 Str bonus) (+1 weapon) (sheds light) (2450 gp)", "Composite Shortbow (+1 Str bonus) (+1 weapon, Thundering) (8450 gp)", 
                            "Composite Shortbow (+1 Str bonus) (+2 weapon, Bane) (design provides clue to function) (18450 gp)", "Composite Shortbow (+1 weapon) (2375 gp)", 
                            "Composite Shortbow (+1 weapon) (inscription provides clue to function) (2375 gp)", "Composite Shortbow (+1 weapon) (sheds light) (2375 gp)", 
                            "Composite Shortbow (+2 Str bonus) (+1 weapon) (2525 gp)", "Composite Shortbow (+2 Str bonus) (+1 weapon) (sheds light) (2525 gp)", 
                            "Composite Shortbow (+2 Str bonus) (+1 weapon, Seeking) (8525 gp)", "Composite Shortbow (+2 weapon) (sheds light) (8375 gp)", 
                            "Composite Shortbow (+3 weapon) (inscription provides clue to function) (18375 gp)", "Dagger (+1 weapon) (2302 gp)", "Dagger (+1 weapon) (design provides clue to function) (2302 gp)", 
                            "Dagger (+1 weapon) (sheds light) (2302 gp)", "Dagger (+1 weapon, Ominous) (8302 gp)", "Dagger (+1 weapon, Thundering) (design provides clue to function) (8302 gp)", 
                            "Dagger (+1 weapon, Vicious) (8302 gp)", "Dagger (+2 weapon, Unholy) (32302 gp)", "Dagger (+3 weapon, Frost) (32302 gp)", "Dagger (+3 weapon, Jurist) (32302 gp)", 
                            "Darkleaf Studded Leather Armor (775 gp)", "Darkwood Buckler (203 gp)", "Darkwood Shield (257 gp)", "Dart (+1 weapon) (2300 gp 5 sp)", 
                            "Dart (+1 weapon) (inscription provides clue to function) (2300 gp 5 sp)", "Dart (+1 weapon) (sheds light) (2300 gp 5 sp)", "Dart (+2 weapon) (8300 gp 5 sp)", 
                            "Dart (+2 weapon) (sheds light) (8300 gp 5 sp)", "Disarming Blade (17820 gp)", "Disarming Blade (17820 gp) (sheds light)", "Dragonhide Half-plate (silver dragon) (1500 gp)", 
                            "Dragonhide Plate (3300 gp)", "Dust Bolt (1730 gp)", "Dust Bolt (1730 gp) (design provides clue to function)", "Dust Bolt (1730 gp) (sheds light)", "Dustburst Bullet (196 gp)", 
                            "Dwarven Plate (16500 gp)", "Dwarven Waraxe (+1 weapon) (2330 gp)", "Dwarven Waraxe (+1 weapon) (sheds light) (2330 gp)", "Dwarven Waraxe (+1 weapon, Defending) (8330 gp)", 
                            "Dwarven Waraxe (+2 weapon) (8330 gp)", "Dwarven Waraxe (+2 weapon, Flaming Burst) (32330 gp)", "Dwarven Waraxe (+3 weapon) (18330 gp)", "Eel Hide Leather Armor (1210 gp)", 
                            "Elysian Bronze Full Plate (4500 gp)", "Elysian Bronze Splint Mail (3200 gp)", "Falchion (+1 weapon) (2375 gp)", "Falchion (+1 weapon, Keen) (8375 gp)", "Falchion (+2 weapon) (8375 gp)", 
                            "Falchion (+2 weapon) (sheds light) (8375 gp)", "Fire-forged Steel Half-plate (3600 gp)", "Fortress Shield (19180 gp)", "Frost-forged Steel Full Plate (4500 gp)", 
                            "Frost-forged Steel Scale Mail (2550 gp)", "Full Plate (+1 armor) (2650 gp)", "Full Plate (+1 armor, Bitter) (5650 gp)", "Full Plate (+1 armor, Brawling) (5650 gp)", 
                            "Full Plate (+1 armor, Fortification (moderate)) (17650 gp)", "Full Plate (+1 armor, Mirrored) (5650 gp)", "Full Plate (+1 armor, Poison-resistant) (4900 gp)", 
                            "Full Plate (+2 armor) (5650 gp)", "Full Plate (+3 armor) (10650 gp)", "Full Plate (+3 armor, Poison-resistant) (12900 gp)", "Full Plate (+4 armor) (17650 gp)", 
                            "Full Plate (+4 armor, Champion) (26650 gp)", "Gauntlet (+1 weapon) (2302 gp)", "Gauntlet (+1 weapon) (design provides clue to function) (2302 gp)", 
                            "Gauntlet (+1 weapon) (sheds light) (2302 gp)", "Gauntlet (+1 weapon, Bane (humanoids, human)) (sheds light) (8302 gp)", "Gauntlet (+2 weapon) (sheds light) (8302 gp)", 
                            "Gauntlet (+2 weapon, Shock) (18302 gp)", "Glaive (+1 weapon) (2308 gp)", "Glaive (+2 weapon) (8308 gp)", "Glaive (+2 weapon, Icy Burst) (32308 gp)", "Greataxe (+1 weapon) (2320 gp)", 
                            "Greataxe (+1 weapon) (inscription provides clue to function) (2320 gp)", "Greataxe (+1 weapon) (sheds light) (2320 gp)", "Greataxe (+1 weapon, Bane (animals)) (8320 gp)", 
                            "Greataxe (+1 weapon, Cunning) (sheds light) (8320 gp)", "Greataxe (+1 weapon, Glamered) (6320 gp)", "Greataxe (+1 weapon, Spell Storing) (design provides clue to function) (8320 gp)", 
                            "Greataxe (+2 weapon) (8320 gp)", "Greataxe (+2 weapon) (sheds light) (8320 gp)", "Greataxe (+2 weapon, Ki Focus) (18320 gp)", "Greatclub (+1 weapon) (2305 gp)", 
                            "Greatclub (+1 weapon) (design provides clue to function) (2305 gp)", "Greatclub (+1 weapon) (sheds light) (2305 gp)", "Greatclub (+1 weapon, Bane (undead)) (8305 gp)", 
                            "Greatclub (+1 weapon, Flaming) (8305 gp)", "Greatclub (+2 weapon) (8305 gp)", "Greatclub (+3 weapon, Frost) (32305 gp)", "Greater Burrowing Bullet (3447 gp)", 
                            "Greater Burrowing Bullet (3447 gp) (design provides clue to function)", "Greater Burrowing Bullet (3447 gp) (inscription provides clue to function)", 
                            "Greater Burrowing Bullet (3447 gp) (sheds light)", "Greater Hushing Arrow (1047 gp)", "Greater Hushing Arrow (1047 gp) (inscription provides clue to function)", 
                            "Greater Hushing Arrow (1047 gp) (sheds light)", "Greater Slaying Arrow (aberrations) (4057 gp)", "Greater Slaying Arrow (constructs) (4057 gp) (inscription provides clue to function)", 
                            "Greater Slaying Arrow (fey) (4057 gp)", "Greater Slaying Arrow (humanoids, giants) (4057 gp)", "Greater Slaying Arrow (humanoids, giants) (4057 gp) (inscription provides clue to function)", 
                            "Greater Slaying Arrow (humanoids, human) (4057 gp) (sheds light)", "Greater Slaying Arrow (humanoids, orc) (4057 gp)", "Greater Slaying Arrow (humanoids, reptilian) (4057 gp)", 
                            "Greater Slaying Arrow (magical beasts) (4057 gp) (inscription provides clue to function)", "Greater Slaying Arrow (monstrous humanoids) (4057 gp)", 
                            "Greater Slaying Arrow (outsiders, earth) (4057 gp) (inscription provides clue to function)", "Greater Slaying Arrow (outsiders, lawful) (4057 gp)", "Greatsword (+1 weapon) (2350 gp)", 
                            "Greatsword (+1 weapon) (design provides clue to function) (2350 gp)", "Greatsword (+1 weapon) (inscription provides clue to function) (2350 gp)", 
                            "Greatsword (+1 weapon) (sheds light) (2350 gp)", "Greatsword (+1 weapon, Furious) (8350 gp)", "Greatsword (+1 weapon, Glamered) (6350 gp)", 
                            "Greatsword (+1 weapon, Mighty Cleaving) (8350 gp)", "Greatsword (+1 weapon, Shock) (8350 gp)", "Greatsword (+2 weapon) (8350 gp)", 
                            "Greatsword (+2 weapon) (design provides clue to function) (8350 gp)", "Halberd (+1 weapon) (2310 gp)", "Halberd (+1 weapon) (sheds light) (2310 gp)", "Half-plate (+1 armor) (1750 gp)", 
                            "Half-plate (+1 armor, Balanced) (4750 gp)", "Half-plate (+1 armor, Brawling) (4750 gp)", "Half-plate (+1 armor, Defiant) (4750 gp)", "Half-plate (+1 armor, Glamered) (4450 gp)", 
                            "Half-plate (+1 armor, Titanic) (16750 gp)", "Half-plate (+2 armor) (4750 gp)", "Half-plate (+4 armor, Benevolent) (18750 gp)", "Handaxe (+1 weapon) (2306 gp)", 
                            "Handaxe (+1 weapon) (sheds light) (2306 gp)", "Handaxe (+2 weapon) (8306 gp)", "Heavy Crossbow (+1 weapon) (2350 gp)", "Heavy Crossbow (+1 weapon) (sheds light) (2350 gp)", 
                            "Heavy Crossbow (+1 weapon, Holy) (sheds light) (18350 gp)", "Heavy Crossbow (+2 weapon) (sheds light) (8350 gp)", "Heavy Flail (+1 weapon) (sheds light) (2315 gp)", 
                            "Heavy Mace (+1 weapon) (2312 gp)", "Heavy Mace (+1 weapon) (design provides clue to function) (2312 gp)", "Heavy Mace (+1 weapon) (inscription provides clue to function) (2312 gp)", 
                            "Heavy Mace (+1 weapon) (sheds light) (2312 gp)", "Heavy Mace (+2 weapon) (sheds light) (8312 gp)", "Heavy Steel Shield (+1 shield) (1170 gp)", 
                            "Heavy Steel Shield (+1 shield, Animated) (9170 gp)", "Heavy Steel Shield (+1 shield, Bashing) (4170 gp)", "Heavy Steel Shield (+1 shield, Blinding) (4170 gp)", 
                            "Heavy Steel Shield (+1 shield, Clangorous) (4170 gp)", "Heavy Steel Shield (+1 shield, Grinding) (4170 gp)", "Heavy Steel Shield (+1 shield, Impervious) (4170 gp)", 
                            "Heavy Steel Shield (+1 shield, Radiant) (8670 gp)", "Heavy Steel Shield (+1 shield, Ramming) (4170 gp)", "Heavy Steel Shield (+1 shield, Wild) (16170 gp)", 
                            "Heavy Steel Shield (+2 shield) (4170 gp)", "Heavy Steel Shield (+2 shield, Spell Resistance (13)) (16170 gp)", "Heavy Steel Shield (+3 shield) (9170 gp)", 
                            "Heavy Steel Shield (+4 shield, Poison-resistant) (18420 gp)", "Heavy Wooden Shield (+1 shield) (1157 gp)", "Heavy Wooden Shield (+1 shield, Arrow Catching) (4157 gp)", 
                            "Heavy Wooden Shield (+1 shield, Defiant) (4157 gp)", "Heavy Wooden Shield (+1 shield, Fortification (light)) (4157 gp)", "Heavy Wooden Shield (+1 shield, Merging) (9157 gp)", 
                            "Heavy Wooden Shield (+1 shield, Ramming) (4157 gp)", "Heavy Wooden Shield (+1 shield, Spell Resistance (15)) (16157 gp)", "Heavy Wooden Shield (+2 shield) (4157 gp)", 
                            "Heavy Wooden Shield (+4 shield, Impervious) (25157 gp)", "Hide (+1 armor) (1165 gp)", "Hide (+1 armor, Bitter) (4165 gp)", "Hide (+1 armor, Dastard) (4165 gp)", 
                            "Hide (+1 armor, Grinding) (4165 gp)", "Hide (+1 armor, Rallying) (6165 gp)", "Hide (+2 armor) (4165 gp)", "Hide (+2 armor, Creeping) (9165 gp)", "Hide (+3 armor) (9165 gp)", 
                            "Hushing Arrow (547 gp)", "Hushing Arrow (547 gp) (sheds light)", "Javelin of Lightning (1500 gp)", "Javelin of Lightning (1500 gp) (inscription provides clue to function)", 
                            "Lance (+1 weapon) (2310 gp)", "Lance (+1 weapon) (design provides clue to function) (2310 gp)", "Lance (+1 weapon) (inscription provides clue to function) (2310 gp)", 
                            "Lance (+1 weapon) (sheds light) (2310 gp)", "Lance (+1 weapon, Ki Focus) (inscription provides clue to function) (8310 gp)", "Lance (+1 weapon, Throwing) (8310 gp)", 
                            "Lance (+2 weapon) (inscription provides clue to function) (8310 gp)", "Lance of Jousting (4310 gp)", "Lance of Jousting (4310 gp) (design provides clue to function)", 
                            "Lance of Jousting (4310 gp) (sheds light)", "Lash of the Howler (18305 gp)", "Leather Armor (+1 armor) (1160 gp)", "Leather Armor (+1 armor, Bolstering) (4160 gp)", 
                            "Leather Armor (+1 armor, Brawling) (4160 gp)", "Leather Armor (+1 armor, Dastard) (4160 gp)", "Leather Armor (+1 armor, Poison-resistant) (3410 gp)", 
                            "Leather Armor (+1 armor, Spell Resistance (15)) (16160 gp)", "Leather Armor (+1 armor, Warding) (4160 gp)", "Leather Armor (+2 armor) (4160 gp)", 
                            "Leather Armor (+2 armor, Slick) (7910 gp)", "Leather Armor (+3 armor) (9160 gp)", "Leather Armor (+3 armor, Balanced) (16160 gp)", "Leather Armor (+4 armor) (16160 gp)", 
                            "Leather Armor (+4 armor, Bolstering) (25160 gp)", "Leather Armor (+4 armor, Defiant) (25160 gp)", "Light Crossbow (+1 weapon) (2335 gp)", 
                            "Light Crossbow (+1 weapon) (inscription provides clue to function) (2335 gp)", "Light Crossbow (+1 weapon) (sheds light) (2335 gp)", "Light Crossbow (+1 weapon, Distance) (8335 gp)", 
                            "Light Crossbow (+2 weapon, Distance) (sheds light) (18335 gp)", "Light Flail (+1 weapon) (design provides clue to function) (2308 gp)", 
                            "Light Flail (+1 weapon) (inscription provides clue to function) (2308 gp)", "Light Flail (+1 weapon) (sheds light) (2308 gp)", "Light Flail (+2 weapon) (8308 gp)", 
                            "Light Flail (+2 weapon) (inscription provides clue to function) (8308 gp)", "Light Hammer (+1 weapon) (2301 gp)", "Light Hammer (+1 weapon) (sheds light) (2301 gp)", 
                            "Light Mace (+1 weapon) (2305 gp)", "Light Mace (+1 weapon) (design provides clue to function) (2305 gp)", "Light Mace (+1 weapon) (inscription provides clue to function) (2305 gp)", 
                            "Light Mace (+1 weapon) (sheds light) (2305 gp)", "Light Mace (+1 weapon, Ominous) (8305 gp)", "Light Mace (+1 weapon, Valiant) (sheds light) (8305 gp)", 
                            "Light Mace (+1 weapon, Wounding) (18305 gp)", "Light Mace (+2 weapon) (design provides clue to function) (8305 gp)", "Light Pick (+1 weapon) (2304 gp)", 
                            "Light Pick (+1 weapon) (inscription provides clue to function) (2304 gp)", "Light Pick (+1 weapon) (sheds light) (2304 gp)", "Light Steel Shield (+1 shield) (1159 gp)", 
                            "Light Steel Shield (+1 shield, Animated) (9159 gp)", "Light Steel Shield (+1 shield, Arrow Catching) (4159 gp)", "Light Steel Shield (+1 shield, Fortification (light)) (4159 gp)", 
                            "Light Steel Shield (+1 shield, Poison-resistant) (3409 gp)", "Light Steel Shield (+1 shield, Ramming) (4159 gp)", "Light Steel Shield (+2 shield) (4159 gp)", 
                            "Light Steel Shield (+2 shield, Merging) (16159 gp)", "Light Steel Shield (+2 shield, Rallying) (9159 gp)", "Light Steel Shield (+2 shield, Spell Resistance (13)) (16159 gp)", 
                            "Light Steel Shield (+3 shield) (9159 gp)", "Light Steel Shield (+3 shield, Defiant) (16159 gp)", "Light Steel Shield (+3 shield, Impervious) (16159 gp)", 
                            "Light Steel Shield (+4 shield) (16159 gp)", "Light Steel Shield (+4 shield, Arrow Catching) (25159 gp)", "Light Steel Shield (+4 shield, Ramming) (25159 gp)", 
                            "Light Wooden Shield (+1 shield) (1153 gp)", "Light Wooden Shield (+1 shield, Animated) (9153 gp)", "Light Wooden Shield (+1 shield, Fortification (moderate)) (16153 gp)", 
                            "Light Wooden Shield (+1 shield, Impervious) (4153 gp)", "Light Wooden Shield (+1 shield, Spell Resistance (13)) (9153 gp)", "Light Wooden Shield (+2 shield) (4153 gp)", 
                            "Light Wooden Shield (+2 shield, Spell Resistance (13)) (16153 gp)", "Light Wooden Shield (+3 shield) (9153 gp)", "Light Wooden Shield (+3 shield, Grinding) (16153 gp)", 
                            "Light Wooden Shield (+3 shield, Mirrored) (16153 gp)", "Light Wooden Shield (+4 shield) (16153 gp)", "Living Steel Banded Mail (1750 gp)", "Living Steel Breastplate (1200 gp)", 
                            "Living Steel Heavy Shield (120 gp)", "Longbow (+1 weapon) (2375 gp)", "Longbow (+1 weapon) (design provides clue to function) (2375 gp)", "Longbow (+1 weapon) (sheds light) (2375 gp)", 
                            "Longbow (+1 weapon, Bane) (sheds light) (8375 gp)", "Longbow (+1 weapon, Corrosive) (8375 gp)", "Longbow (+2 weapon) (8375 gp)", 
                            "Longbow (+2 weapon) (design provides clue to function) (8375 gp)", "Longbow (+2 weapon) (inscription provides clue to function) (8375 gp)", "Longbow (+2 weapon) (sheds light) (8375 gp)", 
                            "Longbow (+3 weapon) (18375 gp)", "Longbow (+3 weapon, Jurist) (sheds light) (32375 gp)", "Longspear (+1 weapon) (2305 gp)", 
                            "Longspear (+1 weapon) (design provides clue to function) (2305 gp)", "Longspear (+1 weapon) (inscription provides clue to function) (2305 gp)", 
                            "Longspear (+1 weapon) (sheds light) (2305 gp)", "Longspear (+1 weapon, Conductive) (sheds light) (8305 gp)", "Longspear (+1 weapon, Flaming) (8305 gp)", 
                            "Longspear (+1 weapon, Mighty Cleaving) (8305 gp)", "Longspear (+1 weapon, Neutralizing) (8305 gp)", "Longspear (+2 weapon, Quenching) (sheds light) (18305 gp)", 
                            "Longsword (+1 weapon) (2315 gp)", "Longsword (+1 weapon) (design provides clue to function) (2315 gp)", "Longsword (+1 weapon) (inscription provides clue to function) (2315 gp)", 
                            "Longsword (+1 weapon) (sheds light) (2315 gp)", "Longsword (+1 weapon, Courageous) (sheds light) (8315 gp)", "Longsword (+1 weapon, Defending) (8315 gp)", 
                            "Longsword (+1 weapon, Frost) (8315 gp)", "Longsword (+1 weapon, Shock) (8315 gp)", "Longsword (+1 weapon, Spell Storing) (8315 gp)", "Longsword (+2 weapon) (8315 gp)", 
                            "Longsword (+2 weapon) (inscription provides clue to function) (8315 gp)", "Mistmail (2250 gp)", "Mithral Heavy Shield (1020 gp)", "Mithral Shirt (1100 gp)", "Mithral Splint Mail (9200 gp)", 
                            "Morningstar (+1 weapon) (2308 gp)", "Morningstar (+1 weapon) (design provides clue to function) (2308 gp)", "Morningstar (+1 weapon) (sheds light) (2308 gp)", 
                            "Morningstar (+1 weapon, Throwing) (8308 gp)", "Morningstar (+2 weapon) (8308 gp)", "Morningstar (+2 weapon, Anarchic) (inscription provides clue to function) (32308 gp)", 
                            "Nunchaku (+1 weapon) (2302 gp)", "Nunchaku (+1 weapon) (design provides clue to function) (2302 gp)", "Nunchaku (+1 weapon, Conductive) (sheds light) (8302 gp)", 
                            "Nunchaku (+1 weapon, Merciful) (sheds light) (8302 gp)", "Padded Armor (+1 armor) (1155 gp)", "Padded Armor (+1 armor, Bitter) (4155 gp)", "Padded Armor (+1 armor, Dastard) (4155 gp)", 
                            "Padded Armor (+1 armor, Delving) (11155 gp)", "Padded Armor (+1 armor, Mirrored) (4155 gp)", "Padded Armor (+2 armor) (4155 gp)", "Padded Armor (+3 armor) (9155 gp)", 
                            "Padded Armor (+4 armor, Mirrored) (25155 gp)", "Quarterstaff (+1 weapon) (2600 gp)", "Quarterstaff (+1 weapon) (design provides clue to function) (2600 gp)", 
                            "Quarterstaff (+1 weapon) (inscription provides clue to function) (2600 gp)", "Quarterstaff (+1 weapon) (sheds light) (2600 gp)", 
                            "Quarterstaff (+1 weapon, Thundering) (sheds light) (8600 gp)", "Quarterstaff (+1 weapon, Vicious) (sheds light) (8600 gp)", "Quarterstaff (+2 weapon) (sheds light) (8600 gp)", 
                            "Rapier (+1 weapon) (2320 gp)", "Rapier (+1 weapon) (inscription provides clue to function) (2320 gp)", "Rapier (+1 weapon) (sheds light) (2320 gp)", "Rapier (+1 weapon, Flaming) (8320 gp)", 
                            "Rapier (+1 weapon, Limning) (8320 gp)", "Rapier (+2 weapon) (8320 gp)", "Rapier (+2 weapon) (sheds light) (8320 gp)", "Rapier (+3 weapon, Bane (dragons)) (sheds light) (32320 gp)", 
                            "Rapier (+3 weapon, Quenching) (sheds light) (32320 gp)", "Sai (+1 weapon) (2301 gp)", "Sai (+1 weapon) (inscription provides clue to function) (2301 gp)", 
                            "Sai (+1 weapon) (sheds light) (2301 gp)", "Sai (+1 weapon, Corrosive) (8301 gp)", "Sai (+1 weapon, Throwing) (8301 gp)", "Sai (+2 weapon) (inscription provides clue to function) (8301 gp)", 
                            "Sap (+1 weapon) (2301 gp)", "Sap (+1 weapon) (sheds light) (2301 gp)", "Sap (+2 weapon, Holy) (32301 gp)", "Scale Mail (+1 armor) (1200 gp)", "Scale Mail (+1 armor, Defiant) (4200 gp)", 
                            "Scale Mail (+1 armor, Jousting) (4950 gp)", "Scale Mail (+1 armor, Mirrored) (4200 gp)", "Scale Mail (+1 armor, Poison-resistant) (3450 gp)", "Scale Mail (+1 armor, Rallying) (6200 gp)", 
                            "Scale Mail (+1 armor, Stanching) (4200 gp)", "Scale Mail (+2 armor) (4200 gp)", "Scale Mail (+3 armor, Dastard) (16200 gp)", "Scale Mail (+3 armor, Defiant) (16200 gp)",
                            "Scale Mail (+3 armor, Spell Storing) (16200 gp)", "Scale Mail (+4 armor) (16200 gp)", "Screaming Bolt (267 gp)", "Screaming Bolt (267 gp) (inscription provides clue to function)", 
                            "Scythe (+1 weapon) (2318 gp)", "Scythe (+1 weapon) (inscription provides clue to function) (2318 gp)", "Scythe (+1 weapon) (sheds light) (2318 gp)", "Scythe (+1 weapon, Ki Focus) (8318 gp)", 
                            "Scythe (+2 weapon) (8318 gp)", "Scythe (+2 weapon) (design provides clue to function) (8318 gp)", "Scythe (+2 weapon) (sheds light) (8318 gp)", "Scythe (+2 weapon, Corrosive) (18318 gp)", 
                            "Scythe (+3 weapon) (design provides clue to function) (18318 gp)", "Searing Arrow (1516 gp)", "Searing Arrow (1516 gp) (sheds light)", "Shieldsplitter Lance (18310 gp) (sheds light)", 
                            "Shortbow (+1 weapon) (2330 gp)", "Shortbow (+1 weapon) (design provides clue to function) (2330 gp)", "Shortbow (+1 weapon) (inscription provides clue to function) (2330 gp)", 
                            "Shortbow (+1 weapon) (sheds light) (2330 gp)", "Shortbow (+1 weapon, Bane) (8330 gp)", "Shortbow (+1 weapon, Frost) (8330 gp)", "Shortbow (+1 weapon, Shock) (8330 gp)", 
                            "Shortbow (+1 weapon, Thundering) (8330 gp)", "Shortbow (+2 weapon) (inscription provides clue to function) (8330 gp)", "Shortbow (+3 weapon, Cunning) (sheds light) (32330 gp)", 
                            "Shortspear (+1 weapon) (2301 gp)", "Shortspear (+1 weapon) (sheds light) (2301 gp)", "Shortspear (+1 weapon, Jurist) (8301 gp)", "Shortspear (+1 weapon, Limning) (sheds light) (8301 gp)", 
                            "Shortspear (+2 weapon) (8301 gp)", "Shortspear (+2 weapon) (sheds light) (8301 gp)", "Shortspear (+2 weapon, Glorious) (design provides clue to function) (32301 gp)", 
                            "Shortsword (+1 weapon) (2310 gp)", "Shortsword (+1 weapon) (inscription provides clue to function) (2310 gp)", "Shortsword (+1 weapon) (sheds light) (2310 gp)", 
                            "Shortsword (+1 weapon, Bane (aberrations)) (8310 gp)", "Shortsword (+1 weapon, Flaming) (8310 gp)", "Shortsword (+1 weapon, Grayflame) (8310 gp)", 
                            "Shortsword (+1 weapon, Limning) (sheds light) (8310 gp)", "Shortsword (+1 weapon, Mighty Cleaving) (sheds light) (8310 gp)", "Shortsword (+2 weapon) (8310 gp)", 
                            "Shortsword (+2 weapon) (sheds light) (8310 gp)", "Sickle (+1 weapon) (2306 gp)", "Sickle (+1 weapon) (sheds light) (2306 gp)", "Sickle (+2 weapon) (8306 gp)", 
                            "Sickle (+3 weapon, Thundering) (32306 gp)", "Sizzling Arrow (1516 gp)", "Sizzling Arrow (1516 gp) (sheds light)", "Slaying Arrow (humanoids, elf) (2282 gp) (sheds light)", 
                            "Slaying Arrow (humanoids, orc) (2282 gp)", "Slaying Arrow (humanoids, reptilian) (2282 gp)", "Slaying Arrow (magical beasts) (2282 gp)", "Slaying Arrow (monstrous humanoids) (2282 gp)", 
                            "Slaying Arrow (outsiders, lawful) (2282 gp)", "Slaying Arrow (undead) (2282 gp)", "Sleep Arrow (132 gp)", "Sleep Arrow (132 gp) (design provides clue to function)", 
                            "Sleep Arrow (132 gp) (sheds light)", "Sling (+1 weapon) (2300 gp)", "Sling (+1 weapon) (design provides clue to function) (2300 gp)", "Sling (+1 weapon) (sheds light) (2300 gp)", 
                            "Sling (+1 weapon, Frost) (8300 gp)", "Sling (+2 weapon) (inscription provides clue to function) (8300 gp)", "Sling (+2 weapon, Igniting) (32300 gp)", "Spear (+1 weapon) (2302 gp)", 
                            "Spear (+1 weapon) (design provides clue to function) (2302 gp)", "Spear (+1 weapon) (sheds light) (2302 gp)", "Spear (+1 weapon, Bane (outsiders, lawful)) (sheds light) (8302 gp)", 
                            "Spear (+1 weapon, Corrosive) (8302 gp)", "Spear (+1 weapon, Cunning) (8302 gp)", "Spear (+1 weapon, Frost) (sheds light) (8302 gp)", "Spear (+1 weapon, Ominous) (8302 gp)", 
                            "Spear (+2 weapon) (8302 gp)", "Spear (+2 weapon) (inscription provides clue to function) (8302 gp)", "Splint Mail (+1 armor) (1350 gp)", "Splint Mail (+1 armor, Defiant) (4350 gp)", 
                            "Splint Mail (+1 armor, Expeditious) (5350 gp)", "Splint Mail (+1 armor, Invulnerability) (16350 gp)", "Splint Mail (+2 armor) (4350 gp)", "Splint Mail (+2 armor, Shadow) (8100 gp)", 
                            "Splint Mail (+3 armor, Deathless) (16350 gp)", "Studded Leather Armor (+1 armor) (1175 gp)", "Studded Leather Armor (+1 armor, Bolstering) (4175 gp)", 
                            "Studded Leather Armor (+1 armor, Dastard) (4175 gp)", "Studded Leather Armor (+1 armor, Fortification (light)) (4175 gp)", "Studded Leather Armor (+1 armor, Slick) (4925 gp)", 
                            "Studded Leather Armor (+1 armor, Spell Storing) (4175 gp)", "Studded Leather Armor (+2 armor) (4175 gp)", "Studded Leather Armor (+2 armor, Glamered) (6875 gp)", "Tangle Bolt (226 gp)", 
                            "Tangle Bolt (226 gp) (inscription provides clue to function)", "Tangle Bolt (226 gp) (sheds light)", "Tower Shield (+1 shield) (1180 gp)", "Tower Shield (+1 shield, Bashing) (4180 gp)", 
                            "Tower Shield (+1 shield, Impervious) (4180 gp)", "Tower Shield (+2 shield) (4180 gp)", "Tower Shield (+3 shield) (9180 gp)", "Tower Shield (+4 shield, Ramming) (25180 gp)", 
                            "Tracer Bullet (100 gp)", "Tracer Bullet (100 gp) (sheds light)", "Trident (+1 weapon) (2315 gp)", "Trident (+1 weapon) (design provides clue to function) (2315 gp)", 
                            "Trident (+1 weapon) (inscription provides clue to function) (2315 gp)", "Trident (+1 weapon, Ghost Touch) (8315 gp)", "Trident (+3 weapon) (sheds light) (18315 gp)", 
                            "Warhammer (+1 weapon) (2312 gp)", "Warhammer (+1 weapon) (design provides clue to function) (2312 gp)", "Warhammer (+1 weapon) (inscription provides clue to function) (2312 gp)", 
                            "Warhammer (+1 weapon) (sheds light) (2312 gp)", "Warhammer (+1 weapon, Frost) (sheds light) (8312 gp)", "Warhammer (+2 weapon) (8312 gp)", "Warhammer (+2 weapon) (sheds light) (8312 gp)", 
                            "Whip (+1 weapon) (2301 gp)", "Whip (+1 weapon) (inscription provides clue to function) (2301 gp)", "Whip (+1 weapon) (sheds light) (2301 gp)", "Whip (+2 weapon) (sheds light) (8301 gp)", 
                            "Winged Shield (17257 gp)", "Zombie Skin Shield (2159 gp)"]
    possibility = intelligent * random.randrange(1, 101, 1)
    if possibility > 96 :
        details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, intemIntellList[random.randrange(0, intemIntellList.__len__(), 1)], alignmentList[random.randrange(0, alignmentList.__len__(), 1)], "\n", 
                        sensesList[random.randrange(0, sensesList.__len__(), 1)], powersList[random.randrange(0, powersList.__len__(), 1)], "\n", purposeList[random.randrange(0, purposeList.__len__(), 1)], 
                        dedPowersList[random.randrange(0, dedPowersList.__len__(), 1)], "\n", baseEgoModList[random.randrange(0, baseEgoModList.__len__(), 1)], 
                        intMagicEquipList[random.randrange(0, intMagicEquipList.__len__(), 1)])
    return details   

def EncouterTreasure(cr, currency = 100, artObj = 100, specialMats = 100, normEquip = 100,
                     magicEquip = 100, pots = 100, scroll = 100, wand = 100, staff = 100, rod = 100, ring = 100,
                     wonderous = 100, artifact = 100, cursed = 100, intelligent = 100) :
    details = ""
    details = Currency(cr, currency)  
    details = ArtObj(cr, artObj)  
    details = SpecialMats(cr, specialMats)  
    details = NormEquip(cr, normEquip)  
    details = MagicEquip(cr, magicEquip)   
    details = Pots(cr, pots)  
    details = Scroll(cr, scroll)  
    details = Wand(cr, wand)  
    details = Staff(cr, staff)  
    details = Rod(cr, rod) 
    details = Ring(cr, ring) 
    details = Wonderous(cr, wonderous)   
    details = Artifact(cr, artifact)   
    details = Cursed(cr, cursed)   
    details = Intelligent(cr, intelligent)

    return details

def HoardTreasure(cr, currency = 100, artObj = 100, specialMats = 100, normEquip = 100,
                  magicEquip = 100, pots = 100, scroll = 100, wand = 100, staff = 100, rod = 100, ring = 100,
                  wonderous = 100, artifact = 100, cursed = 100, intelligent = 100) :
    details = ""
    details = Currency(cr, currency)  
    details = ArtObj(cr, artObj)  
    details = SpecialMats(cr, specialMats)  
    details = NormEquip(cr, normEquip)  
    details = MagicEquip(cr, magicEquip)   
    details = Pots(cr, pots)  
    details = Scroll(cr, scroll)  
    details = Wand(cr, wand)  
    details = Staff(cr, staff)  
    details = Rod(cr, rod) 
    details = Ring(cr, ring) 
    details = Wonderous(cr, wonderous)   
    details = Artifact(cr, artifact)   
    details = Cursed(cr, cursed)   
    details = Intelligent(cr, intelligent)
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