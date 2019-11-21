import random
import TreasureGenerator
def Humanoid(cr, name = None) :
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
        humanMale = ["Alis", "Sagramour", "Sagremor", "Tentagil", "Pelleas", "Gurgalan", "Cnidel", "Carrado", "Llacheu", "Nantres", "Griffyth", "Dagonet", "Anguysh", 
                            "Tristian", "Tristan", "Gringolet", "Daguenet", "Gawain", "Houdain", "Anir", "Ektor", "Pellam", "Albion", "Mabuz", "Uriens", "Camelon", "Brehus", 
                            "Bertram", "Escalibor", "Amr", "Dinadan", "Lludd", "Tor", "Guivret", "Petrus", "Cafall", "Bryan", "Clamedeus", "Melyon", "Percival", "Evrain", 
                            "Bersules", "Breuse", "Antfortas", "Melechan", "Florence", "Evadeam", "Lohengrin", "Laudegrance", "Ector", "Melwas", "Froille", "Bernlak", "Drudwyn", 
                            "Cadwallon", "Gais", "Launcelot", "Mabonaqain", "Pellinore", "Lueius", "Morholt", "Girflet", "Cacamwri", "Caerleon", "Meleagant", "Urien", "Lancelot", 
                            "Goveniayle", "Aglarale", "Dristan", "Royns", "Ryons", "Maldue", "Ysbaddaden", "Borre", "Bors", "Balin", "Peredwus", "Pant", "Calibum", "Gaheris", 
                            "Octha", "Calibor", "Palamedes", "Ither", "Leodegraunce", "Parsifal", "Che", "Griffith", "Cai", "Lucan", "Catterick", "Glais", "Galatyn", "Gareth", 
                            "Cus", "Loe", "Bedwyr", "Rion", "Camlann", "Feirefiz", "Nentres", "Merlin", "Alixandre", "Bercilak", "Ryence", "Lamorak", "Alexandre", "Agravain", 
                            "Taliesin", "Escanor", "Engres", "Caw", "Aglaral", "Kei", "Baldulf", "Bicoir", "Brandelis", "Benoyce", "Owain", "Bellangere", "Bagdemagus", 
                            "Trevrizent", "Kanelinqes", "Tristram", "Accalon", "Bedver", "Gorre", "Cador", "Apollo", "Morold", "Balen", "Bliant", "Avalloc", "Isdemus", "Arthgallo", 
                            "Mabon", "Morgan Tud", "Meliodas", "Tristen", "Awarnach"]
        humanFemale = ["Lynette", "Lunet", "Morgana", "Angharad", "Gwendolen", "Ygeme", "Lausanne", "Ragnall", "Gwendoloena", "Enite", "Viviane", "Lysanor", "Morgawse", 
                            "Ettard", "Chelinda", "Lynessa", "Nyneve", "Igraine", "Grainne", "Margawse", "Clarissant", "Nimue", "Lynnette", "Kay", "Lyonet", "Astolat", 
                            "Gwenhwyfach", "Ade", "Matilda", "Ysolde", "Albiona", "Condwiramurs", "Branwen", "Igrayne", "Herzeloyde", "Shalott", "Elayne", "Avalon", "Avilon", 
                            "Angharat", "Graine", "Acheflow", "Ganieda", "Sebille", "Modron", "Avarona", "Elizabeth", "Cotovatre", "Guanhumora", "Igerne", "Isoude", "Pridwyn", 
                            "Llamrei", "Bedegrayne", "Guenevere", "Lyonors", "Isoud", "Nineve", "Avaron", "Morcades", "Orguelleuse", "Chelinde", "Jenifer", "Soredamors", "Lynne", 
                            "Gwenevere", "Argante", "Iblis", "Creiddyladl", "Elsa", "Belakane", "Anglides", "Enid", "Cundrie", "Sigune", "Lyonesse", "Wenhaver", "Ygraine", 
                            "Gvenour", "Lynet"]
        dwarfMale = ["Thengel", "Ethelward", "Baldor", "Gamling", "Éomund", "Wald", "Dunsig", "Baldmund", "Leofdag", "Hild", "Eorl", "Frumgar", "Baldwig", "Edgar", "Fréaláf", 
                            "Aldor", "Wigbald", "Elfbert", "Celmund", "Fréawine", "Elfgar", "Tirwald", "Eofor", "Adwine", "Fastwine", "Gladwine", "Grimwine", "Cenhelm", "Wulf", 
                            "Cadda", "Garwine", "Folca", "Gríma", "Eforhild", "Léod", "Adwig", "Bertric", "Dunstan", "Aldwine", "Elfswith", "Théodred", "Ethelred", "Háma", 
                            "Leofric", "Baldhelm", "Elfwine", "Hereward", "Eothain", "Ordred", "Hildred", "Dernhelm", "Sewine", "Folcwine", "Hefric", "Tordag", "Grimmund", 
                            "Dunwine", "Britta", "Goldwine", "Brego", "Elfstan", "Ordlac", "Dunhere", "Ethelfrith", "Frithdag", "Fréa", "Ardwulf", "Deorwine", "Hulac", "Elfred", 
                            "Fengel", "Baldric", "Edbert", "Ordstan", "Elfhelm", "Torfrith", "Éomer", "Leofwine", "Fram", "Baldwine", "Baldred", "Déor", "Cenric", "Wulfstan", 
                            "Folcred", "Gram", "Leofstan", "Dungar"]
        dwarfFemale = ["Runfled", "Merewyn", "Cwendar", "Ethelfled", "Mereliss", "Estwyn", "Laywyn", "Trewyn", "Garfled", "Ides", "Darwise", "Gledhild", "Elfhild", "Engifu", 
                            "Saulwyn", "Dawyn", "Layfled", "Elfwise", "Sorgifu", "Shadufled", "Shadugifu", "Edhild", "Estswith", "Cynegith", "Godliss", "Leofled", "Frithild", 
                            "Estrun", "Sunnfled", "Eowyn", "Godswith", "Cwenswith", "Swetelayu", "Trewred", "Leofgifu", "Bledwyn", "Aldwyn", "Meregith", "Cynered", "Sigeburga", 
                            "Meregifu", "Shaduwyn", "Sigewyn", "Mildgith", "Trewfled", "Olfete", "Sweterun", "Burnhild", "Saulred", "Trewhild", "Dargifu", "Dawfled", "Lisswyn", 
                            "Sigerun", "Sunnwyn", "Merthgifu", "Eafled", "Théodburga", "Sunngifu", "Darfled", "Merthgith", "Merefled", "Rosefled", "Swetefled", "Hild", "Adgith", 
                            "Sorrun", "Elfgifu", "Darwyn", "Aldgith", "Brunhild", "Cynewise", "Bledgifu", "Théodrun", "Swetewyn", "Cwenhild", "Wilfled", "Brunwyn", "Lissgifu", 
                            "Trewrun", "Sorwyn", "Cynewyn", "Estmund", "Wilrun", "Mildwyn", "Runwyn", "Burnwyn", "Runwise", "Eawyn", "Théodwyn", "Cynefled", "Runhild"]
        elfMale = ["Melin", "Maethorion", "Loegon", "Erthorion", "Lamaendir", "Galben", "Caraphindaer", "Hababen", "Lossion", "Lithuichon", "Fardaer", "Gwathrenor", "Beltor", 
                            "Mahtar", "Triwathon", "Pegion", "Merethor", "Nasar", "Falchion", "Anglaeg", "Guldurchon", "Gilher", "Lanchion", "Gawon", "Rhovanion", "Vahaiya", "Rhodor", 
                            "Glothroch", "Eithruin", "Fonion", "Ialon", "Istuion", "Nemiron", "Tatharben", "Losdir", "Haradaer", "Carastar", "Corudor", "Colfind", "Haeronor", 
                            "Borniphen", "Pelinelben", "Ýridhremen", "Arasdir", "Cidinnanc", "Goston", "Annor", "Foron", "Graw", "Véra", "Mercion", "Aglareb", "Gilon", "Thendaer", 
                            "Amlugreg", "Agarvorn", "Rosgon", "Forvenor", "Vilwarindil", "Estoladion", "Arrad", "Téro", "Gwaew", "Ereg", "Tavorion", "Solcthor", "Mêr", "Dúvemen", 
                            "Glirdaer", "Candir", "Luinor", "Haerion", "Húrdaer", "Bregiamlug", "Amlugelu", "Rúseaserco", "Mélo", "Dírion", "Caldir", "Noruiben", "Calaear", "Golloron", 
                            "Lónaer", "Miluichanar", "Iamben", "Ianudor", "Thanben", "Carachon", "Lindo", "Gelion", "Amlugidinn", "Deldhimben", "Lanwatan", "Geruilher", "Ordaer", 
                            "Deldhichon", "Yalúmion", "Faucion", "Glîr", "Culinion", "Alasailion", "Írchanar", "Glavroldor", "Tirrion", "Mallen", "Narchorion", "Círchon", "Gollben", 
                            "Gaear", "Rehtar", "Lalphen", "Thondor", "Huirocco", "Arraben", "Gemmon", "Beleg", "Airehíse", "Lennion", "Paran", "Gorthasser", "Egnastor", "Northor", 
                            "Caelebamlug", "Wahaiya", "Amlugalen", "Esgaron", "Mithrildir", "Aegon", "Glamrendir", "Amathluin", "Núrchanar", "Limmon", "Echadrion", "Badhroc", 
                            "Amarion", "Badhron", "Helegnaer", "Úhaeldor", "Bregeben", "Mindonor", "Ianaer", "Nídthor", "Amlugorhal", "Elben", "Maeasdir", "Lírdir", "Vailimo", 
                            "Sarna", "Mindomen", "Úfanweo", "Thôn", "Fannon", "Einior", "Amartharn", "Lostor", "Lámino", "Ídhrion", "Avornamdir", "Cúvallorn", "Lastoron", "Gondir", 
                            "Fanion", "Nullion", "Hethuon", "Baradhroch", "Faenor", "Meldaer", "Cabrion", "Mastaro", "Eldamanar", "Ilvanion", "Rivalchon", "Quildolorion", "Delgarathor", 
                            "Faun", "Abladon", "Alfirin", "Lusto", "Thurilosmben", "Rawon", "Glasdaer", "Nirophen", "Herenion", "Vea", "Ríndir", "Lusta", "Aramdir", "Bothion", "Tumna", 
                            "Hataltamo", "Rátaro", "Parthanar", "Tyelpenasse", "Hwestaer", "Ríchon", "Lesben", "Bregol", "Faerveren", "Duirrochon"]
        elfFemale = ["Istuiwen", "Com", "Alphien", "Norgalaben", "Thîn", "Canben", "Haered", "Morphen", "Amdirnith", "Seriel", "Calimiel", "Berioriel", "Methen", "Caildis", 
                            "Halyare", "Emlineth", "Inu", "Peleccotan", "Súlthel", "Amdirthog", "Laurealassie", "Faimben", "Nirwen", "Celeben", "Melui", "Amdirand", "Ladien", 
                            "Duinen", "Thíndes", "Aderthriel", "Olthel", "Path", "Eregien", "Rýthil", "Esgalwathiel", "Fonthel", "Alagiel", "Cannamdir", "Aerdis", "Dogneth", 
                            "Cullasdis", "Amarthelien", "Úhaelbes", "Caelnith", "Gwaereneth", "Farhel", "Braigiel", "Ladrengilthel", "Fimdes", "Rivaltsel", "Tultar", "Gwache", 
                            "Gwaedhneth", "Uthaessel", "Romben", "Crabandis", "Deldhindis", "Nodwen", "Gorogel", "Boghel", "Gorien", "Taine", "Emlinil", "Gruithoriel", 
                            "Dinalagosbes", "Arndis", "Caraphinnith", "Fasdes", "Erebeth", "Húbes", "Naernith", "Lachel", "Heledirthel", "Amrúmben", "Emethil", "Gronniel", 
                            "Amdiradan", "Maedes", "Forveniel", "Lithuinith", "Pathwen", "Glessil", "Culde", "Gernith", "Istien", "Ruhtariel", "Methenien", "Daenes", "Derenil", 
                            "Amluglagor", "Cadwareth", "Tong", "Amdirbarad", "Gwaengwen", "Glavrol", "Filegeth", "Lúthel", "Ólerydes", "Amathwaen", "Úhaeleth", "Partphen", 
                            "Ungoleth", "Calarien", "Haeromes", "Telde", "Gwanniel", "Caranith", "Gelessil", "Goe", "Húben", "Hedlethil", "Háliel", "Hostnith", "Quentare", "Calad", 
                            "Gweluthel", "Balliniel", "Lámina", "Mánie", "Auþa", "Nindes", "Dúvengwen", "Norniel", "Yaimie", "Brasseneth", "Nadhordis", "Boldes", "Glohel", 
                            "Cúchador", "Glordis", "Ethir", "Nagor", "Aica", "Túghel", "Valda", "Logwen", "Iphambes", "Iachneth", "Lóteriel", "Pegnis", "Míþiel", "Faeniel", 
                            "Eruneth", "Thernil", "Calphel", "Randur", "Hall", "Lótealoxe", "Berenthel", "Aithel", "Erynith", "Edwendes", "Níndis", "Amrúmes", "Gwilwilethel", 
                            "Thangurbes", "Cidinnanc", "Raegwen", "Alate", "Dineniel", "Tundis", "Cíwneth", "Falver", "Achaspen", "Lhaethel", "Dereth", "Adasser", "Ehereg", 
                            "Gorogien", "Gawabes", "Salab", "Corchel", "Nesser", "Thíniel", "Iphangwen", "Ethirhel", "Maethes", "Andamundandil", "Nerythiril", "Caenith", "Laegiel", 
                            "Gorvel", "Calithil", "Húlel", "Roitar", "Rust", "Lindangandie", "Eredthel", "Solcphen", "Lomel", "Conien", "Gwingnith", "Rhossolaspen", "Riellendur", 
                            "Magolneth", "Tatharthel", "Hithuneth", "Laerguliel"]
        gnomeMale = ["Largo", "Merimas", "Wilibald", "Gardner", "Hogg", "Reginard", "Bolger", "Déagol", "Hildigard", "Marcho", "Brandagamba", "Headstrong", "Galpsi", "Carl", 
                            "Hayward", "Noakes", "Flambard", "Hlothran", "Falco", "Meriadoc", "Proudfoot", "Isembold", "Stoor", "Goldworthy", "Diggle", "River Folk", "Hildifons", 
                            "Goodchild", "Bandobras", "Hob", "Fastred", "Goodbody", "Underhill", "Marmadas", "Tolman", "Bucca", "Togo", "Sackville", "Madoc", "Blanco", "Frodo", 
                            "Brandybuck", "Oldbuck", "Hending", "Fosco", "Puddifoot", "Goodenough", "Gamgee", "Ilberic", "Merimac", "Labingi", "Isembard", "Took", "Harfoot", 
                            "Hamson", "Halfred", "Goold", "Bophîn", "Ponto", "Brown", "Galbasi", "Tûk", "Gamwich", "Ferdinand", "Gorbulas", "Maggot", "Rufus", "Andwise", "Moro", 
                            "Daddy", "Isumbras", "Dudo", "Merry", "Dinodas", "Tobold", "Odovacar", "Robin", "Sandyman", "Adelard", "Cottar", "Seredic", "Gawkroger", "Jolly", 
                            "Longo", "Pippin", "Elfstan", "Banks", "Cotman", "Townsend", "Faramir", "Everard", "Halfast", "Smallburrow", "Mugwort", "Rumble", "Sméagol", "Hobson", 
                            "Whitfoot", "Bob", "Odo", "Hildibrand", "Tunnelly", "Butcher", "Lotho", "Brockhouse", "Sancho", "Lightfoot", "Fredegar", "Minto", "North-Tooks", 
                            "Farmer", "Fallohide", "Ted", "Otho", "Bowman", "Holfast", "Rudigar", "Ferdibrand", "Bilbo", "Filibert"]
        gnomeFemale = ["Galpsi", "Amaranth", "Angelica", "Lightfoot", "Boffin", "Bracegirdle", "Gardner", "Chubb-Baggins", "Roper", "Hlothran", "North-Tooks", "Bolger", 
                            "Goldilocks", "Drogo", "Burrowes", "Esmeralda", "Fíriel", "Pott", "Dora", "Rosamunda", "Laura", "Townsend", "Mugwort", "Brockhouse", "Celandine", 
                            "Tanta", "Lobelia", "Twofoot", "Daisy", "Menegilda", "Tûk", "Saradoc", "Noakes", "Primula", "Pimpernel", "Brownlock", "Malva", "Longholes", "Burrows", 
                            "Greenhand", "Hugo", "Hilda", "Lily", "Goold", "Gammidge", "Linda", "Lalia", "Mentha", "Fallohide", "Hogg", "Gamwich", "Fairbairn", "Prisca", "Hayward", 
                            "Goodbody", "Goldworthy", "Labingi", "Brandybuck", "Hanna", "Donnamira", "Pansy", "Mimosa", "Took", "Gorhendad", "Sandheaver", "Melilot", "Goodenough", 
                            "Zaragamba", "Whitfoot", "Mirabella", "Brandagamba", "Bophîn", "May", "Rose", "Baggins", "Bell", "Estella", "Stoor", "Bungo", "Brown", "Smallburrow", 
                            "Butcher", "Clayhanger", "Eglantine", "River Folk", "Sandyman", "Harfoot", "Proudfoot", "Salvia", "Bunce", "Grubb", "Camellia", "Asphodel", "Cotton", 
                            "Primrose", "Maggot", "Banks", "Belladonna", "Hornblower", "Rumble", "Rowan", "Gilly", "Puddifoot", "Belba", "Oldbuck", "Pearl", "Gawkroger", "Berylla"]
        orcish = ["Snagagûl", "Gûlghâsh", "Snagabúrz", "Dugbúrz", "Asholog", "Urukbúrz", "Globuk", "Bagronk", "Ologbúrz", "Gûlbúbhosh", "Búbhoshum", "Ghâshbúrz", "Gûlburzum", 
                            "Pushdug", "Snagaburzum", "Snagasharkû", "Sharkû", "Snagaghâsh", "Burzum", "Ashuruk", "Tamruzîr", "Pharazbalak", "Shakalbalak", "Azrubêl", "Shakalgimil", 
                            "Ûrîthôr", "Bawbuthôr", "Balkazîr", "Zâinabên", "Aphanuzîr", "Dôlguzagar", "Avradizimir", "Rôthzagar", "Rôthzôr", "Bêlzagar", "Zimrupân", "Pharazôn", 
                            "Zimrathôn", "Gimlibên", "Gimilbalak", "Abattârik", "Nimrubên", "Balkumagân", "Azrubên", "Dôlgubalak", "Balakân", "Sapthan", "Shakalzôr", "Shakalzagar", 
                            "Avalôzîr", "Gimilzôr", "Nimruzîr", "Arnubalkân", "Gimlân", "Karbazîr", "Arnubên", "Rôthbalak", "Nilûbên", "Gimilzagar", "Abrazîr", "Azrugimil", 
                            "Rôthpharaz", "Tarîkmagân", "Azruzôr", "Arnuzîr", "Azulzîr", "Îrpân", "Azruzagar", "Shakalpharaz", "Avalôbên", "Azrubalak", "Azrupharaz", "Aglarân", 
                            "Zôrzagar", "Adûnabêl", "Rôthgimil", "Sakalthôr", "Tamrubên"]
        natureNames = ["Aster", "River", "Quarry", "Lake", "Bear", "Ocean", "August", "Bruno", "Sequoia", "Grove", "Viridis", "Flame", "Sunny", "Red", "Sterling", "Finch", 
                            "Green", "North", "Rufous", "Pepper", "Stone", "Bay", "Forrest", "Cardinal", "Frost", "Verdant", "Cliff", "Season", "Wolf", "Indigo", "Berry", 
                            "Glaucous", "Fox", "Umber", "Gray", "Ash", "Crimson", "Clay", "Linx", "Jonquil", "Storm", "Saffron", "Vermilion", "Dior", "Breeze", "Blue", "Satordi", 
                            "Haze", "Heath", "March", "Air", "Ridge", "Burr", "Tiger", "Onyx", "Titian", "Hawk", "Rock", "Leaf", "Colt", "Jasper", "Winter", "Buck", "Drake", "Sky"]
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
