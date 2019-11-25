import random
import NPCGenorator
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def Population(cityType) :
    details = ""
    if cityType == "v" :
        details = "%s%s%s%s" % (details, "Population: ", random.randrange(200, 1599, 1), "\n")
    elif cityType == "t" :
        details = "%s%s%s%s" % (details, "Population: ", random.randrange(2000, 5000, 1), "\n")
    elif cityType == "c" :
        details = "%s%s%s%s" % (details, "Population: ", random.randrange(5000, 18000, 1), "\n")
    else :
        details = "%s%s%s%s" % (details, "Population: ", random.randrange(23000, 75000, 1), "\n")
    return details

def Military(strength) :
    details = ""
    if strength == "conscripts" :
        details = "%s%s%s%s%s" % (details, "Military Strength(conscripts): ", random.randrange(0, 2, 1), "%", " of population\n")
    if strength == "low" :
        details = "%s%s%s%s%s" % (details, "Military Strength: ", random.randrange(4, 8, 1), "%", " of population\n")
    if strength == "medium" :
        details = "%s%s%s%s%s" % (details, "Military Strength: ", random.randrange(9, 16, 1), "%", " of population\n")
    if strength == "high" :
        details = "%s%s%s%s%s" % (details, "Military Strength: ", random.randrange(16, 22, 1), "%", " of population\n")
    else :
        details = "%s%s%s%s%s" % (details, "Military Strength: ", random.randrange(22, 50, 1), "%", " of population\n")
    return details

def Race() :
    details = ""
    num = random.randrange(1, 11, 1)
    if num == 1 :
        subType = "human"
    elif num == 2 :
        subType = "dwarf"
    elif num == 3 :
        subType = "gnome"
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
    elif num == 9 :
        subType = "lizardfolk"
    else :
        subType = "changling"

    details = "%s%s%s" % ("Humanoid(", subType, ")\n")
    return details, subType

def Leader(alignment, cityType, race) :
    details = ""
    if cityType == "v" :
        cr = 5
    elif cityType == "t" :
        cr = 7
    elif cityType == "c" :
        cr = 12
    else :
        cr = 18
    fileName = NPCGenorator.Humanoid(cr = cr, classNames = "Noble", subType = race)
    details = "%s%s%s%s" % (details, "Filename: ", fileName, "\n")
    return details

def NotableNPCs(alignment, cityType) :
    details = ""
    if cityType == "v" :
        cr = random.randrange(1, 5, 1)
        num = random.randrange(1, 15, 1)
    elif cityType == "t" :
        cr = random.randrange(1, 7, 1)
        num = random.randrange(10, 25, 1)
    elif cityType == "c" :
        cr = random.randrange(1, 12, 1)
        num = random.randrange(25, 60, 1)
    else :
        cr = random.randrange(1, 18, 1)
        num = random.randrange(80, 100, 1)
    while num > 0 :
        fileName = NPCGenorator.Humanoid(cr = cr, classNames = "Noble", subType = race)
        details = "%s%s%s%s" % (details, "Filename: ", fileName, "\n")
        num -= 1
    return details

def Wealth(cityType) :
    details = ""
    if cityType == "v" :
        details = "%s%s%s%s" % (details, "Wealth: ", random.randrange(2000, 15990, 1), " gp\n")
    elif cityType == "T" :
        details = "%s%s%s%s" % (details, "Wealth: ", random.randrange(20000, 50000, 1), " gp\n")
    elif cityType == "C" :
        details = "%s%s%s%s" % (details, "Wealth: ", random.randrange(500000, 1800000, 1), " gp\n")
    else :
        details = "%s%s%s%s" % (details, "Wealth: ", random.randrange(5300000, 21500000, 1), " gp\n")
    return details

def NoteablePlaces(cityType, alignment, race) :
    details = ""
    holder = []
    noteableLocations = ["The Old Burrows: A modest tavern, largely built into the side of a small hill and catering exclusively to halflings. It is known for its invisible food and drink.", "The Witch's Tavern: A large adventurer's inn, built within what was once a wizard's tower.", "The Shrine of Sacha: A stone lantern enshrining the flame of Sacha, God of the Sky, said to be sometimes visited by the god himself.", 
                            "The Garden of Statues: An overgrown garden filled with weirdly life-like stone statues. It is said that a medusa's lair lies somewhere within the hedge labyrinth.", "The Shrine of Ambriel: A cauldron lamp enshrining the flame of Ambriel, Lord of Disasters, said to bestow favor to those who leave an offering.", "The Empyrean Odeum: A grand stone-walled theatre, said to be haunted by the ghost of a mummer.", "Piersym's Carvings: A cluttered woodcarver's workshop, built within a copse of elder trees.", 
                            "The ruins of Hughye Keep.", "The Crossed Swords: A fanciful commoner's inn, decorated with exotic weapons and armor.", "The Bloody Thorn: A fanciful dwarven tavern, kept by a brass dragon named Muabuna.", "Breda's Pottery: A modest potter's workshop, decorated with many of what appear to be dragon eggs.", "The Inn of a Thousand Names: A large elven inn, which is said to have a thousand doors in a thousand towns, each under a different sign and name. Anyone who enters through a particular door can only leave through that same door, unless they know the innkeeper's secret.", 
                            "The Courthouse: An impressive half-timbered building, filled with busy magistrates and advocates.", "An obelisk of rough-hewn stone, placed to honor Lady Earcorn.", "Anies' Carvings: A modest woodcarver's workshop, built around a large ash tree.", "Birdsong Alley: A verdant alley between buildings. Though no birds are ever seen, it is often filled with gentle birdsong.", "An ancient temple ruins, which appears restored upon the night of the solstice.", "The Wench's Cellar: A modest elven inn, which seems to be bigger on the inside than on the outside.", "Horne's Pottery: The workshop of a female human potter named Ecin Horne, who knows the secret of an alchemical clay which is as clear as diamond.", 
                            "The Harlequin and Mug: A large commoner's tavern, built atop an outcrop of quartz crystal.", "A tall spire of rune-carved stone, which floats several inches above the ground.", "The Topaz Goblet: A fanciful adventurer's inn, said to be a front for the Thieves' Guild.", "The Shrine of Culsu: A stone niche enshrining an idol of Culsu, Goddess of Love, surrounded by a labyrinth path.", "Aelfgynn's Forge: A large blacksmith's workshop, built within the walls of an old iron tower.", "Heahga's Woodwork: A cluttered woodcarver's workshop, carved out of the trunk of a large oak tree.", "The Broken Hammer: A large commoner's inn, said to be built atop an ancient dungeon.", 
                            "Greenhome: A single storey building of stone walls which has been completely overgrown by flowering vines scale-like leaves thorny vines writhing vines. It is the home of Ereshki, a young green dragon and sage.", "The Odeum of Hilosid: A grand half-timbered theatre, known for its fiery draconic operas.", "The Shrine of Bielel: A bronze statue of Bielel, Lord of Vengeance, said to bestow favor to those who leave an offering.", "Gralphye's Masonry: The workshop of a male human stonemason named Gralphye, who seems to know every dungeon within twenty leagues of town.", "Raffin's Pottery: The workshop of a male human potter named Raffin, who was once a great wizard, but stumbled into a fortune and retired.", 
                            "The Courthouse: A grand building of stone walls, filled with pompous magistrates and advocates.", "The Scoundrel and Flask: An elegant elven inn, said to be haunted by the ghost of a sphinx.", "The ruins of Pycey Tower.", "The Guildhall: An ornate building of timber and brick walls, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", 
                            "The Pavilion of Spirits: A grand stone-walled theatre, home of a female human named Cece Bourney and her troupe of trained owls.", "The Lazy Hero: A heroic elven tavern, known for its epic trivia and arcana contests.", "The Earth Shrine: A wondrous statue of rough granite, said to hold the ruby heart of the world.", "The Golem's Pottery: A neglected potter's workshop, served by a single clay golem. The golem will accept commands from anyone, but only follows commands to craft goblets, bowls, and other simple thrown wares.", 
                            "The Warrior and Scroll: A fanciful elven tavern, kept by a retired wizard named Ewin Moore.", "Exard's Forge: A modest blacksmith's workshop, built around a volcanic fissure filled with flames.", "A ruined tower of blackened stone walls, said to be haunted by the ghost of the last lord of a long-forgotten kingdom.", "Aldelm's Masonry: The workshop of a male human stonemason named Aldelm, who is rumored to be quarrying stone from a cursed ruins.", "The Theatre of Polinios: A large half-timbered theatre, known for its week-long elven epics.", 
                            "The Guildhall: A large half-timbered building, once a minor temple. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Aengen's Armor and Shields: The workshop of a female human armorer named Aengen, who also sells potions of healing.", "The Pool of Enellan: A large stone basin filled with clear water. It is said that the pool sometimes reveals visions of the future to those who gaze into it long enough.", "The Crossed Hammers: A shabby commoner's tavern, which serves only rum.", 
                            "An ancient abbey ruins, which appears restored upon the night of the new moon.", "The Academy of Arcane Study: A small school of witches and wizards, said to be haunted by the ghost of an arch-wizard.", "Burga's Blades: A large weaponsmith's workshop, built around a shrine of Nellote, Lady of War.", "Elil's Arsenal: The workshop of a female human weaponsmith named Elil, known for her poisoned daggers.", "The House of Whispers: A two-storey half-timbered theatre, known for its week-long elven epics.", "The Golden Dagger: A neglected commoner's inn, built within an ancient tower of rune-carved stone.", "George's Pottery: A modest potter's workshop, built within what was once a titan's tankard.", 
                            "A ruined keep of rotting stone walls, said to lie atop a dungeon filled with long-forgotten treasures.", "Blinge's Masonry: A neglected stonemason's workshop, said to be guarded by living gargoyles.", "The Guildhall: An impressive timber and brick building, decorated with wrought-iron lamps. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", "The Hanging Tower: A three-storey tower of stone walls hangs upside-down from a floating earthmote. It is infested by a colony of bats, and said to be the lair of an ancient vampire named Thermundo.", "The Fool's Pub: A modest adventurer's inn, known for its impossible variety of beers and ales.", 
                            "The Jester and Rose: A grand adventurer's tavern, built within what was once a minor temple.", "Aeved's Pottery: A cluttered potter's workshop, which uses a volcanic fissure as a firing kiln.", "The Cursed Wand: A shabby dwarven tavern, brightly lit by glowing gemstones set into the ceiling.", "The Beggar's Ring: A ring of quartz monoliths stands beside the street, usually attended by beggars and waifs. Anyone who stands within the ring and tosses aside a gold coin can teleport to any street location within town.", "The Stormspire: An ancient obelisk of weathered stone, engraved with columns of arcane glyphs. Each time the spire is struck by lightning, it vanishes for exactly nine hours. Each time it returns, some of the glyphs have changed.", 
                            "The Stormspire: A column of hewn crystal, engraved with columns of arcane runes. Each time the spire is struck by lightning, it vanishes for exactly nine hours. Each time it returns, some of the runes have changed.", "The Wench and Chalice: A heroic commoner's tavern, within which time seems to pass more slowly.", "The Viridian Cask: A grand commoner's tavern, known for the ghosts which haunt its halls.", "Waerhuia's Pottery: A cluttered potter's workshop, built around a shrine of Hadriel, Lady of Earth.", "The Weavers Guild House: A grand half-timbered building, decorated with wrought-iron lamps.", "Wisym's Arsenal: The workshop of a male human weaponsmith named Wisym, who has been purchasing much more raw iron than usual.", 
                            "The Asylum: A single storey stone-walled building, filled with the madmen and lunatics of the town.", "The Broken Fang: A fanciful commoner's inn, which serves only brandy.", "Intes' Clocks: A neglected clockmaker's workshop, built within what was once an aristocrat's manor.", "The Shrine of Samua: A stone lantern enshrining the flame of Samua, Goddess of Trickery, said to be sometimes visited by the goddess herself.", "The Cracked Mug: A fanciful dwarven inn, kept by a retired knight named Jamas.", "Kater's Armor and Shields: A neglected armorer's workshop, built within the walls of an iron-banded stone tower.", "Cyne's Masonry: A cluttered stonemason's workshop, said to be guarded by living gargoyles.", 
                            "The Guildhall: An impressive timber and brick building, once a minor temple. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Wulfa's Blades: The workshop of a male human weaponsmith named Wulfa, who was once an adventurer, but retired after his companions were lost in the Black Prison of Souls.", "The Shrine of Maelik: A stone niche enshrining the holy symbol of Maelik, God of Love, said to bestow favor to those who leave an offering.", "The Dragon Stables: The original stalls of this huge stone-walled building were each large enough to hold a young dragon. They have been divided by wooden frames into horse stalls, which are hired out to merchants, pilgrims, and other travellers.", 
                            "The Shrine of Kusha: A stone statue of Kusha, God of War, surrounded by a labyrinth path.", "The Artificers Guild House: A two-storey building of living wood, decorated with stained glass windows.", "Ered's Carvings: The workshop of a female human woodcarver named Ered, known for her intricate puzzle boxes.", "An ancient spire of polished stone, said to be the key to a planar gate.", "An obelisk of dark stone, said to entomb a relic of Goneli, Lord of Trickery.", "The Jade Runestone: A broken menhir of green jade, engraved with arcane runes. It is said that any child born within a league of the stone upon the night of the equinox will live a charmed life.", 
                            "Gery's Clocks: The workshop of a male human clockmaker named Gery, known for his mastery of languages.", "An ancient abbey ruins, which appears restored upon the night of the full moon.", "Lowe's Masonry: A modest stonemason's workshop, built within a ring of ancient stone monoliths.", "Ryany's Masonry: The workshop of a male human stonemason named Ryany, known for his knowledge of dwarven runes and glyphs.", "The Viridian Axe: A modest elven tavern, decorated with wards against demons.", "The Yellow Staff: A neglected adventurer's tavern, built atop an outcrop of hewn and rune-carved stone.", "A column of dark stone, which floats several inches above the ground.", "A tall statue of polished stone, placed to mark the Battle of Baleah Keep.", 
                            "The Beggar and Wain: A modest adventurer's inn, which serves magical potions in addition to beers and ales.", "Marget's Smithy: A neglected blacksmith's workshop, built within the walls of an old iron tower.", "Pere's Masonry: A modest stonemason's workshop, built around a shrine of Bride, Goddess of Earth.", "Raffin's Clocks: The workshop of a male human clockmaker named Raffin, who leads both the Clockmakers and Trapwrights Guilds.", "The Lightning Tree: This tall tree seems to be struck by lightning in every storm, and its bark bears countless intricate burn scars.", "Pycey's Masonry: The workshop of a female human stonemason named Bryne Pycey, known for her weirdly specific knowledge of giants.", 
                            "Vynge's Woodwork: The workshop of a female human woodcarver named Marger Vynge, known for her intricate puzzle boxes.", "The Guildhall: A grand building of timber and brick walls, decorated with finely carved friezes. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Hell's Close : A narrow alley which ends at the broken ruins of a warlock's tower. Anyone walking towards the ruins becomes enveloped by phantasmal shadows.", "The Pavilion of Veils: A two-storey stone-walled theatre, said to be built upon the ground where a sidhe noble was betrayed and murdered.", "Wyny's Masonry: A modest stonemason's workshop, said to be guarded by living gargoyles.", 
                            "The Lewd Wench: A modest adventurer's inn, kept by a sphinx named Nanna.", "The Shrine of Thenry: A cauldron lamp enshrining the flame of Thenry, God of Lies, surrounded by a neglected garden.", "The Honest Merchant: The shop of a female human equipment merchant named Kathon, within which a magical spell prevents lies and falsehoods from being spoken.", "The Pillory of Immortality: A madman has been trapped within this pillory for as long as anyone can remember. He does not age, and cannot be freed.", "The Bloody Arrow: A shabby commoner's tavern, kept by a bronze dragon named Baalatu.", "The Glassblowers Guild House: A grand half-timbered building, decorated with stained glass windows.", "The ruins of Wroby Tower.", "The Artificers Guild House: A single storey building of finely wrought iron, decorated with wards against demons.", 
                            "The Alchemists Guild House: A three-storey tower of finely carved stone, guarded by a stone golem.", "The Crossed Hammers: A large elven inn, which serves only rum.", "The Alchemists Guild House: A two-storey building of living wood, decorated with wards against demons.", "The Pirate's Cellar: A shabby dwarven tavern, kept by a bronze dragon named Khazuha.", "The Guildhall: An impressive stone-walled building, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "The Theatre of Lights: A large timber and brick theatre, which seems to be bigger on the inside than on the outside.", "The Earth Shrine: A wondrous obelisk of rough granite, said to be a magical portal to the heart of the world.", 
                            "The Shrine of Hamath Potte: A bronze statue of Hamath Potte, Lord of the Harvest, said to reveal visions to those who leave an offering.", "An ancient column of dark stone, placed to mark the Battle of the Lesingay Forest.", "The Cloister of Veils: An ornate terraced building, decorated with many holy symbols wrought in precious metals.", "The Barracks: A sturdy building of timber and brick walls, a station of of the town guard. It adjoins a small gaol used to detain thieves and scofflaws.", "The Pilgrim and Cup: A shabby elven tavern, built within what was once an aristocrat's manor.", "The Shrine of Ralphye: A stone statue of Ralphye, God of the Sea, said to be sometimes visited by the god himself.", "Ecil's Masonry: A large stonemason's workshop, said to be guarded by living gargoyles.", 
                            "The Hungry King: A fanciful elven inn, built atop an outcrop of hewn and rune-carved stone.", "The Cursed Sword: A modest elven tavern, kept by a gold dragon named Nabiuma.", "The Guildhall: A grand half-timbered building, decorated with brightly dyed pennons. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Tayley's Masonry: A modest stonemason's workshop, built within a ring of ancient stone monoliths.", "Reyny's Masonry: The workshop of a male human stonemason named Reyny, known for his knowledge of dwarven runes and glyphs.", "Gylew's Armaments: A neglected weaponsmith's workshop, built within the walls of an embattled stone tower.", 
                            "The Trickster and Axe: An elegant elven tavern, built within an ancient tower of rune-carved stone.", "The Triumphant Burrows: A modest inn, largely built into the side of a small hill and catering exclusively to halflings. It is known for the fire elemental which dwells in its hearth.", "Kathon's Masonry: A modest stonemason's workshop, built around a shrine of Elen, Goddess of Earth.", "The Temple of Narder, Lord of Plants: An ornate terraced building, decorated with bright lamps and glazed-tile mosaics.", "The Bastille: A magical prison of strong stone walls, guarded by arcane golems. It is said that the guards alone decide how long to hold one condemned, and that none have escaped them.", "The Cracked Cup: A fanciful dwarven inn, kept by a sphinx named Khimmilka.", 
                            "The weathered ruins of a small castle, said to be haunted by the ghost of the last lord of a long-forgotten kingdom.", "The Crowned Warrior: An elegant adventurer's tavern, built atop an outcrop of quartz crystal.", "A broken statue of dark stone, placed to honor a local hero named Stiny Hoport.", "The Druid's Hedge: This old hedge is the home of Lyne, an elven druid who became stuck in the shape of a red fox long ago.", "The Half-full Goblet: A shabby adventurer's tavern, built atop an outcrop of hewn and rune-carved stone.", "Lesym's Pottery: The workshop of a male human potter named Lesym, known for his clever puzzle jugs.", "Gilan's Woodwork: A modest woodcarver's workshop, built around a large elder tree.", 
                            "The Dragon Pottery: The workshop of a female human potter named Hone, built within a large dragon kiln. Hone spends several months filling the shop with thrown pots, then bricks in the door and spends several days firing it. The opening of the fired kiln is a local festival.", "Anell's Armor and Shields: The workshop of a female human armorer named Anell, who is rumored to lead a cult of elemental evil.", "Pyley's Forge: A neglected blacksmith's workshop, built atop an outcrop of volcanic rock.", "The Bloody Dagger: A grand dwarven tavern, kept by a sphinx named Sabi.", "The Well of Evil: A sinister shaft in the ground, filled with malevolent whispers. Small creatures sometimes fall in, and crawl back out as undead horrors.", 
                            "Kater's Hauberks: The workshop of a female human armorer named Kater, who is rumored to lead an infernal cult.", "The Pirate and Blade: A neglected commoner's tavern, kept by a sphinx named Nusuma.", "The House of Spirits: A two-storey stone-walled theatre, which seems to be bigger on the inside than on the outside.", "Parre's Masonry: A modest stonemason's workshop, built within a ring of ancient stone monoliths.", "Wisym's Masonry: The workshop of a male human stonemason named Wisym, known for his secret and concealed doors.", "The Rampant Wench: An elegant adventurer's inn, decorated with stone gargoyles.", "The Cursed Arrow: A fanciful elven inn, said to be built atop a haunted catacombs.", "Rewill's Masonry: The workshop of a male human stonemason named Rewill, who seems to know every dungeon within twenty leagues of town.", 
                            "The Dwarven Mine: A group of dwarves with picks and shovels came here long ago, and began digging. It is said that on a quiet night, one can still hear them toiling far below.", "Annet's Armor and Shields: The workshop of a female human armorer named Annet, who is rumored to work her forge with bound salamanders.", "The Midnight House: A large timber and brick theatre, home of the renowned male human troubadour Henry Amell.", "The Shrine of Brine Lylle: A stone niche enshrining the holy symbol of Brine Lylle, Lady of Plague, said to bestow favor to those who leave an offering.", "A tall monolith of hewn crystal, which glows with magical light upon the night of the new moon.", "Marte's Clocks: A large clockmaker's workshop, built within what was once an aristocrat's manor.", 
                            "The Shrine of Elyn: A stone monolith engraved with the holy symbol of Elyn, Goddess of Lightning, said to be sometimes visited by the goddess herself.", "The Theatre of Aces: A two-storey half-timbered theatre, within which time seems to pass more slowly.", "A ruined tower of corroded iron walls, said to be haunted by the shadows of the warriors who failed to defend it.", "The Archer and Cup: A heroic adventurer's tavern, kept by a copper dragon named Ilis.", "The Guildhall: A grand timber and brick building, decorated with finely carved friezes. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", "The Bronze Blade: A fanciful adventurer's tavern, built within the walls of an ancient iron keep.", "The Pavilion of Silence: A grand half-timbered theatre, within which anything might be an illusion.", "The Cracked Tankard: An elegant elven tavern, known for its invisible food and drink.", 
                            "Koerwe's Pottery: A large potter's workshop, built around a shrine of Arthund Hawe, Lord of Earth.", "The ruins of Payney Tower.", "The Merry King: A fanciful dwarven tavern, said to be a front for the Thieves' Guild.", "Cilia's Woodwork: A cluttered woodcarver's workshop, built around a large hawthorn tree.", "The Courthouse: An ornate timber and brick building, filled with pompous magistrates and advocates.", "Gylex's Pottery: A neglected potter's workshop, built around a shrine of Johny, God of Earth.", "The Crimson Chain: A shabby elven inn, decorated with stone gargoyles.", "The Greedy Beggar: A shabby dwarven inn, decorated with monstrous skulls.", "Sarry's Hauberks: The workshop of a female human armorer named Sarry, known for her knowledge of runes and glyphs.", "The Shrine of Arler: A stone spire engraved with the holy symbol of Arler, Lord of Luck, said to be sometimes visited by the god himself.", "The Dancing Toad: A heroic elven inn, within which time seems to pass more slowly.", "Greenhome: A two-storey timber and brick building which has been completely overgrown by flowering vines scale-like leaves thorny vines writhing vines. It is the home of Saba, a young green dragon and astrologer.", "The ruins of a seven-sided keep, which appears restored upon the night of the solstice.", "The Coliseum: A large circular amphitheatre, known for its trials by combat.", 
                            "A menhir of obsidian, said to be the key to a planar gate.", "The Theatre of Lusostro: A large half-timbered theatre, within which anything might be an illusion.", "The Light Merchant: A two-storey building of timber and brick walls, the shop of a male human weapon merchant named Jamas Eddyn. It is said to be built atop a crater where a piece of the sun fell to earth long ago, and everything Jamas sells glows with warmth when needed.", "The Queen's Stone: It is said that the legendary hero Iden drew the sword Damned Triumph from this anvil of hewn stone and became queen of the realm.", "Wyne's Pottery: The workshop of a male human potter named Holip Wyne, known for his living earthenware figurines.", "The Shrine of Jane: A stone lantern enshrining the flame of Jane, Lady of Fate, said to reveal visions to those who leave an offering.", "The Goblet and Ghost: An elegant elven inn, built within what was once a minor temple. Anyone who enters the inn becomes attended by a personal ghostly companion, who serves and entertains them while they remain.", "The Temple of Athard, God of Death: A grand terraced building, decorated with carved friezes and glazed-tile mosaics.", "The Well of Evil: A sinister shaft in the ground, surrounded by a ring of skulls. Four guards are posted here at all times, each armed with a silver-bladed sword.", "A tall arch of polished stone, said to entomb a relic of Thiliam Vynge, God of Death.", 
                            "Maley's Masonry: A modest stonemason's workshop, built within a ring of ancient stone monoliths.", "Leony's Masonry: The workshop of a male human stonemason named Leony, known for his secret and concealed doors.", "The Shrine of Georguy: A stone niche enshrining an idol of Georguy, God of Nightmares, said to reveal visions to those who leave an offering.", "An overgrown abbey ruins, said to be haunted by floating wisps of flame.", "The Courthouse: A grand half-timbered building, filled with pompous magistrates and advocates.", "The Guildhall: A grand stone-walled building, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "The Clockwork: A large pyramid of rotating gears and ticking escapements, crafted from brass and inscribed with geometric patterns. No-one seems to know who created it, nor when, nor its purpose.", "The Exalted Knave: A fanciful adventurer's tavern, brightly lit by magical candles and crystal chandeliers.", "The Devil's Gallows: It is said that every thief and murderer condemned to these gallows whispers a dark secret or betrayal in the moment before they die.", "The Cracked Goblet: A fanciful adventurer's inn, entirely managed by squirrels.", 
                            "The Troll's Bridge: A stone bridge spans a small stream. It seems perfectly normal, but neither goat nor any other animal will willingly cross over it.", "The Shrine of Ecil: A stone lantern enshrining the flame of Ecil, Lady of Travel, said to bestow favor to those who leave an offering.", "The Shrine of Wyny: A stone niche enshrining an idol of Wyny, God of Civilization, surrounded by a neglected garden.", "A broken column of weathered stone, said to entomb the bones of Lord Munder Hyne.", "The Shepherd and Chariot: A heroic dwarven tavern, decorated with stone gargoyles.", "The ruins of a seven-sided tower, said to lie atop a dungeon filled with long-forgotten treasures.", "Benne's Masonry: The workshop of a female human stonemason named Benne, who is rumored to lead a cult of a monstrous goddess.", "A statue of rune-carved stone, said to entomb an ancient and powerful demon.", "The Guardhouse: A sturdy timber and brick building, headquarters of the town guard. A bronze statue of a goddess of honor stands in front of the building.", "The Hunter's Cellar: A neglected dwarven inn, said to be haunted by the ghost of an arch-wizard.", "The Yellow Chain: A large elven inn, kept by a retired adventurer named Mara.", "Piersym's Carvings: A large woodcarver's workshop, built around a large hawthorn tree.", 
                            "The Guildhall: An ornate timber and brick building, decorated with wrought-iron lamps. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", "Fryany's Arsenal: The workshop of a male human weaponsmith named Fryany, known for his blades, which shine with a cold light when orcs are near.", "A broken menhir of rough-hewn stone, which glows with magical light upon the night of the equinox.", "The Weary Harper: A modest commoner's inn, kept by a retired adventurer named Wyny.", "Alter's Hauberks: The workshop of a male human armorer named Alter, who is rumored to lead a cult of chaos.", "The Temple of Gilex, Lord of the Sun: An ornate stone-walled building, decorated with bright lamps and stained glass windows.", "The Shrine of Elyn: A stone niche enshrining an idol of Elyn, Goddess of Chaos, surrounded by a neglected garden.", "The ruins of Abar Keep.", "Wilhye's Pottery: The workshop of a male human potter named Wilhye, known for his living earthenware figurines.", "Daley's Anvil: The workshop of a female human blacksmith named Elys Daley, who is rumored to possess a small hoard of meteoric iron.", "The Odeum of Euphoria: A large theatre of stone walls, home of a troupe of illusionist-actors.", "The Guildhall: A grand stone-walled building, once an inn house. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", 
                            "A two-storey stone-walled building, the home and personal library of a female human sage named Joane. She specializes in the study of distant lands and peoples.", "Barde's Masonry: A large stonemason's workshop, hewn from a single massive outcrop of rock.", "Nieles' Pottery: The workshop of a male human potter named Nieles, known for his living earthenware figurines.", "The Hanging Tower: A three-storey tower of stone walls hangs upside-down from a floating earthmote. It is infested by a colony of bats, and said to be the lair of an ancient vampire named Cusega.", "Abel's Anvil: The workshop of a female human blacksmith named Abel, who has been purchasing much more raw iron than usual.", "The ruins of Aucien Keep.", "The Verdant House: A two-storey timber and brick theatre, known for its halfling slice of life plays.", "A broken arch of dark stone, placed to mark the Battle of Hingamse Hill.", "Artis' Clocks: The workshop of a male human clockmaker named Artis, known for his mastery of languages.", "The Witch's Tavern: A grand dwarven tavern, kept by a retired adventurer named Gylex Weke.", 
                            "Foxe's Carvings: The workshop of a male human woodcarver named Gylas Foxe, who also brews potions and elixirs.", "The Archer and Flail: A modest elven inn, known for the fire elemental which dwells in its hearth.", "Willew's Clocks: The workshop of a male human clockmaker named Willew, known for his elegant clockwork toys.", "Wene's Anvil: A cluttered blacksmith's workshop, built within the walls of an old iron tower.", "The House of Domacho: A grand timber and brick theatre, said to be haunted by the ghost of a dancer.", "The Light Merchant: A single storey stone-walled building, the shop of a female human weapon merchant named Malia. It is said to be built atop a crater where a piece of the sun fell to earth long ago, and everything Malia sells glows with golden light for a year less a day.", "Gauward's Forge: The workshop of a male human blacksmith named Gauward, who has been purchasing much more raw iron than usual.", "The Viridian Tankard: A large commoner's inn, which seems to be bigger on the inside than on the outside.", 
                            "The Hound and Hell-hound: An elegant commoner's tavern, built within the walls of an ancient iron keep.", "The Guildhall: An ornate building of stone walls, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "A tall monolith of polished stone, said to entomb a relic of Sabil, Lady of Chaos.", "The Thirsty Hero: An elegant adventurer's tavern, kept by a retired wizard named Ernard Paray.", "A column of dark stone, said to entomb an ancient and powerful demon.", "The Cloister of Death: An open courtyard surrounded by caryatids of hewn stone. A company of ghostly elven warriors gathers within the cloister upon the night of the solstice.", "A broken statue of dark stone, said to be the key to a planar gate.", 
                            "Gauwyn's Masonry: The workshop of a male human stonemason named Gauwyn, who seems to know every dungeon within twenty leagues of town.", "The Eye of Horus: An ancient bronze statue of a male human warrior with the head of a falcon. It is said that anyone who sacrifices one of their own eyes before the statue can see and speak with Death until the next dawn.", "The Pavilion of Tears: A grand timber and brick theatre, said to be haunted by the ghost of a jester.", "The ruins of Rewalt Tower.", "The Guildhall: A large building of half-timbered walls, once an inn house. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Gyles' Masonry: The workshop of a male human stonemason named Gyles, known for his weirdly specific knowledge of giants.", "The Broken Hammer: A heroic elven tavern, within which time seems to pass more slowly.", "The Silver House: A grand timber and brick theatre, known for its week-long elven epics.", "A menhir of crystal, which floats several feet above the ground.", "Rarder's Clocks: A large clockmaker's workshop, built around a shrine of Thamath, Lord of Time.", "The Theatre of Whispers: A two-storey theatre of half-timbered walls, home of a thieves' guild pretending to be dancers.", "Eryn's Masonry: A modest stonemason's workshop, built within a ring of ancient stone monoliths.", "Hany's Masonry: The workshop of a male human stonemason named Hany, known for his knowledge of dwarven runes and glyphs.", "The Gudon Gate: An arch of weathered stone, within which lies a magical portal to the distant town of Gudon.", "An ancient arch of polished agate, which glows with magical light upon the night of the solstice.", "Gery's Armaments: A neglected weaponsmith's workshop, built within the walls of an embattled stone tower.", "The Stone Dragon: A colossal petrified dragon stands over the street. It is said that the dragon will be made flesh again if any descendant of the wizard who imprisoned it passes by without leaving a coin.", "Deray's Clocks: The workshop of a male human clockmaker named Nichye Deray, who is rumored to be immortal.", "The Arena: A large semi-circular amphitheatre, said to be haunted by the ghost of a legendary gladiator.", "The Shrine of Lany Dane: A bronze statue of Lany Dane, Lord of Travel, said to be sometimes visited by the god himself.", "The Clockwork: A large prism of rotating gears and ticking escapements, crafted from brass and inscribed with alien symbols. No-one seems to know who created it, nor when, nor its purpose.", "Steray's Clocks: The workshop of a female human clockmaker named Beatra Steray, known for her mastery of languages.", "Ilis' Carvings: The workshop of a male human woodcarver named Ilis, known for his staves and wands, favored by the Astrologers Society.", "The Old Wall: A section of an old town wall divides several blocks. The ghosts of a town guard can sometimes be seen walking upon it.", "The Citadel: A buttressed building of polished black stone walls, without doors or windows. It is said to be a fortress of the king's army, but no-one has ever been seen to enter or leave it.", "The Well of Evil: A sinister shaft in the ground, filled with noxious fumes. It is said that anyone who casts their own heart into the well will be granted their heart's darkest desire.", "Richye's Armory: The workshop of a male human armorer named Richye, who also sells potions of healing.", "The Stout King: A grand commoner's tavern, known for the fire elemental which dwells in its hearth.", "The Odeum of Pratesos: A large half-timbered theatre, within which anything might be an illusion.", "A broken temple ruins, which appears restored upon the night of the new moon.", "The Lazy Wench: A modest dwarven inn, entirely managed by clockwork golems.", "Mary's Clocks: A neglected clockmaker's workshop, built around a shrine of Anet, Lady of Time.", "The Tabluff Gate: A ring of crystal monoliths, within which lies a magical portal to the distant town of Tabluff.", "The Pavilion of Flames: A grand stone-walled theatre, which has one door here and another in the Divine City of Ingwood.", "The Hanging Tower: A three-storey timber and brick tower hangs upside-down from a floating earthmote. It is said to be haunted by the ghost of a male human mage named Anies, who once ruled the realm through dark sorcery.", "The Spectral Aqueduct: A section of an old aqueduct stands over the street. A curtain of water falls continuously from the lower end of the aqueduct into a large stone basin. The water is clear and cold, but vanishes from any vessel used to contain it.", "The Golem's Pottery: A cluttered potter's workshop, served by a single clay golem. The golem will accept commands from anyone, but only follows commands to craft goblets, bowls, and other simple thrown wares.", "Ennel's Masonry: The workshop of a female human stonemason named Ennel, who is rumored to have arranged the murder of the previous guildmaster.", "The Foolish Pilgrim: A heroic adventurer's tavern, said to be a front for the Thieves' Guild.", "The Guildhall: A grand stone-walled building, decorated with stained glass windows. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", "The Abbey of the Luminous Lords: An ornate colonnaded building, decorated with bronze statues of many gods and goddesses.", "An ancient arch of quartz, placed to honor a local god of destruction.", "The Guildhall: An impressive half-timbered building, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local trade guilds.", "Atel's Clocks: A neglected clockmaker's workshop, within which time seems to pass more slowly.", "The Guildhall: An impressive building of stone walls, once an aristocrat's manor. It contains a large meeting hall and several smaller rooms, and is shared amongst several local merchant guilds.", "The Shrine of Hone: A stone monolith engraved with the holy symbol of Hone, Lady of Winter, said to reveal visions to those who leave an offering.", "The Scarlet Cask: A shabby dwarven tavern, known for the fire elemental which dwells in its hearth.", "The Crossed Axes: A shabby dwarven tavern, decorated with monstrous skulls.", "Nathye's Woodwork: A large woodcarver's workshop, built around a large elder tree.", "The King and Flask: A grand adventurer's inn, built within the walls of an ancient iron keep.", "The Broken Arrow: An elegant dwarven tavern, within which a magical spell protects against poisons.", "The Bloody Shield: A grand adventurer's inn, built atop an outcrop of quartz crystal.", "The Cursed Blade: A shabby adventurer's tavern, built atop an outcrop of obsidian.", "The Temple of Hames, Lord of Protection: An impressive colonnaded building, decorated with ethereal curtains and idols of precious stone.", "The Cursed Arrow: A shabby commoner's inn, within which time seems to pass more slowly.", "Brione's Clocks: A neglected clockmaker's workshop, built around a shrine of Hily, Goddess of Time.", "The Yellow Mug: An elegant commoner's tavern, brightly lit by magical candles and crystal chandeliers.", "Vere's Anvil: The workshop of a male human blacksmith named Enryn Vere, who was once the best weaponsmith in the kingdom.", "Thury's Armaments: A neglected weaponsmith's workshop, decorated with a collection of sundered shields."]

    if cityType == "v" :
        num = random.randrange(0, 2, 1)
    elif cityType == "t" :
        num = random.randrange(0, 4, 1)
    elif cityType == "c" :
        num = random.randrange(1, 5, 1)
    else :
        num = random.randrange(3, 10, 1)
    while num > 0 :
        holder.append(random.randrange(0, noteableLocations.__len__(), 1))
        num -= 1
    holder = Remove(holder)
    for i in holder :
        details =  "%s%s%s" % (details, noteableLocations[i], "\n")
    return details

def Inn(cityType) :
    details = ""
    innList = ["Poor Inn", "Inn", "Good Inn", "Noble Inn"]
    holder = []
    if cityType == "v" :
        num = random.randrange(0, 2, 1)
    elif cityType == "t" :
        num = random.randrange(1, 4, 1)
    elif cityType == "c" :
        num = random.randrange(3, 9, 1)
    else :
        num = random.randrange(10, 20, 1)
    while num > 0 :
        holder.append(random.randrange(0, innList.__len__(), 1))
        num -= 1
    for i in holder :
        details =  "%s%s%s" % (details, innList[i], "\n")
    return details

def Store(cityType) :
    details = ""
    storeList = ["Weapon Shop", "Armor Shop", "Wonderous Item Shop", "Potion Shop", "Scroll Shop", "Wand Shop", "General Store", "Magic Shop", "Art Shop", "Jewellery Store"]
    holder = []
    if cityType == "v" :
        num = random.randrange(0, 2, 1)
    elif cityType == "t" :
        num = random.randrange(1, 4, 1)
    elif cityType == "c" :
        num = random.randrange(3, 9, 1)
    else :
        num = random.randrange(10, 20, 1)
    while num > 0 :
        holder.append(random.randrange(0, storeList.__len__(), 1))
        num -= 1
    for i in holder :
        details =  "%s%s%s" % (details, storeList[i], "\n")
    return details

def Craftsman(cityType) :
    details = ""
    craftList = ["Jeweller", "Mason", "Painter", "Carver", "Sculpter", "Apothicary", "Goldsmith", "Miller", "Clothier", "Shoemaker"]
    holder = []
    if cityType == "v" :
        num = random.randrange(0, 2, 1)
    elif cityType == "t" :
        num = random.randrange(1, 4, 1)
    elif cityType == "c" :
        num = random.randrange(3, 9, 1)
    else :
        num = random.randrange(10, 20, 1)
    while num > 0 :
        holder.append(random.randrange(0, craftList.__len__(), 1))
        num -= 1
    for i in holder :
        details =  "%s%s%s" % (details, craftList[i], "\n")
    return details

def Guilds(cityType) :
    details = ""
    guildList = ["Fighters Guild", "Merchants Guild", "Theives Guild", "Assassins Guild", "Wizards Guild", "Craftsmans Guild"]
    holder = []
    if cityType == "v" :
        num = random.randrange(0, 2, 1)
    elif cityType == "t" :
        num = random.randrange(1, 4, 1)
    elif cityType == "c" :
        num = random.randrange(3, 9, 1)
    else :
        num = random.randrange(10, 20, 1)
    while num > 0 :
        holder.append(random.randrange(0, guildList.__len__(), 1))
        num -= 1
    Remove(holder)
    for i in holder :
        details =  "%s%s%s" % (details, guildList[i], "\n")
    return details

# print("What is the Cities Name?\n")
# cityName = ""
# cityName << input()
# print("\nWhat is the Cities Size?((V)illage, (T)own, (C)ity, (M)etropolis)\n")
# cityType = ""
# cityType << input().tolower()
# print("\nWhat is the Cities Alignment?(LG, NG, CG, LN, N, CN, LE, NE, CE)\n")
# alignment = ""
# alignment << input()
# print("\nWhat is the Military strength?(conscripts, low, medium, high, militant)\n")
# strength = ""
# strength << input().tolower()

# detail = ""

# details = Population(cityType) 
# detail = "%s%s" % (detail, details)
# details = Military(strength) 
# detail = "%s%s" % (detail, details)
# details = Wealth(cityType)
# detail = "%s%s" % (detail, details)
# details, race = Race() 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = Leader(alignment, cityType, race) 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = NotableNPCs(alignment, cityType)
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = NoteablePlaces(cityType, alignment, race) 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = Inn(cityType) 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = Store(cityType) 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = Craftsman(cityType) 
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
# details = Guilds(cityType)
# detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")

# fileName = "%s%s%s%s%s" % (cityName, cityType, alignment, strength, ".txt")
# oFile = open(fileName, "w")
# oFile.write(detail)
# oFile.close()



cityNames = ["Ashdale Green", "Barbeck", "Barby", "Barworth", "Birchford Green", "Birchhurst", "Birchleigh", "Birchthwaite", "Blackhey Cross", "Blackpool", "Blackwich", "Dunworth", "Eastleigh", "Eastport", "Great Presden", "Guildhey Heath", "Guildmarsh", "Guildthorpe Cross", "Harburn", "Hartfield Cross", "Hartley", "Hartmoor", "Harwick", "Hazelbeck", "Hazellea", "Hazelwell", "Hazelwich", "Hazelworth", "Henhall Green", "Henhaven Heath", "Henholm", "Henmarsh", "Henmoor", "Henworth", "Hindford", "Hindpool", "Hopham", "Hopleigh", "Hopmarsh", "Hopton", "Hopwick", "Ildale", "Ilford", "Ilpool", "Keldbeck", "Keldton", "Kinbeck Lake", "Kinbrook Green", "Kinbury", "Kindale", "Kinfold", "Kinleigh", "Kinwell", "Kirbrook Bridge", "Kirhalgh Lake", "Kirwich", "Langhall", "Langholm", "Langpool", "Little Foxfold", "Little Hopworth", "Little Kirwike", "Little Otterhall", "Little Overley", "Little Woolhaven", "Marsington Cross", "Middleby", "Milldon", "Millley", "Moorham Lake", "Moorlea", "Newburgh", "Newdale", "Newhurst", "Newmouth Green", "Newwick", "Northhall", "Northhey", "Northwell", "Oakburgh", "Oakdale", "Oakmere", "Otterbury", "Ottermoor", "Otterthwaite", "Oulmoor"]
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

for i in range(0, cityNames.__len__()) :
    detail = ""
    if count[i] == 0 :
        cityType = "v"
    elif count[i] == 0 :
        cityType = "t"
    elif count[i] == 0 :
        cityType = "c"
    else :
        cityType = "m"
    
    cityName = cityNames[i]
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

    strengthList = ["conscripts", "low", "medium", "high", "militant"]
    strength = strengthList[random.randrange(0, strengthList.__len__(), 1)]

    details = Population(cityType) 
    detail = "%s%s" % (detail, details)
    details = Military(strength) 
    detail = "%s%s" % (detail, details)
    details = Wealth(cityType)
    detail = "%s%s" % (detail, details)
    details, race = Race() 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = Leader(alignment, cityType, race) 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = NotableNPCs(alignment, cityType)
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = NoteablePlaces(cityType, alignment, race) 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = Inn(cityType) 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = Store(cityType) 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = Craftsman(cityType) 
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")
    details = Guilds(cityType)
    detail = "%s%s%s" % (detail, details, "\n-----------------------------------------------------------------------------------------------------\n")

    fileName = "%s%s%s%s%s%s" % ("~", cityName, cityType, alignment, strength, ".txt")
    oFile = open(fileName, "w")
    oFile.write(detail)
    oFile.close()