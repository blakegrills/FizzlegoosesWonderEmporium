import random
import TreasureGenerator
def Humanoid(cr, name = None, classNames = None) :
    #Name, Type and location block
    details = ""
    size = "medium"
    diceNum = 1
    subType = ""
    num = random.randrange(1, 11, 1)
    sex = random.randrange(0, 2, 1)
    humanMale=["Alis","Sagramour","Sagremor","Tentagil","Pelleas","Gurgalan","Cnidel","Carrado","Llacheu","Nantres","Griffyth","Dagonet","Anguysh","Tristian","Tristan","Gringolet","Daguenet","Gawain","Houdain","Anir","Ektor","Pellam","Albion","Mabuz","Uriens","Camelon","Brehus","Bertram","Escalibor","Amr","Dinadan","Lludd","Tor","Guivret","Petrus","Cafall","Bryan","Clamedeus","Melyon","Percival","Evrain","Bersules","Breuse","Antfortas","Melechan","Florence","Evadeam","Lohengrin","Laudegrance","Ector","Melwas","Froille","Bernlak","Drudwyn","Cadwallon","Gais","Launcelot","Mabonaqain","Pellinore","Lueius","Morholt","Girflet","Cacamwri","Caerleon","Meleagant","Urien","Lancelot","Goveniayle","Aglarale","Dristan","Royns","Ryons","Maldue","Ysbaddaden","Borre","Bors","Balin","Peredwus","Pant","Calibum","Gaheris","Octha","Calibor","Palamedes","Ither","Leodegraunce","Parsifal","Che","Griffith","Cai","Lucan","Catterick","Glais","Galatyn","Gareth","Cus","Loe","Bedwyr","Rion","Camlann","Feirefiz","Nentres","Merlin","Alixandre","Bercilak","Ryence","Lamorak","Alexandre","Agravain","Taliesin","Escanor","Engres","Caw","Aglaral","Kei","Baldulf","Bicoir","Brandelis","Benoyce","Owain","Bellangere","Bagdemagus","Trevrizent","Kanelinqes","Tristram","Accalon","Bedver","Gorre","Cador","Apollo","Morold","Balen","Bliant","Avalloc","Isdemus","Arthgallo","Mabon","MorganTud","Meliodas","Tristen","Awarnach"]
    humanFemale=["Lynette","Lunet","Morgana","Angharad","Gwendolen","Ygeme","Lausanne","Ragnall","Gwendoloena","Enite","Viviane","Lysanor","Morgawse","Ettard","Chelinda","Lynessa","Nyneve","Igraine","Grainne","Margawse","Clarissant","Nimue","Lynnette","Kay","Lyonet","Astolat","Gwenhwyfach","Ade","Matilda","Ysolde","Albiona","Condwiramurs","Branwen","Igrayne","Herzeloyde","Shalott","Elayne","Avalon","Avilon","Angharat","Graine","Acheflow","Ganieda","Sebille","Modron","Avarona","Elizabeth","Cotovatre","Guanhumora","Igerne","Isoude","Pridwyn","Llamrei","Bedegrayne","Guenevere","Lyonors","Isoud","Nineve","Avaron","Morcades","Orguelleuse","Chelinde","Jenifer","Soredamors","Lynne","Gwenevere","Argante","Iblis","Creiddyladl","Elsa","Belakane","Anglides","Enid","Cundrie","Sigune","Lyonesse","Wenhaver","Ygraine","Gvenour","Lynet"]
    dwarfMale=["Thengel","Ethelward","Baldor","Gamling","Éomund","Wald","Dunsig","Baldmund","Leofdag","Hild","Eorl","Frumgar","Baldwig","Edgar","Fréaláf","Aldor","Wigbald","Elfbert","Celmund","Fréawine","Elfgar","Tirwald","Eofor","Adwine","Fastwine","Gladwine","Grimwine","Cenhelm","Wulf","Cadda","Garwine","Folca","Gríma","Eforhild","Léod","Adwig","Bertric","Dunstan","Aldwine","Elfswith","Théodred","Ethelred","Háma","Leofric","Baldhelm","Elfwine","Hereward","Eothain","Ordred","Hildred","Dernhelm","Sewine","Folcwine","Hefric","Tordag","Grimmund","Dunwine","Britta","Goldwine","Brego","Elfstan","Ordlac","Dunhere","Ethelfrith","Frithdag","Fréa","Ardwulf","Deorwine","Hulac","Elfred","Fengel","Baldric","Edbert","Ordstan","Elfhelm","Torfrith","Éomer","Leofwine","Fram","Baldwine","Baldred","Déor","Cenric","Wulfstan","Folcred","Gram","Leofstan","Dungar"]
    dwarfFemale=["Runfled","Merewyn","Cwendar","Ethelfled","Mereliss","Estwyn","Laywyn","Trewyn","Garfled","Ides","Darwise","Gledhild","Elfhild","Engifu","Saulwyn","Dawyn","Layfled","Elfwise","Sorgifu","Shadufled","Shadugifu","Edhild","Estswith","Cynegith","Godliss","Leofled","Frithild","Estrun","Sunnfled","Eowyn","Godswith","Cwenswith","Swetelayu","Trewred","Leofgifu","Bledwyn","Aldwyn","Meregith","Cynered","Sigeburga","Meregifu","Shaduwyn","Sigewyn","Mildgith","Trewfled","Olfete","Sweterun","Burnhild","Saulred","Trewhild","Dargifu","Dawfled","Lisswyn","Sigerun","Sunnwyn","Merthgifu","Eafled","Théodburga","Sunngifu","Darfled","Merthgith","Merefled","Rosefled","Swetefled","Hild","Adgith","Sorrun","Elfgifu","Darwyn","Aldgith","Brunhild","Cynewise","Bledgifu","Théodrun","Swetewyn","Cwenhild","Wilfled","Brunwyn","Lissgifu","Trewrun","Sorwyn","Cynewyn","Estmund","Wilrun","Mildwyn","Runwyn","Burnwyn","Runwise","Eawyn","Théodwyn","Cynefled","Runhild"]
    elfMale=["Melin","Maethorion","Loegon","Erthorion","Lamaendir","Galben","Caraphindaer","Hababen","Lossion","Lithuichon","Fardaer","Gwathrenor","Beltor","Mahtar","Triwathon","Pegion","Merethor","Nasar","Falchion","Anglaeg","Guldurchon","Gilher","Lanchion","Gawon","Rhovanion","Vahaiya","Rhodor","Glothroch","Eithruin","Fonion","Ialon","Istuion","Nemiron","Tatharben","Losdir","Haradaer","Carastar","Corudor","Colfind","Haeronor","Borniphen","Pelinelben","Ýridhremen","Arasdir","Cidinnanc","Goston","Annor","Foron","Graw","Véra","Mercion","Aglareb","Gilon","Thendaer","Amlugreg","Agarvorn","Rosgon","Forvenor","Vilwarindil","Estoladion","Arrad","Téro","Gwaew","Ereg","Tavorion","Solcthor","Mêr","Dúvemen","Glirdaer","Candir","Luinor","Haerion","Húrdaer","Bregiamlug","Amlugelu","Rúseaserco","Mélo","Dírion","Caldir","Noruiben","Calaear","Golloron","Lónaer","Miluichanar","Iamben","Ianudor","Thanben","Carachon","Lindo","Gelion","Amlugidinn","Deldhimben","Lanwatan","Geruilher","Ordaer","Deldhichon","Yalúmion","Faucion","Glîr","Culinion","Alasailion","Írchanar","Glavroldor","Tirrion","Mallen","Narchorion","Círchon","Gollben","Gaear","Rehtar","Lalphen","Thondor","Huirocco","Arraben","Gemmon","Beleg","Airehíse","Lennion","Paran","Gorthasser","Egnastor","Northor","Caelebamlug","Wahaiya","Amlugalen","Esgaron","Mithrildir","Aegon","Glamrendir","Amathluin","Núrchanar","Limmon","Echadrion","Badhroc","Amarion","Badhron","Helegnaer","Úhaeldor","Bregeben","Mindonor","Ianaer","Nídthor","Amlugorhal","Elben","Maeasdir","Lírdir","Vailimo","Sarna","Mindomen","Úfanweo","Thôn","Fannon","Einior","Amartharn","Lostor","Lámino","Ídhrion","Avornamdir","Cúvallorn","Lastoron","Gondir","Fanion","Nullion","Hethuon","Baradhroch","Faenor","Meldaer","Cabrion","Mastaro","Eldamanar","Ilvanion","Rivalchon","Quildolorion","Delgarathor","Faun","Abladon","Alfirin","Lusto","Thurilosmben","Rawon","Glasdaer","Nirophen","Herenion","Vea","Ríndir","Lusta","Aramdir","Bothion","Tumna","Hataltamo","Rátaro","Parthanar","Tyelpenasse","Hwestaer","Ríchon","Lesben","Bregol","Faerveren","Duirrochon"]
    elfFemale=["Istuiwen","Com","Alphien","Norgalaben","Thîn","Canben","Haered","Morphen","Amdirnith","Seriel","Calimiel","Berioriel","Methen","Caildis","Halyare","Emlineth","Inu","Peleccotan","Súlthel","Amdirthog","Laurealassie","Faimben","Nirwen","Celeben","Melui","Amdirand","Ladien","Duinen","Thíndes","Aderthriel","Olthel","Path","Eregien","Rýthil","Esgalwathiel","Fonthel","Alagiel","Cannamdir","Aerdis","Dogneth","Cullasdis","Amarthelien","Úhaelbes","Caelnith","Gwaereneth","Farhel","Braigiel","Ladrengilthel","Fimdes","Rivaltsel","Tultar","Gwache","Gwaedhneth","Uthaessel","Romben","Crabandis","Deldhindis","Nodwen","Gorogel","Boghel","Gorien","Taine","Emlinil","Gruithoriel","Dinalagosbes","Arndis","Caraphinnith","Fasdes","Erebeth","Húbes","Naernith","Lachel","Heledirthel","Amrúmben","Emethil","Gronniel","Amdiradan","Maedes","Forveniel","Lithuinith","Pathwen","Glessil","Culde","Gernith","Istien","Ruhtariel","Methenien","Daenes","Derenil","Amluglagor","Cadwareth","Tong","Amdirbarad","Gwaengwen","Glavrol","Filegeth","Lúthel","Ólerydes","Amathwaen","Úhaeleth","Partphen","Ungoleth","Calarien","Haeromes","Telde","Gwanniel","Caranith","Gelessil","Goe","Húben","Hedlethil","Háliel","Hostnith","Quentare","Calad","Gweluthel","Balliniel","Lámina","Mánie","Auþa","Nindes","Dúvengwen","Norniel","Yaimie","Brasseneth","Nadhordis","Boldes","Glohel","Cúchador","Glordis","Ethir","Nagor","Aica","Túghel","Valda","Logwen","Iphambes","Iachneth","Lóteriel","Pegnis","Míþiel","Faeniel","Eruneth","Thernil","Calphel","Randur","Hall","Lótealoxe","Berenthel","Aithel","Erynith","Edwendes","Níndis","Amrúmes","Gwilwilethel","Thangurbes","Cidinnanc","Raegwen","Alate","Dineniel","Tundis","Cíwneth","Falver","Achaspen","Lhaethel","Dereth","Adasser","Ehereg","Gorogien","Gawabes","Salab","Corchel","Nesser","Thíniel","Iphangwen","Ethirhel","Maethes","Andamundandil","Nerythiril","Caenith","Laegiel","Gorvel","Calithil","Húlel","Roitar","Rust","Lindangandie","Eredthel","Solcphen","Lomel","Conien","Gwingnith","Rhossolaspen","Riellendur","Magolneth","Tatharthel","Hithuneth","Laerguliel"]
    gnomeMale=["Largo","Merimas","Wilibald","Gardner","Hogg","Reginard","Bolger","Déagol","Hildigard","Marcho","Brandagamba","Headstrong","Galpsi","Carl","Hayward","Noakes","Flambard","Hlothran","Falco","Meriadoc","Proudfoot","Isembold","Stoor","Goldworthy","Diggle","RiverFolk","Hildifons","Goodchild","Bandobras","Hob","Fastred","Goodbody","Underhill","Marmadas","Tolman","Bucca","Togo","Sackville","Madoc","Blanco","Frodo","Brandybuck","Oldbuck","Hending","Fosco","Puddifoot","Goodenough","Gamgee","Ilberic","Merimac","Labingi","Isembard","Took","Harfoot","Hamson","Halfred","Goold","Bophîn","Ponto","Brown","Galbasi","Tûk","Gamwich","Ferdinand","Gorbulas","Maggot","Rufus","Andwise","Moro","Daddy","Isumbras","Dudo","Merry","Dinodas","Tobold","Odovacar","Robin","Sandyman","Adelard","Cottar","Seredic","Gawkroger","Jolly","Longo","Pippin","Elfstan","Banks","Cotman","Townsend","Faramir","Everard","Halfast","Smallburrow","Mugwort","Rumble","Sméagol","Hobson","Whitfoot","Bob","Odo","Hildibrand","Tunnelly","Butcher","Lotho","Brockhouse","Sancho","Lightfoot","Fredegar","Minto","North-Tooks","Farmer","Fallohide","Ted","Otho","Bowman","Holfast","Rudigar","Ferdibrand","Bilbo","Filibert"]
    gnomeFemale=["Galpsi","Amaranth","Angelica","Lightfoot","Boffin","Bracegirdle","Gardner","Chubb-Baggins","Roper","Hlothran","North-Tooks","Bolger","Goldilocks","Drogo","Burrowes","Esmeralda","Fíriel","Pott","Dora","Rosamunda","Laura","Townsend","Mugwort","Brockhouse","Celandine","Tanta","Lobelia","Twofoot","Daisy","Menegilda","Tûk","Saradoc","Noakes","Primula","Pimpernel","Brownlock","Malva","Longholes","Burrows","Greenhand","Hugo","Hilda","Lily","Goold","Gammidge","Linda","Lalia","Mentha","Fallohide","Hogg","Gamwich","Fairbairn","Prisca","Hayward","Goodbody","Goldworthy","Labingi","Brandybuck","Hanna","Donnamira","Pansy","Mimosa","Took","Gorhendad","Sandheaver","Melilot","Goodenough","Zaragamba","Whitfoot","Mirabella","Brandagamba","Bophîn","May","Rose","Baggins","Bell","Estella","Stoor","Bungo","Brown","Smallburrow","Butcher","Clayhanger","Eglantine","RiverFolk","Sandyman","Harfoot","Proudfoot","Salvia","Bunce","Grubb","Camellia","Asphodel","Cotton","Primrose","Maggot","Banks","Belladonna","Hornblower","Rumble","Rowan","Gilly","Puddifoot","Belba","Oldbuck","Pearl","Gawkroger","Berylla"]
    orcish=["Snagagûl","Gûlghâsh","Snagabúrz","Dugbúrz","Asholog","Urukbúrz","Globuk","Bagronk","Ologbúrz","Gûlbúbhosh","Búbhoshum","Ghâshbúrz","Gûlburzum","Pushdug","Snagaburzum","Snagasharkû","Sharkû","Snagaghâsh","Burzum","Ashuruk","Tamruzîr","Pharazbalak","Shakalbalak","Azrubêl","Shakalgimil","Ûrîthôr","Bawbuthôr","Balkazîr","Zâinabên","Aphanuzîr","Dôlguzagar","Avradizimir","Rôthzagar","Rôthzôr","Bêlzagar","Zimrupân","Pharazôn","Zimrathôn","Gimlibên","Gimilbalak","Abattârik","Nimrubên","Balkumagân","Azrubên","Dôlgubalak","Balakân","Sapthan","Shakalzôr","Shakalzagar","Avalôzîr","Gimilzôr","Nimruzîr","Arnubalkân","Gimlân","Karbazîr","Arnubên","Rôthbalak","Nilûbên","Gimilzagar","Abrazîr","Azrugimil","Rôthpharaz","Tarîkmagân","Azruzôr","Arnuzîr","Azulzîr","Îrpân","Azruzagar","Shakalpharaz","Avalôbên","Azrubalak","Azrupharaz","Aglarân","Zôrzagar","Adûnabêl","Rôthgimil","Sakalthôr","Tamrubên"]
    if num == 1 :
        subType = "human"
        if name == None :
            if sex == 0 :
                name = humanMale[random.randrange(0, humanMale.__len__(), 1)]
                sex = "Male"
            else :
                name = humanFemale[random.randrange(0, humanFemale.__len__(), 1)]
                sex = "Female"
    elif num == 2 :
        subType = "dwarf"
        if name == None :
            if sex == 0 :
                name = dwarfMale[random.randrange(0, dwarfMale.__len__(), 1)]
                sex = "Male"
            else :
                name = dwarfFemale[random.randrange(0, dwarfFemale.__len__(), 1)]
                sex = "Female"
    elif num == 3 :
        subType = "gnome"
        size = "small"
        if name == None :
            if sex == 0 :
                name = gnomeMale[random.randrange(0, gnomeMale.__len__(), 1)]
                sex = "Male"
            else :
                name = gnomeFemale[random.randrange(0, gnomeFemale.__len__(), 1)]
                sex = "Female"
    elif num == 4 :
        subType = "elf"
        if name == None :
            if sex == 0 :
                name = elfMale[random.randrange(0, elfMale.__len__(), 1)]
                sex = "Male"
            else :
                name = elfFemale[random.randrange(0, elfFemale.__len__(), 1)]
                sex = "Female"
    elif num == 5 :
        subType = "orc"
        if name == None :
            if sex == 0 :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Male"
            else :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Female"
    elif num == 6 :
        subType = "half-orc"
        ranNum = random.randrange(0, 2, 1)
        if name == None :
            if sex == 0 :
                if ranNum == 0 :
                    name = humanMale[random.randrange(0, humanMale.__len__(), 1)]
                else :
                    name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Male"
            else :
                if ranNum == 0 :
                    name = humanFemale[random.randrange(0, humanFemale.__len__(), 1)]
                else :
                    name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Female"
    elif num == 7 :
        subType = "half-elf"
        ranNum = random.randrange(0, 2, 1)
        if name == None :
            if sex == 0 :
                if ranNum == 0 :
                    name = humanMale[random.randrange(0, humanMale.__len__(), 1)]
                else :
                    name = elfMale[random.randrange(0, elfMale.__len__(), 1)]
                sex = "Male"
            else :
                if ranNum == 0 :
                    name = humanFemale[random.randrange(0, humanFemale.__len__(), 1)]
                else :
                    name = elfFemale[random.randrange(0, elfFemale.__len__(), 1)]
                sex = "Female"
    elif num == 8 :
        subType = "goblin"
        size = "small"
        if name == None :
            if sex == 0 :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Male"
            else :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Female"
    elif num == 9 :
        subType = "lizardfolk"
        if name == None :
            if sex == 0 :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Male"
            else :
                name = orcish[random.randrange(0, orcish.__len__(), 1)]
                sex = "Female"
    else :
        subType = "changling"
        if name == None :
            if sex == 0 :
                name = humanMale[random.randrange(0, humanMale.__len__(), 1)]
                sex = "Male"
            else :
                name = humanFemale[random.randrange(0, humanFemale.__len__(), 1)]
                sex = "Female"

    details = "%s%s%s%s%s%s%s" % (name, "\nHumanoid(", subType, ")\n", "sex: ", sex, "\n")
    details = "%s%s%s%s%s%s%s%s" % (details, "CR: ", cr, "\n", "size: ", size, "\n", "--------------------------------------------\n")
    
    if classNames == None :
        classNames = ["Guard", "Professional", "Assassin", "Rogue", "Priest", "Fighter", "Noble", "Slave", "Mage", "Military", "Merchant"]
    npcClass = classNames[random.randrange(0, classNames.__len__(), 1)]
    if npcClass == "Guard" :
        #Stat Block
        strength = 12 + int(cr*.15)
        dexterity = 12 + int(cr*.15)
        constitution = 10 + int(cr*.2)
        intelligence = 10 + int(cr*.15)
        wisdom = 10 + int(cr*.2)
        charisma = 10 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.5)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s" % ("Perception ", cr + 3 + (int((wisdom-10)/2)), "\nIntimidate ", cr + 3 + (int((charisma-10)/2)), "\nKnowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Professional" :
        profession = ["farmer", "hunter", "fisherman", "sailor", "Jeweller", "Mason", "Smith", "Musician", "Prostitute", "Sculptor", "Painter", "Skald", "Medicine"]
        holder = profession[random.randrange(0, profession.__len__(), 1)]
        npcClass = "%s%s%s%s" % (npcClass, "(", holder, ")")
        #Stat Block
        strength = 10 + int(cr*.15)
        dexterity = 10 + int(cr*.15)
        constitution = 10 + int(cr*.15)
        intelligence = 12 + int(cr*.2)
        wisdom = 12 + int(cr*.2)
        charisma = 10 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(2, 5, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.25)
        fortitude = int(cr*.333) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s" % ("Appraise ", cr + 3 + (int((intelligence-10)/2)), "\nBluff ", cr + 3 + (int((charisma-10)/2)), "\nProfession(", holder, ")", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Assassin" :
        #Stat Block
        strength = 12 + int(cr*.15)
        dexterity = 14 + int(cr*.15)
        constitution = 10 + int(cr*.2)
        intelligence = 12 + int(cr*.15)
        wisdom = 12 + int(cr*.2)
        charisma = 12 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.75)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.666) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % ("Appraise ", cr + 3 + (int((intelligence-10)/2)), "\nAcrobatics ", cr + 3 + (int((dexterity-10)/2)), "\nDisable Device ", cr + 3 + (int((dexterity-10)/2)), "\nStealth ", cr + 3 + (int((dexterity-10)/2)), "\nBluff ", cr + 3 + (int((charisma-10)/2)), "\nProfession(poisonmaking)", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Rogue" :
        #Stat Block
        strength = 10 + int(cr*.15)
        dexterity = 12 + int(cr*.15)
        constitution = 10 + int(cr*.2)
        intelligence = 12 + int(cr*.15)
        wisdom = 10 + int(cr*.2)
        charisma = 10 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.5)
        fortitude = int(cr*.333) + (int((constitution-10)/2))
        reflex = int(cr*.666) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % ("Appraise ", cr + 3 + (int((intelligence-10)/2)), "\nAcrobatics ", cr + 3 + (int((dexterity-10)/2)), "\nDisable Device ", cr + 3 + (int((dexterity-10)/2)), "\nStealth ", cr + 3 + (int((dexterity-10)/2)), "\nBluff ", cr + 3 + (int((charisma-10)/2)), "Knowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Priest" :
        #Stat Block
        strength = 10 + int(cr*.15)
        dexterity = 10 + int(cr*.15)
        constitution = 10 + int(cr*.15)
        intelligence = 10 + int(cr*.15)
        wisdom = 14 + int(cr*.25)
        charisma = 10 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.25)
        fortitude = int(cr*.333) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.666) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s" % ("Knowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Religion) ", cr + 3 + (int((intelligence-10)/2)), "\nSpellcraft ", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Fighter" :
        #Stat Block
        strength = 12 + int(cr*.2)
        dexterity = 12 + int(cr*.2)
        constitution = 12 + int(cr*.2)
        intelligence = 10 + int(cr*.1)
        wisdom = 10 + int(cr*.1)
        charisma = 10 + int(cr*.1)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(5, 7, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*1)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s" % ("Animal Handling ", cr + 3 + (int((wisdom-10)/2)), "\nIntimidate ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Noble" :
        #Stat Block
        strength = 10 + int(cr*.15)
        dexterity = 10 + int(cr*.15)
        constitution = 10 + int(cr*.15)
        intelligence = 12 + int(cr*.2)
        wisdom = 10 + int(cr*.15)
        charisma = 12 + int(cr*.2)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(2, 5, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.5)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.666) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s" % ("Bluff ", cr + 3 + (int((charisma-10)/2)), "\nDiplomacy ", cr + 3 + (int((charisma-10)/2)), "\nKnowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Slave" :
        #Stat Block
        strength = 10 + int(cr*0)
        dexterity = 10 + int(cr*0)
        constitution = 8 + int(cr*0)
        intelligence = 8 + int(cr*0)
        wisdom = 10 + int(cr*.1)
        charisma = 10 + int(cr*0)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(2, 5, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.25)
        fortitude = int(cr*.333) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s" % ("Profession(slave) ", cr + 3 + (int((wisdom-10)/2)), "\nKnowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Mage" :
        #Stat Block
        strength = 8 + int(cr*.1)
        dexterity = 10 + int(cr*.1)
        constitution = 8 + int(cr*.1)
        intelligence = 14 + int(cr*.25)
        wisdom = 12 + int(cr*.1)
        charisma = 12 + int(cr*.2)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(2, 5, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.25)
        fortitude = int(cr*.333) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.666) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s%s%s" % ("Knowledge(Planes) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(History) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Arcane) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nLinguistics ", cr + 3 + (int((intelligence-10)/2)), "\nSpellcraft ", cr + 3 + (int((intelligence-10)/2)), "\n--------------------------------------------\n")

    if npcClass == "Military" :
        if cr < 10 :
            positionList = ["Infantry", "Archer", "Siege Engineer"]
            npcClass = "%s%s%s%s" % (npcClass, "(", positionList[random.randrange(0, positionList.__len__(), 1)], ")")
            if npcClass == "Military(Infantry)" :
                #Stat Block
                strength = 12 + int(cr*.2)
                dexterity = 10 + int(cr*.1)
                constitution = 12 + int(cr*.2)
                intelligence = 10 + int(cr*.1)
                wisdom = 10 + int(cr*.2)
                charisma = 10 + int(cr*.1)
                skills = "%s%s%s%s%s" % ("knowledge(history) ", cr + 3 + (int((intelligence-10)/2)), "\nProfession(Infantry) ", cr + 3 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
            elif npcClass == "Military(Archer)" :
                #Stat Block
                strength = 10 + int(cr*.1)
                dexterity = 14 + int(cr*.25)
                constitution = 10 + int(cr*.1)
                intelligence = 10 + int(cr*.1)
                wisdom = 10 + int(cr*.15)
                charisma = 10 + int(cr*.1)
                skills = "%s%s%s%s%s" % ("knowledge(history) ", cr + 3 + (int((intelligence-10)/2)), "\nProfession(Archer) ", cr + 3 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
            else :
                #Stat Block
                strength = 10 + int(cr*.1)
                dexterity = 10 + int(cr*.1)
                constitution = 10 + int(cr*.2)
                intelligence = 12 + int(cr*.15)
                wisdom = 14 + int(cr*.25)
                charisma = 10 + int(cr*.15)
                skills = "%s%s%s%s%s" % ("knowledge(history) ", cr + 3 + (int((intelligence-10)/2)), "\nProfession(siege) ", cr + 3 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
        elif cr < 15 :
            positionList = ["Infantry Commander", "Knight", "Siege Commander"]
            npcClass = "%s%s%s%s" % (npcClass, "(", positionList[random.randrange(0, positionList.__len__(), 1)], ")")
            if npcClass == "Military(Infantry Commander)" :
                #Stat Block
                strength = 14 + int(cr*.15)
                dexterity = 12 + int(cr*.15)
                constitution = 12 + int(cr*.2)
                intelligence = 10 + int(cr*.15)
                wisdom = 12 + int(cr*.25)
                charisma = 10 + int(cr*.15)
                skills = "%s%s%s%s%s%s%s%s%s" % ("Ride ", cr + 3 + (int((wisdom-10)/2)), "\nknowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nknowledge(history) ", cr + 5 + (int((intelligence-10)/2)), "\nProfession(Infantry) ", cr + 8 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
            elif npcClass == "Military(Knight)" :
                #Stat Block
                strength = 14 + int(cr*.2)
                dexterity = 10 + int(cr*.1)
                constitution = 12 + int(cr*.2)
                intelligence = 10 + int(cr*.15)
                wisdom = 12 + int(cr*.25)
                charisma = 12 + int(cr*.15)
                skills = "%s%s%s%s%s%s%s%s%s" % ("Ride ", cr + 8 + (int((wisdom-10)/2)), "\nknowledge(Nobility) ", cr + 8 + (int((intelligence-10)/2)), "\nknowledge(history) ", cr + 3 + (int((intelligence-10)/2)), "\nProfession(Knight) ", cr + 5 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
            else :
                #Stat Block
                strength = 10 + int(cr*.1)
                dexterity = 10 + int(cr*.1)
                constitution = 10 + int(cr*.2)
                intelligence = 12 + int(cr*.15)
                wisdom = 14 + int(cr*.25)
                charisma = 10 + int(cr*.15)
                skills = "%s%s%s%s%s%s%s%s%s" % ("Ride ", cr + 3 + (int((wisdom-10)/2)), "\nknowledge(Engineering) ", cr + 8 + (int((intelligence-10)/2)), "\nknowledge(history) ", cr + 3 + (int((intelligence-10)/2)), "\nProfession(Siege) ", cr + 8 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")
        else :
            npcClass = "%s%s" % (npcClass, "(General)")
            #Stat Block
            strength = 12 + int(cr*.15)
            dexterity = 10 + int(cr*.1)
            constitution = 12 + int(cr*.2)
            intelligence = 12 + int(cr*.15)
            wisdom = 14 + int(cr*.25)
            charisma = 14 + int(cr*.15)
            skills = "%s%s%s%s%s%s%s%s%s" % ("Ride ", cr + 3 + (int((wisdom-10)/2)), "\nknowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nknowledge(history) ", cr + 8 + (int((intelligence-10)/2)), "\nProfession(General) ", cr + 8 + (int((wisdom-10)/2)), "\n--------------------------------------------\n")

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.75)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

    if npcClass == "Merchant" :
        #Stat Block
        strength = 12 + int(cr*.15)
        dexterity = 12 + int(cr*.15)
        constitution = 10 + int(cr*.2)
        intelligence = 10 + int(cr*.15)
        wisdom = 10 + int(cr*.2)
        charisma = 10 + int(cr*.15)

        if subType == "human" :
            strength = strength + 2
        elif subType == "dwarf" :
            constitution = constitution + 2
            charisma = charisma - 2
        elif subType == "gnome" :
            intelligence = intelligence + 2
            strength = strength - 2
        elif subType == "elf" :
            dexterity = dexterity + 2
            constitution = constitution - 2
        elif subType == "orc" :
            strength = strength + 4
            intelligence = intelligence - 2
        elif subType == "half-orc" :
            strength = strength + 2
        elif subType == "half-elf" :
            dexterity = dexterity + 2
        elif subType == "goblin" :
            dexterity = dexterity + 4
            charisma = charisma -2
        elif subType == "lizardfolk" :
            constitution = constitution + 4
            strength = strength + 2
            intelligence = intelligence - 3
        else :
            charisma = charisma + 2

        #d6(2,5) d8(4,6) d10(5,7)
        health = int((cr*random.randrange(4, 6, 1)) + (int((constitution-10)/2)*cr))
        baseAttack = int(cr*.5)
        fortitude = int(cr*.666) + (int((constitution-10)/2))
        reflex = int(cr*.333) + (int((dexterity-10)/2))
        will = int(cr*.333) + (int((wisdom-10)/2))

        skills = "%s%s%s%s%s%s%s%s%s%s%s" % ("Perception ", cr + 3 + (int((wisdom-10)/2)), "\nIntimidate ", cr + 3 + (int((charisma-10)/2)), "\nKnowledge(local) ", cr + 3 + (int((intelligence-10)/2)), "\nKnowledge(Nobility) ", cr + 3 + (int((intelligence-10)/2)), "\nSense Motive ", cr + 3 + (int((charisma-10)/2)), "\n--------------------------------------------\n")

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

    details = "%s%s%s%s%s%s%s%s%s%s%s%s" % (details, "Health: ", health, " Base Attack: ", baseAttack, " Fort: ", fortitude, " Ref: ", reflex, " Will: ", will, "\n--------------------------------------------\n")
    details = "%s%s%s%s%s%s%s%s" % (details, "Class: ", npcClass, "Melee attack modifier: ", (baseAttack + int((strength-10)/2)), "Ranged attack modifier: ", (baseAttack + int((dexterity-10)/2)), "\n--------------------------------------------\n")
    details = "%s%s%s" % (details, skills, "\n--------------------------------------------\n")

    wardrobeList = ["His wardrobe is severe, and is completely orange.", "His wardrobe is revealing.", "His wardrobe is attractive and mysterious, with a lot of purple.", "His wardrobe is professional.", "His wardrobe is elegant.", "His wardrobe is sexy, with a lot of black.", "His wardrobe is strange.", "His wardrobe is mysterious.", "His wardrobe is impractacal.", "His wardrobe is flattering, with a lot of purple.", "His wardrobe is businesslike.", "His wardrobe is dignified.", "His wardrobe is tight.", "His wardrobe is practical.", "His wardrobe is bizarre.", "His wardrobe is strange and risque, with a lot of green and white.", "His wardrobe is uncomplicated, with a lot of white and gray.", "His wardrobe is classy.", "His wardrobe is strange, with a lot of blue and white.", "His wardrobe is elaborate.", "His wardrobe is flattering.", "His wardrobe is risque, with a lot of green.", "His wardrobe is severe and attractive, with a completely red color scheme.", "His wardrobe is weird and risque, with a lot of black.", "His wardrobe is flattering, and is completely violet.", "His wardrobe is elegant and impractacal, with a lot of orange and white.", "His wardrobe is tight, with a lot of green and gray.", "His wardrobe is strange and sexy, with a lot of gray and red.", "His wardrobe is elegant and complicated, with a lot of white.", "His wardrobe is dignified, with a lot of blue.", "His wardrobe is plain, with a lot of green and violet.", "His wardrobe is uncomplicated and businesslike, with a lot of blue and white.", "His wardrobe is tight.", "His wardrobe is attractive, and is completely green and gray.", "His wardrobe is classy and sexy, with a mostly white and black color scheme.", "His wardrobe is no-nonsense and severe, with a lot of blue.", "His wardrobe is sexy and simple, with a lot of red.", "His wardrobe is sexy and simple, with a mostly violet color scheme.", "His wardrobe is strange.", "His wardrobe is professional and practical, with a lot of blue and white.", "His wardrobe is severe.", "His wardrobe is strange.", "His wardrobe is sexy, with a lot of blue and black.", "His wardrobe is unconventional.", "His wardrobe is practical and severe, with a mostly green and black color scheme.", "His wardrobe is classy and mysterious, with a lot of blue and white.", "His wardrobe is elaborate, with a lot of orange.", "His wardrobe is dignified.", "His wardrobe is risque.", "His wardrobe is severe.", "His wardrobe is unusual.", "His wardrobe is unusual.", "His wardrobe is severe, with a lot of red and brown.", "His wardrobe is flattering and strange, with a lot of green.", "His wardrobe is flattering, and is mostly white.", "His wardrobe is mysterious, and is mostly yellow and blue.", "His wardrobe is attractive.", "His wardrobe is unusual and revealing, with a mostly green and blue color scheme.", "His wardrobe is severe.", "His wardrobe is impractacal and revealing, with a completely black color scheme.", "His wardrobe is sexy, with a lot of orange.", "His wardrobe is classy.", "His wardrobe is unconventional.", "His wardrobe is classy.", "His wardrobe is classy and unusual, with a lot of orange.", "His wardrobe is impractacal, and is mostly black and purple.", "His wardrobe is risque.", "His wardrobe is risque and weird, with a lot of blue.", "His wardrobe is classy, and is completely green and black.", "His wardrobe is elegant, and is completely orange.", "His wardrobe is attractive and bizarre, with a lot of blue.", "His wardrobe is complicated and mysterious, with a lot of purple and gray.", "His wardrobe is elaborate and sexy, with a mostly purple color scheme.", "His wardrobe is businesslike, and is mostly brown.", "His wardrobe is utilitarian, with a lot of blue and yellow.", "His wardrobe is tight.", "His wardrobe is classy, and is completely black.", "His wardrobe is strange.", "His wardrobe is utilitarian and businesslike, with a completely red and orange color scheme.", "His wardrobe is complicated and risque, with a lot of blue.", "His wardrobe is classy and strange, with a mostly yellow color scheme.", "His wardrobe is practical and dignified, with a lot of blue.", "His wardrobe is strange and businesslike, with a mostly green color scheme.", "His wardrobe is classy and odd, with a mostly green and yellow color scheme.", "His wardrobe is elegant.", "His wardrobe is odd and tight, with a lot of black.", "His wardrobe is severe.", "His wardrobe is classy and mysterious, with a lot of white and orange.", "His wardrobe is odd.", "His wardrobe is tight, and is mostly white and green.", "His wardrobe is severe.", "His wardrobe is classy, with a lot of orange.", "His wardrobe is strange.", "His wardrobe is artistic and complicated, with a lot of yellow and red.", "His wardrobe is classy and elaborate, with a lot of brown.", "His wardrobe is artistic.", "His wardrobe is unusual.", "His wardrobe is weird.", "His wardrobe is no-nonsense and dignified, with a mostly white and violet color scheme.", "His wardrobe is unconventional and artistic, with a completely purple color scheme.", "His wardrobe is utilitarian, and is completely blue.", "His wardrobe is uncomplicated.", "His wardrobe is dignified.", "His wardrobe is artistic.", "His wardrobe is severe and plain, with a lot of black.", "His wardrobe is impractacal, and is completely green.", "His wardrobe is unusual.", "His wardrobe is flattering, and is completely blue and gray.", "His wardrobe is practical, and is mostly purple.", "His wardrobe is mysterious, with a lot of green.", "His wardrobe is flattering, and is completely green and yellow.", "His wardrobe is strange, with a lot of brown and red.", "His wardrobe is practical and severe, with a mostly yellow and blue color scheme.", "His wardrobe is complicated and artistic, with a lot of red and gray.", "His wardrobe is risque and utilitarian, with a lot of red and violet.", "His wardrobe is bizarre.", "His wardrobe is weird, with a lot of black and blue.", "His wardrobe is elaborate, with a lot of green.", "His wardrobe is businesslike and strange, with a lot of yellow.", "His wardrobe is revealing.", "His wardrobe is attractive, with a lot of green and gray.", "His wardrobe is elegant.", "His wardrobe is sexy.", "His wardrobe is sexy, with a lot of white and red.", "His wardrobe is professional and classy, with a completely black and gray color scheme.", "His wardrobe is plain and severe, with a lot of red and blue.", "His wardrobe is utilitarian, and is mostly orange.", "His wardrobe is sexy and weird, with a mostly green color scheme.", "His wardrobe is bizarre and flattering, with a lot of yellow.", "His wardrobe is revealing, with a lot of yellow.", "His wardrobe is bizarre and revealing, with a lot of blue and gray.", "His wardrobe is dignified.", "His wardrobe is uncomplicated and severe, with a lot of white and orange.", "His wardrobe is mysterious, and is completely red and gray.", "His wardrobe is mysterious and sexy, with a completely orange and brown color scheme.", "His wardrobe is mysterious, with a lot of green and gray.", "His wardrobe is elegant.", "His wardrobe is weird and revealing, with a lot of white and black.", "His wardrobe is risque, with a lot of violet and black.", "His wardrobe is risque and unusual, with a lot of blue and yellow.", "His wardrobe is revealing.", "His wardrobe is attractive and strange, with a mostly green color scheme.", "His wardrobe is elaborate and artistic, with a lot of gray and brown.", "His wardrobe is plain.", "His wardrobe is attractive and tight, with a lot of violet and blue.", "His wardrobe is odd and elegant, with a lot of gray and orange.", "His wardrobe is mysterious and artistic, with a lot of red and black.", "His wardrobe is dignified.", "His wardrobe is simple.", "His wardrobe is risque, with a lot of red.", "His wardrobe is utilitarian.", "His wardrobe is simple, with a lot of gray.", "His wardrobe is artistic and bizarre, with a completely red and purple color scheme.", "His wardrobe is practical.", "His wardrobe is elegant.", "His wardrobe is unusual.", "His wardrobe is severe.", "His wardrobe is uncomplicated.", "His wardrobe is risque and flattering, with a completely yellow color scheme.", "His wardrobe is tight and no-nonsense, with a completely yellow and red color scheme.", "His wardrobe is risque and simple, with a lot of red.", "His wardrobe is complicated and tight, with a lot of gray.", "His wardrobe is unconventional and artistic, with a lot of blue.", "His wardrobe is plain.", "His wardrobe is flattering, and is completely white and orange.", "His wardrobe is flattering, and is completely green.", "His wardrobe is tight.", "His wardrobe is mysterious and tight, with a mostly gray color scheme.", "His wardrobe is classy.", "His wardrobe is sexy and practical, with a completely brown color scheme.", "His wardrobe is sexy, and is completely white.", "His wardrobe is elaborate.", "His wardrobe is uncomplicated.", "His wardrobe is professional.", "His wardrobe is odd and unusual, with a lot of purple and black.", "His wardrobe is revealing and elegant, with a mostly red and yellow color scheme.", "His wardrobe is elegant and revealing, with a completely red and white color scheme.", "His wardrobe is revealing and weird, with a lot of orange and red.", "His wardrobe is professional and plain, with a completely green color scheme.", "His wardrobe is sexy.", "His wardrobe is strange.", "His wardrobe is simple, and is completely blue and yellow.", "His wardrobe is risque and unusual, with a mostly yellow color scheme.", "His wardrobe is sexy.", "His wardrobe is severe.", "His wardrobe is artistic and tight, with a lot of blue.", "His wardrobe is uncomplicated and businesslike, with a lot of black and white.", "His wardrobe is uncomplicated.", "His wardrobe is attractive and mysterious, with a lot of red.", "His wardrobe is unusual, and is mostly blue and white.", "His wardrobe is mysterious, and is mostly black and red.", "His wardrobe is classy and tight, with a mostly blue and yellow color scheme.", "His wardrobe is elaborate, with a lot of green.", "His wardrobe is no-nonsense.", "His wardrobe is mysterious and risque, with a lot of yellow and blue.", "His wardrobe is sexy.", "His wardrobe is severe.", "His wardrobe is odd and risque, with a completely white color scheme.", "His wardrobe is attractive and mysterious, with a mostly gray and brown color scheme.", "His wardrobe is artistic, and is mostly green and gray."]
    eyeList = ["He has round gray eyes that are like two pools of mercury.", "He has deep-set chestnut eyes.", "This aloof guy has large gunmetal-gray eyes.", "He has beady eyes the color of burnished iron.", "He has almond-shaped purple eyes that are like two windows on the evening sky.", "He has deep-set blue eyes that are like two lagoons.", "He has slitted blue eyes that are like two chunks of lapis lazuli.", "He has large eyes the color of an overcast sky.", "This harried guy has droopy chocolate-colored eyes.", "This innocent man has slitted coffee-colored eyes.", "This greedy man has round eyes the color of blooming violets.", "This clever guy has beady gray eyes that are like two silver coins.", "He has beady eyes the color of varnished wood.", "He has hooded aquamarine eyes.", "He has almond-shaped blue eyes that are like two pools of water.", "He has narrow eyes the color of the afternoon sky.", "This personable gentleman has round lavender eyes.", "This brave gentleman has slanted turquoise eyes.", "This tense man has hooded gray eyes that are like two windows looking out on an overcast sky.", "This seductive gentleman has deep-set blue eyes.", "He has hooded brown eyes that are like two acorns.", "This thoughtful man has almond-shaped eyes the color of cold ashes.", "This wild guy has large purple eyes that are like two amethysts.", "He has almond-shaped blue eyes.", "He has slanted eyes the color of coffee with cream.", "He has deep-set brown eyes that are like two tiger-eye gems.", "This peaceful gentleman has hooded brown eyes.", "This enthusiastic man has droopy gray eyes.", "He has slanted sky-blue eyes.", "He has almond-shaped gray eyes that are like two silver coins.", "He has wide brown eyes that are like two acorns.", "This cruel guy has large gray eyes that are like two pools of mercury.", "He has slanted chocolate-colored eyes.", "This mysterious man has beady gray eyes that are like two pools of mercury.", "He has deep-set brown eyes that are like two drops of chocolate.", "This studious gentleman has large blue eyes.", "This aloof gentleman has almond-shaped eyes the color of burnished iron.", "He has almond-shaped gray eyes that are like two pieces of steel.", "This humorous gentleman has droopy brown eyes that are like two bronze coins.", "He has large gray eyes that are like two pools of mercury.", "He has round brown eyes that are like two drops of chocolate.", "This aristocratic gentleman has narrow black eyes.", "He has slanted purple eyes that are like two amethysts.", "This spiritual man has beady eyes the color of fine silver.", "He has wide brown eyes.", "He has slanted blue eyes that are like two sapphires.", "This seductive gentleman has slitted brown eyes that are like two bronze coins.", "He has beady gunmetal-gray eyes.", "This cunning guy has droopy eyes the color of milk chocolate.", "This sinful guy has wide eyes the color of black coffee.", "This harried man has almond-shaped green eyes that are like two clumps of moss.", "This trusting man has wide brown eyes that are like two bronze coins.", "He has slanted gray eyes.", "This intimidating guy has slanted blue eyes that are like two turquoises.", "He has droopy eyes the color of chestnuts.", "He has large eyes the color of amethysts.", "This noble gentleman has wide green eyes that are like two pools of stangant water.", "He has large eyes the color of an overcast sky.", "He has slitted chestnut eyes.", "This noble gentleman has large blue eyes that are like two chunks of lapis lazuli.", "He has beady black eyes that are like two dark pits.", "This serene guy has beady brown eyes that are like two tiger-eye gems.", "This cruel guy has slanted emerald eyes.", "This courageous guy has round brown eyes that are like two drops of chocolate.", "This thoughtful guy has deep-set ash-gray eyes.", "He has round blue eyes that are like two pools of water.", "This personable man has droopy blue eyes that are like two sapphires.", "He has large eyes the color of the midnight sky.", "This clever gentleman has wide gray eyes that are like two pieces of steel.", "This misguided guy has droopy blue eyes.", "He has narrow gray eyes that are like two pools of mercury.", "He has beady eyes the color of dark chocolate.", "He has slanted brown eyes that are like two bronze coins.", "This clever guy has round gray eyes that are like two windows looking out on an overcast sky.", "He has droopy amethyst eyes.", "He has slanted eyes the color of blueberries.", "This intimidating guy has wide chestnut eyes.", "He has narrow brown eyes that are like two discs of wood.", "He has slitted black eyes.", "He has beady brown eyes.", "He has slitted coffee-colored eyes.", "This courageous guy has slitted purple eyes.", "He has round gray eyes that are like two pieces of steel.", "He has wide eyes the color of burnished iron.", "This wily gentleman has slanted gray eyes that are like two silver coins.", "This boorish gentleman has large eyes the color of turquoises.", "He has droopy brown eyes that are like two bronze coins.", "This witty man has almond-shaped eyes the color of burnished iron.", "He has almond-shaped brown eyes that are like two drops of chocolate.", "He has slitted eyes the color of fresh green apples.", "He has slanted eyes the color of chestnuts.", "He has beady brown eyes that are like two splotches of mud.", "This trusting guy has hooded gray eyes.", "This solem man has almond-shaped brown eyes.", "He has droopy chocolate-colored eyes.", "This serious guy has hooded blue eyes.", "He has almond-shaped purple eyes that are like two amethysts.", "He has narrow brown eyes that are like two acorns.", "This vain guy has large brown eyes that are like two patches of dried blood.", "He has deep-set chestnut eyes.", "He has large gray eyes that are like two pieces of steel.", "This foul-mouthed guy has wide blue eyes that are like two sapphires.", "This confused gentleman has slitted gray eyes.", "He has round violet eyes that are like two drops of wine.", "He has hooded brown eyes that are like two drops of chocolate.", "He has beady gray eyes that are like two pools of mercury.", "He has beady purple eyes.", "He has narrow gray eyes.", "He has beady brown eyes that are like two bronze coins.", "He has wide brown eyes that are like two acorns.", "This antisocial gentleman has round chocolate-colored eyes.", "This sensitive gentleman has droopy purple eyes that are like two windows on the evening sky.", "This arrogant gentleman has slanted blue eyes that are like two chunks of lapis lazuli.", "This confident gentleman has slitted eyes the color of valuable emeralds.", "He has hooded brown eyes.", "This romantic man has round brown eyes that are like two patches of dried blood.", "He has slanted eyes the color of ripe plums.", "This vain gentleman has beady brown eyes that are like two acorns.", "This curious gentleman has round green eyes.", "He has droopy plum-colored eyes.", "He has deep-set blue eyes that are like two turquoises.", "He has beady eyes the color of chestnuts.", "This energetic gentleman has slitted slate-gray eyes.", "He has beady turquoise eyes.", "He has slitted gray eyes that are like two silver coins.", "He has slitted brown eyes that are like two discs of wood.", "This willfull guy has large gray eyes that are like two windows looking out on an overcast sky.", "This romantic man has droopy brown eyes that are like two acorns.", "This angry gentleman has round brown eyes.", "This mistrustful man has large eyes the color of blue tropical waters.", "He has hooded gray eyes that are like two silver coins.", "This energetic man has hooded brown eyes that are like two discs of wood.", "This silly gentleman has beady soot-black eyes.", "This antisocial gentleman has hooded blue eyes that are like two windows on the afternoon sky.", "This misguided guy has slitted brown eyes that are like two tiger-eye gems.", "This silly guy has narrow eyes the color of the evening sky.", "He has almond-shaped blue eyes that are like two windows on the afternoon sky.", "He has round blue eyes that are like two pools of water.", "This contemplative man has beady black eyes that are like two lumps of coal.", "This generous gentleman has deep-set blue eyes that are like two pools of water.", "This sneaky man has narrow gray eyes that are like two silver coins.", "He has beady brown eyes that are like two patches of dried blood.", "This angry guy has narrow black eyes.", "He has beady gray eyes that are like two pieces of steel.", "This studious guy has large brown eyes that are like two tiger-eye gems.", "He has slanted gray eyes that are like two pools of mercury.", "He has slitted eyes the color of an overcast sky.", "He has hooded green eyes.", "He has round gray eyes that are like two silver coins.", "This serious man has slitted sky-blue eyes.", "He has round blue eyes that are like two chunks of lapis lazuli.", "This cunning man has beady eyes the color of the midnight sky.", "He has narrow brown eyes that are like two splotches of mud.", "He has deep-set brown eyes that are like two bronze coins.", "He has deep-set black eyes.", "This sensual man has droopy eyes the color of varnished wood.", "This generous gentleman has hooded brown eyes that are like two discs of wood.", "He has wide blue eyes that are like two pools of water.", "This noble man has droopy brown eyes that are like two discs of wood.", "This laid-back guy has slitted beige eyes.", "He has hooded violet eyes that are like two amethysts.", "This noble man has large eyes the color of the afternoon sky.", "He has beady gray eyes that are like two pieces of steel.", "This angry guy has beady green eyes that are like two clumps of moss.", "He has deep-set blue eyes that are like two pools of water.", "This sinful gentleman has deep-set royal purple eyes.", "This brave guy has deep-set beige eyes.", "He has deep-set brown eyes.", "This determined guy has narrow violet eyes that are like two amethysts.", "This lazy guy has round brown eyes.", "This wordy gentleman has round brown eyes.", "This noble man has slanted gray eyes.", "This aloof gentleman has narrow cobalt-blue eyes.", "He has round purple eyes that are like two amethysts.", "He has slitted gray eyes that are like two pieces of steel.", "He has wide brown eyes.", "He has almond-shaped brown eyes that are like two drops of chocolate.", "This lonely guy has large brown eyes that are like two tiger-eye gems.", "He has large brown eyes.", "He has slitted blue eyes that are like two turquoises.", "This laid-back guy has large eyes the color of the midnight sky.", "This willfull man has narrow beige eyes.", "This energetic guy has droopy gray eyes that are like two silver coins.", "He has wide smoke-gray eyes.", "This silly guy has slitted eyes the color of ripe plums.", "He has narrow blue eyes that are like two chunks of lapis lazuli.", "He has slitted eyes the color of amethysts.", "He has round blue eyes that are like two chunks of lapis lazuli.", "He has large brown eyes.", "He has slitted green eyes that are like two clumps of moss.", "This spiritual man has almond-shaped brown eyes that are like two bronze coins.", "He has almond-shaped coffee-colored eyes.", "This wise gentleman has large chestnut eyes.", "He has beady blue eyes that are like two sapphires.", "He has large eyes the color of dark chocolate.", "He has hooded brown eyes.", "He has round blue eyes.", "This harried man has almond-shaped gray eyes that are like two windows looking out on an overcast sky.", "This wordy gentleman has hooded eyes the color of obsidian.", "This wise man has slanted gray eyes that are like two pools of mercury."]
    hairList = ["His fine, curly, yellow hair is worn in a style that reminds you of an overused mop.", "His thick, wavy, brown hair is worn in a style that reminds you of a horse's mane.", "He is bald, but used to have luxurious, straight, brown hair.", "His silky, straight, very long hair is the color of charcoal, and is worn in a simple, precise style.", "His fine, straight, gunmetal-gray hair is worn in a style that reminds you of a bale of hay.", "His thick, straight, brown hair is worn in a style that reminds you of a crown.", "His thick, straight, medium-length hair is the color of ripe lemons, and is worn in an artistic style.", "His silky, wavy, black hair is long and is worn in a practical, precise style.", "His fine, curly, black hair is worn in a style that reminds you of a porcupine's quills.", "His luxurious, curly, red hair is worn in a style that reminds you of a helmet.", "His fine, wavy, medium-length hair is the color of chestnuts, and is worn in a bizarre style.", "His silky, straight, brown hair is worn in a style that reminds you of a flowing stream.", "His silky, straight, ebony hair is very short and is worn in an attractive, exotic style.", "His thick, straight, shoulder-length hair is the color of dark chocolate, and is worn in an exotic style.", "His thick, straight, ebony hair is medium-length and is worn in an uncomplicated style.", "His silky, straight, sand-colored hair is worn in a style that reminds you of a wave of water.", "He is bald, but used to have silky, straight, soot-black hair.", "His thick, straight, brown hair is worn in a style that reminds you of a comet's trail.", "His thick, curly, brown hair is worn in a style that reminds you of a flowing cape.", "His thick, curly, chestnut hair is worn in a style that reminds you of a devil's horns.", "His luxurious, curly, medium-length hair is the color of charcoal, and is worn in an utilitarian style.", "His silky, curly, midnight black hair is worn in a style that reminds you of a horse's mane.", "His fine, straight, lemon-yellow hair is worn in a style that reminds you of a waterfall.", "He is bald, but used to have luxurious, straight, yellow hair.", "He is bald, but used to have silky, straight, ivory hair.", "His thick, straight, red hair is worn in a style that reminds you of a flowing cape.", "His silky, straight, short hair is the color of burnished iron, and is worn in a simple, dignified style.", "His fine, wavy, ebony hair is medium-length and is worn in an attractive, precise style.", "His silky, straight, black hair is very long and is worn in a businesslike style.", "His luxurious, curly, obsidian hair is worn in a style that reminds you of a tangled bush.", "His silky, curly, amber hair is worn in a style that reminds you of a helmet.", "His thick, curly, yellow hair is worn in a style that reminds you of a mysterious hood.", "His thick, curly, brown hair is worn in a style that reminds you of a mysterious mask.", "His silky, straight, brown hair is worn in a style that reminds you of a dragon's scales.", "His fine, wavy, very short hair is the color of valuable rubies, and is worn in a precise style.", "His thick, straight, jet black hair is waist-length and is worn in an impractacal style.", "His luxurious, wavy, ebony hair is worn in a style that reminds you of a lionfish's spines.", "His silky, wavy, brick-red hair is very long and is worn in a dignified, simple style.", "His thick, curly, gray hair is worn in a style that reminds you of a gush of water.", "His thick, wavy, sand-colored hair is worn in a style that reminds you of a helmet.", "His luxurious, straight, very short hair is the color of obsidian, and is worn in an impractacal style.", "His thick, straight, beige hair is waist-length and is worn in an uncomplicated, businesslike style.", "He is bald, but used to have luxurious, straight, red hair.", "His thick, straight, brown hair is worn in a style that reminds you of an elaborate sculpture.", "His luxurious, curly, beige hair is worn in a style that reminds you of a crown.", "His silky, straight, bone-white hair is shoulder-length and is worn in an uncomplicated, dignified style.", "His thick, wavy, midnight black hair is short and is worn in an utilitarian, severe style.", "His luxurious, straight, gold hair is worn in a style that reminds you of the rays of the sun.", "His silky, curly, chestnut hair is worn in a style that reminds you of a mysterious mask.", "His luxurious, curly, black hair is worn in a style that reminds you of a mysterious hood.", "His silky, straight, white hair is neck-length and is worn in a businesslike style.", "His silky, straight, black hair is worn in a style that reminds you of a lionfish's spines.", "His luxurious, straight, charcoal-colored hair is worn in a style that reminds you of a burning fire.", "His silky, straight, gunmetal-gray hair is neck-length and is worn in an uncomplicated style.", "He is bald, but used to have luxurious, wavy hair the color of varnished wood He is very tall and has a wide-chested build.", "His silky, straight, beige hair is very short and is worn in an impractacal style.", "His thick, straight, beige hair is medium-length and is worn in a practical style.", "He is bald, but used to have fine, straight, white hair.", "His fine, wavy, sand-colored hair is worn in a style that reminds you of a sea urchin.", "His thick, curly, yellow hair is worn in a style that reminds you of a lionfish's spines.", "His silky, straight, milky-white hair is worn in a style that reminds you of a crown.", "His luxurious, wavy, shoulder-length hair is the color of dark chocolate, and is worn in a precise style.", "His luxurious, straight, gray hair is worn in a style that reminds you of a bird's wing.", "His fine, curly, ebony hair is worn in a style that reminds you of a drifting cloud.", "His silky, curly, iron-gray hair is neck-length and is worn in an artistic style.", "His silky, straight, ash-gray hair is medium-length and is worn in a dignified style.", "His luxurious, straight, amber hair is worn in a style that reminds you of a flame.", "He is bald, but used to have fine, wavy, charcoal-colored hair.", "His fine, straight, beige hair is worn in a style that reminds you of the rays of the sun.", "His luxurious, curly, white hair is medium-length and is worn in an impractacal style.", "His silky, curly, beige hair is neck-length and is worn in an exotic style.", "His fine, straight, gunmetal-gray hair is worn in a style that reminds you of a cascading waterfall.", "His silky, straight, chocolate-colored hair is worn in a style that reminds you of a puffy dandelion.", "He is bald, but used to have luxurious, straight, black hair.", "His silky, straight, yellow hair is medium-length and is worn in an uncomplicated style.", "His luxurious, straight, brown hair is worn in a style that reminds you of a sea urchin.", "His silky, wavy, brown hair is medium-length and is worn in a businesslike, simple style.", "His silky, straight, medium-length hair is the color of yellowed ivory, and is worn in a bizarre style.", "His silky, curly, chestnut hair is worn in a style that reminds you of a burning fire.", "He is bald, but used to have fine, straight hair the color of desert sand He has a graceful build.", "His thick, wavy, short hair is the color of black coffee, and is worn in an utilitarian, severe style.", "His silky, wavy, brown hair is long and is worn in a weird, carefully-crafted style.", "His luxurious, wavy, sand-colored hair is waist-length and is worn in an impractacal, artistic style.", "He is bald, but used to have silky, straight hair the color of bleached bone He is very tall and has a thin build.", "His fine, curly, midnight black hair is worn in a style that reminds you of a dustball.", "His silky, wavy, yellow hair is shoulder-length and is worn in a severe style.", "His luxurious, wavy, white hair is worn in a style that reminds you of a bale of hay.", "His luxurious, wavy, midnight black hair is very short and is worn in a complex style.", "His silky, straight, red hair is neck-length and is worn in a carefully-crafted style.", "His silky, straight, night-black hair is very short and is worn in a carefully-crafted, exotic style.", "His fine, straight, obsidian hair is worn in a style that reminds you of a waterfall.", "His luxurious, wavy, red hair is very long and is worn in an exotic, artistic style.", "His silky, curly, milky-white hair is very short and is worn in an attractive style.", "His silky, wavy, black hair is worn in a style that reminds you of a comet's trail.", "His luxurious, curly, midnight black hair is medium-length and is worn in an attractive style.", "His fine, straight, beige hair is short and is worn in a severe, uncomplicated style.", "He is bald, but used to have luxurious, curly, night-black hair.", "His silky, straight, silver hair is worn in a style that reminds you of a tangled bush.", "His luxurious, wavy, very short hair is the color of charcoal, and is worn in a bizarre style.", "His silky, straight, brown hair is worn in a style that reminds you of a rooster's crest.", "His fine, wavy, white hair is worn in a style that reminds you of a flowing cape.", "His fine, straight, red hair is worn in a style that reminds you of a tangled bush.", "His silky, straight, ebony hair is neck-length and is worn in a severe, simple style.", "His luxurious, curly, waist-length hair is the color of fresh roses, and is worn in an uncomplicated, dignified style.", "His fine, wavy, chocolate-colored hair is worn in a style that reminds you of a pair of horns.", "His silky, straight, yellow hair is medium-length and is worn in a carefully-crafted style.", "He is bald, but used to have luxurious, curly hair the color of coffee with cream He is short and has a lean build.", "His thick, curly, iron-gray hair is medium-length and is worn in a bizarre style.", "He is bald, but used to have luxurious, wavy hair the color of dark chocolate He's got a beard.", "His silky, curly, brown hair is short and is worn in a dignified style.", "His fine, straight, chestnut hair is very short and is worn in an impractacal, artistic style.", "His silky, straight, short hair is the color of black coffee, and is worn in an exotic style.", "His thick, straight, coffee-colored hair is worn in a style that reminds you of a peacock's tail.", "His fine, wavy, brown hair is worn in a style that reminds you of a crown.", "His silky, straight, black hair is worn in a style that reminds you of a complex device.", "His thick, straight, jet black hair is worn in a style that reminds you of an animal's ears.", "His luxurious, wavy, gold hair is medium-length and is worn in an attractive, precise style.", "His thick, straight, yellow hair is worn in a style that reminds you of a dragon's scales.", "His luxurious, wavy, coffee-colored hair is worn in a style that reminds you of a turtle's shell.", "His fine, straight, yellow hair is short and is worn in a carefully-crafted, precise style.", "He is bald, but used to have fine, straight, lemon-yellow hair.", "His luxurious, curly, chocolate-colored hair is long and is worn in a bizarre, elegant style.", "His luxurious, straight, lemon-yellow hair is very short and is worn in a practical style.", "His silky, curly, chestnut hair is short and is worn in an attractive style.", "He is bald, but used to have luxurious, wavy hair the color of desert sand He has an elegant build.", "His silky, wavy, neck-length hair is the color of milk chocolate, and is worn in a weird, elegant style.", "His thick, curly, cream-colored hair is shoulder-length and is worn in a weird, artistic style.", "His fine, straight, gold hair is short and is worn in a complex, attractive style.", "His thick, wavy, brown hair is medium-length and is worn in a dignified, utilitarian style.", "His thick, straight, slate-gray hair is worn in a style that reminds you of the aurora borealis.", "His thick, straight, brown hair is short and is worn in an elegant style.", "His luxurious, curly, white hair is worn in a style that reminds you of a mysterious mask.", "His thick, straight, ash-gray hair is worn in a style that reminds you of a bale of hay.", "His luxurious, straight, very short hair is the color of charcoal, and is worn in a precise style.", "His luxurious, wavy, night-black hair is worn in a style that reminds you of a devil's horns.", "His silky, straight, sand-colored hair is medium-length and is worn in a carefully-crafted style.", "His fine, straight, cream-colored hair is worn in a style that reminds you of a strange headdress.", "He is bald, but used to have fine, straight, chocolate-colored hair.", "His silky, curly, obsidian hair is worn in a style that reminds you of a mysterious hood.", "He is bald, but used to have luxurious, straight, chestnut hair.", "His thick, wavy, neck-length hair is the color of fine gold, and is worn in a handsome style.", "His luxurious, straight, yellow hair is worn in a style that reminds you of a shark's fin.", "His silky, wavy, brown hair is worn in a style that reminds you of the rays of the sun.", "His fine, curly, jet black hair is worn in a style that reminds you of a lionfish's spines.", "His fine, straight, beige hair is short and is worn in a carefully-crafted, weird style.", "His fine, straight, brown hair is worn in a style that reminds you of a complex device.", "His thick, straight, medium-length hair is the color of fine gold, and is worn in a severe style.", "His fine, straight, smoke-gray hair is worn in a style that reminds you of a cobra's hood.", "His luxurious, curly, chalk-white hair is worn in a style that reminds you of a mysterious hood.", "His fine, curly, yellow hair is worn in a style that reminds you of a drifting cloud.", "His fine, straight, black hair is short and is worn in an exotic, artistic style.", "His luxurious, curly, long hair is the color of fine china, and is worn in an uncomplicated style.", "His luxurious, curly, gray hair is worn in a style that reminds you of a dustball.", "His thick, straight, cream-colored hair is worn in a style that reminds you of a plume of smoke.", "His thick, curly, neck-length hair is the color of milk chocolate, and is worn in an artistic style.", "His fine, straight, milky-white hair is worn in a style that reminds you of a devil's horns.", "His thick, straight, coffee-colored hair is worn in a style that reminds you of a helmet.", "His fine, wavy, brown hair is short and is worn in a precise style.", "His thick, curly, gray hair is worn in a style that reminds you of a fluttering flag.", "His silky, straight, brown hair is worn in a style that reminds you of a crown.", "His fine, wavy, brown hair is worn in a style that reminds you of a waterfall.", "His silky, curly, brown hair is worn in a style that reminds you of a fluttering flag.", "His luxurious, curly, black hair is worn in a style that reminds you of a lionfish's spines.", "His silky, curly, black hair is worn in a style that reminds you of the rays of the sun.", "His luxurious, curly, ebony hair is worn in a style that reminds you of a lionfish's spines.", "His thick, curly, gray hair is worn in a style that reminds you of a puffy dandelion.", "His fine, wavy, white hair is very short and is worn in a handsome style.", "His luxurious, straight, medium-length hair is the color of the midnight sky, and is worn in a weird, elegant style.", "His fine, straight, yellow hair is neck-length and is worn in an exotic style.", "His silky, curly, obsidian hair is worn in a style that reminds you of a cascading waterfall.", "His luxurious, curly, obsidian hair is worn in a style that reminds you of a gush of water.", "His fine, straight, cream-colored hair is neck-length and is worn in an uncomplicated, businesslike style.", "His fine, straight, brown hair is worn in a style that reminds you of a pair of wings.", "His fine, straight, brown hair is medium-length and is worn in an impractacal, handsome style.", "His luxurious, curly, gray hair is worn in a style that reminds you of a tangled bush.", "His silky, wavy, brown hair is worn in a style that reminds you of a helmet.", "His luxurious, straight, iron-gray hair is worn in a style that reminds you of a rocky outcropping.", "He is bald, but used to have silky, straight, black hair.", "His luxurious, straight, black hair is medium-length and is worn in an uncomplicated style.", "His thick, straight, coffee-colored hair is worn in a style that reminds you of a mysterious mask.", "His thick, straight, coffee-colored hair is very short and is worn in an utilitarian style.", "He is bald, but used to have luxurious, straight, coffee-colored hair.", "His thick, straight, brown hair is very short and is worn in an artistic style.", "His fine, straight, beige hair is very long and is worn in an artistic, complex style.", "His luxurious, wavy, neck-length hair is the color of red bricks, and is worn in an uncomplicated style.", "His luxurious, curly, medium-length hair is the color of milk chocolate, and is worn in an impractacal, carefully-crafted style.", "His luxurious, straight, gray hair is worn in a style that reminds you of a bird's wing.", "His fine, wavy, medium-length hair is the color of dark chocolate, and is worn in a simple, businesslike style.", "His thick, wavy, chestnut hair is neck-length and is worn in a precise style.", "His fine, curly, coffee-colored hair is very short and is worn in a bizarre style.", "His silky, straight, slate-gray hair is waist-length and is worn in a dignified, simple style.", "His fine, wavy, chocolate-colored hair is shoulder-length and is worn in a complex style.", "His thick, curly, white hair is very long and is worn in an attractive, weird style.", "His thick, straight, neck-length hair is the color of burnished iron, and is worn in a dignified style.", "His fine, straight, brown hair is worn in a style that reminds you of a porcupine's quills.", "He is bald, but used to have thick, curly hair the color of dark chocolate He is short and has a feminine build.", "His fine, wavy, yellow hair is worn in a style that reminds you of a pile of leaves.", "His silky, straight, black hair is very short and is worn in a handsome, weird style.", "His thick, wavy, chocolate-colored hair is worn in a style that reminds you of a peacock's tail."]
    skinList = ["His skin is tanned.", "His skin is light-colored.", "His skin is nut-brown.", "His skin is china-white.", "His skin is tan.", "His skin is pale.", "His skin is deeply-tanned.", "His skin is cream-colored.", "His skin is white.", "His skin is ruddy.", "His skin is dark.", "His skin is brown.", "His skin is black.", "His skin is chocolate-brown."]
    buildList = ["He has a boyish build.", "He has a broad-shouldered build.", "He has a feminine build.", "He has a graceful build.", "He has a lean build.", "He has a lithe build.", "He has a masculine build.", "He has a narrow build.", "He has a plump build.", "He has a slender build.", "He has a thin build.", "He has a wide-chested build.", "He has an angular build.", "He has an athletic build.", "He has an elegant build.", "He has an overmuscled build.", "He is short and has a boyish build.", "He is short and has a broad-shouldered build.", "He is short and has a feminine build.", "He is short and has a graceful build.", "He is short and has a lithe build.", "He is short and has a masculine build.", "He is short and has a narrow build.", "He is short and has a plump build.", "He is short and has a slender build.", "He is short and has a wide-chested build.", "He is short and has an angular build.", "He is short and has an athletic build.", "He is short and has an elegant build.", "He is short and has an overmuscled build.", "He is tall and has a boyish build.", "He is tall and has a broad-shouldered build.", "He is tall and has a feminine build.", "He is tall and has a graceful build.", "He is tall and has a lean build.", "He is tall and has a masculine build.", "He is tall and has a narrow build.", "He is tall and has a slender build.", "He is tall and has a thin build.", "He is tall and has a wide-chested build.", "He is tall and has an athletic build.", "He is tall and has an overmuscled build.", "He is very short and has a boyish build.", "He is very short and has a broad-shouldered build.", "He is very short and has a feminine build.", "He is very short and has a graceful build.", "He is very short and has a lean build.", "He is very short and has a lithe build.", "He is very short and has a masculine build.", "He is very short and has a slender build.", "He is very short and has a thin build.", "He is very short and has a wide-chested build.", "He is very short and has an athletic build.", "He is very short and has an elegant build.", "He is very short and has an overmuscled build.", "He is very tall and has a boyish build.", "He is very tall and has a broad-shouldered build.", "He is very tall and has a feminine build.", "He is very tall and has a graceful build.", "He is very tall and has a lean build.", "He is very tall and has a lithe build.", "He is very tall and has a masculine build.", "He is very tall and has a narrow build.", "He is very tall and has a slender build.", "He is very tall and has a thin build.", "He is very tall and has a wide-chested build.", "He is very tall and has an athletic build.", "He is very tall and has an elegant build.", "He is very tall and has an overmuscled build."]
    facialHairList = ["He\'s got a beard and a prominent moustache.", "He\'s got a beard and moustache.", "He\'s got a beard.", "He\'s got a full beard and a moustache.", "He\'s got a full beard and a thick moustache.", "He\'s got a full beard.", "He\'s got a long moustache.", "He\'s got a moustache.", "He\'s got a prominent moustache.", "He\'s got a short beard and a moustache.", "He\'s got a short beard and a thin moustache.", "He\'s got a short beard.", "He\'s got a small beard and a moustache.", "He\'s got a small moustache.", "He\'s got a stylish moustache.", "He\'s got a thick moustache.", "He\'s got a thin moustache."]
    noseList = ["He has a crooked nose and nearly-nonexistent eyebrows.", "He has a domed forehead and a crooked nose.", "He has a hooked nose and thin eyebrows.", "He has a hooked nose.", "He has a large nose and a weak chin.", "He has a large nose and full lips.", "He has a large nose and small feet.", "He has a large nose and thick eyebrows.", "He has a large nose and thin lips.", "He has a large nose.", "He has a low forehead and a small nose.", "He has a small nose and a pointed chin.", "He has a small nose.", "He has a wide forehead and a hooked nose.", "He has a wide forehead and a small nose.", "He has a wide forehead and an elegant nose.", "He has a wide forehead and an upturned nose.", "He has an elegant nose and a pointed chin.", "He has an elegant nose.", "He has an upturned nose and a wide chin.", "He has an upturned nose and nearly-nonexistent eyebrows.", "He has an upturned nose and prominent cheekbones.", "He has an upturned nose and prominent ears.", "He has an upturned nose and stubby-fingered hands.", "He has an upturned nose and thin eyebrows.", "He has an upturned nose and wide feet.", "He has an upturned nose."]
    otherList = ["This gentleman makes you think of a curious cat.", "This gentleman makes you think of a deadly scorpion.", "This gentleman makes you think of a lost baby bird.", "This gentleman makes you think of a mysterious manta ray.", "This gentleman makes you think of a precise clock.", "This gentleman makes you think of an elegant piece of art..", "This gentleman makes you think of an unstoppable storm.", "This gentleman puts you in mind of a brilliant inventor.", "This gentleman puts you in mind of a busy bee.", "This gentleman puts you in mind of a chirping parakeete.", "This gentleman puts you in mind of a cobra waiting to strike.", "This gentleman puts you in mind of a dangerous but beautiful lionfish.", "This gentleman puts you in mind of a flighty gazelle.", "This gentleman puts you in mind of a fluttering hummingbird.", "This gentleman puts you in mind of a glorious phoenix.", "This gentleman puts you in mind of a lost baby bird.", "This gentleman puts you in mind of a perfect arrow.", "This gentleman puts you in mind of a scuttling lizard.", "This gentleman puts you in mind of a sturdy tree.", "This gentleman puts you in mind of a wild animal.", "This gentleman puts you in mind of a wise owl.", "This gentleman puts you in mind of an elegant dragonfly.", "This gentleman reminds you of a cautious chipmunk.", "This gentleman reminds you of a cobra waiting to strike.", "This gentleman reminds you of a dishonest shyster.", "This gentleman reminds you of a fluttering hummingbird.", "This gentleman reminds you of a placid lake.", "This gentleman reminds you of a playful kitten.", "This gentleman reminds you of a playful otter.", "This gentleman reminds you of a randy rabbit.", "This gentleman reminds you of a regal ruler.", "This gentleman reminds you of a savvy alley cat.", "This gentleman reminds you of a sneaky serpent.", "This gentleman reminds you of a wild animal.", "This gentleman reminds you of a witty comedian.", "This gentleman reminds you of an impenetrable fortress.", "This guy makes you think of a bolt of lightning.", "This guy makes you think of a cobra waiting to strike.", "This guy makes you think of a dangerous but beautiful lionfish.", "This guy makes you think of a lost and wandering spirit.", "This guy makes you think of a playful puppy.", "This guy makes you think of a prowling alligator.", "This guy makes you think of a rabid dog.", "This guy makes you think of a sensitive artist.", "This guy makes you think of a sneaky serpent.", "This guy makes you think of an enraged bear.", "This guy makes you think of an immovable mountain.", "This guy makes you think of an unavoidable bloodhound.", "This guy puts you in mind of a hunting tiger.", "This guy puts you in mind of a lost baby bird.", "This guy puts you in mind of a malevolent demon.", "This guy puts you in mind of a mysterious monolith.", "This guy puts you in mind of a placid lake.", "This guy puts you in mind of a playful dolphin.", "This guy puts you in mind of a playful otter.", "This guy puts you in mind of a prowling panther.", "This guy puts you in mind of a regal ruler.", "This guy puts you in mind of a savvy alley cat.", "This guy puts you in mind of an elegant dragonfly.", "This guy reminds you of a busy bee.", "This guy reminds you of a deadly scorpion.", "This guy reminds you of a flutering butterfly.", "This guy reminds you of a glorious phoenix.", "This guy reminds you of a mysterious raven.", "This guy reminds you of a playful puppy.", "This guy reminds you of a prowling jackal.", "This guy reminds you of a sturdy tree.", "This guy reminds you of an immovable mountain.", "This man makes you think of a curious cat.", "This man makes you think of a darting fish.", "This man makes you think of a dashing cheetah.", "This man makes you think of a deadly eel.", "This man makes you think of a dishonest shyster.", "This man makes you think of a flutering butterfly.", "This man makes you think of a noble eagle.", "This man makes you think of a proud lion.", "This man makes you think of a regal dragon.", "This man makes you think of a wild animal.", "This man makes you think of an industrious ant.", "This man makes you think of an unavoidable bloodhound.", "This man makes you think of an unstoppable hunting dog.", "This man puts you in mind of a brightly-shining star.", "This man puts you in mind of a brilliant inventor.", "This man puts you in mind of a clever fox.", "This man puts you in mind of a dangerous vampire.", "This man puts you in mind of a lone wolf.", "This man puts you in mind of a mysterious sphinx.", "This man puts you in mind of a placid lake.", "This man puts you in mind of a proud lion.", "This man puts you in mind of a randy rabbit.", "This man puts you in mind of a regal dragon.", "This man puts you in mind of a scuttling lizard.", "This man puts you in mind of a strutting cat.", "This man puts you in mind of an industrious ant.", "This man puts you in mind of an inhuman statue.", "This man reminds you of a cobra waiting to strike.", "This man reminds you of a dignified swan.", "This man reminds you of a mysterious manta ray.", "This man reminds you of a playful puppy.", "This man reminds you of a randy demon."]

    otherListFem = ["This lady makes you think of a curious cat.", "This lady makes you think of a deadly scorpion.", "This lady makes you think of a lost baby bird.", "This lady makes you think of a mysterious womanta ray.", "This lady makes you think of a precise clock.", "This lady makes you think of an elegant piece of art..", "This lady makes you think of an unstoppable storm.", "This lady puts you in mind of a brilliant inventor.", "This lady puts you in mind of a busy bee.", "This lady puts you in mind of a chirping parakeete.", "This lady puts you in mind of a cobra waiting to strike.", "This lady puts you in mind of a dangerous but beautiful lionfish.", "This lady puts you in mind of a flighty gazelle.", "This lady puts you in mind of a fluttering hummingbird.", "This lady puts you in mind of a glorious phoenix.", "This lady puts you in mind of a lost baby bird.", "This lady puts you in mind of a perfect arrow.", "This lady puts you in mind of a scuttling lizard.", "This lady puts you in mind of a sturdy tree.", "This lady puts you in mind of a wild animal.", "This lady puts you in mind of a wise owl.", "This lady puts you in mind of an elegant dragonfly.", "This lady reminds you of a cautious chipmunk.", "This lady reminds you of a cobra waiting to strike.", "This lady reminds you of a dishonest shyster.", "This lady reminds you of a fluttering hummingbird.", "This lady reminds you of a placid lake.", "This lady reminds you of a playful kitten.", "This lady reminds you of a playful otter.", "This lady reminds you of a randy rabbit.", "This lady reminds you of a regal ruler.", "This lady reminds you of a savvy alley cat.", "This lady reminds you of a sneaky serpent.", "This lady reminds you of a wild animal.", "This lady reminds you of a witty comedian.", "This lady reminds you of an impenetrable fortress.", "This lady makes you think of a bolt of lightning.", "This lady makes you think of a cobra waiting to strike.", "This lady makes you think of a dangerous but beautiful lionfish.", "This lady makes you think of a lost and wandering spirit.", "This lady makes you think of a playful puppy.", "This lady makes you think of a prowling alligator.", "This lady makes you think of a rabid dog.", "This lady makes you think of a sensitive artist.", "This lady makes you think of a sneaky serpent.", "This lady makes you think of an enraged bear.", "This lady makes you think of an immovable mountain.", "This lady makes you think of an unavoidable bloodhound.", "This lady puts you in mind of a hunting tiger.", "This lady puts you in mind of a lost baby bird.", "This lady puts you in mind of a malevolent demon.", "This lady puts you in mind of a mysterious monolith.", "This lady puts you in mind of a placid lake.", "This lady puts you in mind of a playful dolphin.", "This lady puts you in mind of a playful otter.", "This lady puts you in mind of a prowling panther.", "This lady puts you in mind of a regal ruler.", "This lady puts you in mind of a savvy alley cat.", "This lady puts you in mind of an elegant dragonfly.", "This lady reminds you of a busy bee.", "This lady reminds you of a deadly scorpion.", "This lady reminds you of a flutering butterfly.", "This lady reminds you of a glorious phoenix.", "This lady reminds you of a mysterious raven.", "This lady reminds you of a playful puppy.", "This lady reminds you of a prowling jackal.", "This lady reminds you of a sturdy tree.", "This lady reminds you of an immovable mountain.", "This woman makes you think of a curious cat.", "This woman makes you think of a darting fish.", "This woman makes you think of a dashing cheetah.", "This woman makes you think of a deadly eel.", "This woman makes you think of a dishonest shyster.", "This woman makes you think of a flutering butterfly.", "This woman makes you think of a noble eagle.", "This woman makes you think of a proud lion.", "This woman makes you think of a regal dragon.", "This woman makes you think of a wild animal.", "This woman makes you think of an industrious ant.", "This woman makes you think of an unavoidable bloodhound.", "This woman makes you think of an unstoppable hunting dog.", "This woman puts you in mind of a brightly-shining star.", "This woman puts you in mind of a brilliant inventor.", "This woman puts you in mind of a clever fox.", "This woman puts you in mind of a dangerous vampire.", "This woman puts you in mind of a lone wolf.", "This woman puts you in mind of a mysterious sphinx.", "This woman puts you in mind of a placid lake.", "This woman puts you in mind of a proud lion.", "This woman puts you in mind of a randy rabbit.", "This woman puts you in mind of a regal dragon.", "This woman puts you in mind of a scuttling lizard.", "This woman puts you in mind of a strutting cat.", "This woman puts you in mind of an industrious ant.", "This woman puts you in mind of an inhuwoman statue.", "This woman reminds you of a cobra waiting to strike.", "This woman reminds you of a dignified swan.", "This woman reminds you of a mysterious womanta ray.", "This woman reminds you of a playful puppy.", "This woman reminds you of a randy demon."]
    noseListFem = ["She has a crooked nose and nearly-nonexistent eyebrows.", "She has a domed forehead and a crooked nose.", "She has a hooked nose and thin eyebrows.", "She has a hooked nose.", "She has a large nose and a weak chin.", "She has a large nose and full lips.", "She has a large nose and small feet.", "She has a large nose and thick eyebrows.", "She has a large nose and thin lips.", "She has a large nose.", "She has a low forehead and a small nose.", "She has a small nose and a pointed chin.", "She has a small nose.", "She has a wide forehead and a hooked nose.", "She has a wide forehead and a small nose.", "She has a wide forehead and an elegant nose.", "She has a wide forehead and an upturned nose.", "She has an elegant nose and a pointed chin.", "She has an elegant nose.", "She has an upturned nose and a wide chin.", "She has an upturned nose and nearly-nonexistent eyebrows.", "She has an upturned nose and prominent cheekbones.", "She has an upturned nose and prominent ears.", "She has an upturned nose and stubby-fingered hands.", "She has an upturned nose and thin eyebrows.", "She has an upturned nose and wide feet.", "She has an upturned nose."]
    buildListFem = ["She has a boyish build.", "She has a broad-shouldered build.", "She has a feminine build.", "She has a graceful build.", "She has a lean build.", "She has a litShe build.", "She has a masculine build.", "She has a narrow build.", "She has a plump build.", "She has a slender build.", "She has a thin build.", "She has a wide-chested build.", "She has an angular build.", "She has an athletic build.", "She has an elegant build.", "She has an overmuscled build.", "She is short and has a boyish build.", "She is short and has a broad-shouldered build.", "She is short and has a feminine build.", "She is short and has a graceful build.", "She is short and has a litShe build.", "She is short and has a masculine build.", "She is short and has a narrow build.", "She is short and has a plump build.", "She is short and has a slender build.", "She is short and has a wide-chested build.", "She is short and has an angular build.", "She is short and has an athletic build.", "She is short and has an elegant build.", "She is short and has an overmuscled build.", "She is tall and has a boyish build.", "She is tall and has a broad-shouldered build.", "She is tall and has a feminine build.", "She is tall and has a graceful build.", "She is tall and has a lean build.", "She is tall and has a masculine build.", "She is tall and has a narrow build.", "She is tall and has a slender build.", "She is tall and has a thin build.", "She is tall and has a wide-chested build.", "She is tall and has an athletic build.", "She is tall and has an overmuscled build.", "She is very short and has a boyish build.", "She is very short and has a broad-shouldered build.", "She is very short and has a feminine build.", "She is very short and has a graceful build.", "She is very short and has a lean build.", "She is very short and has a litShe build.", "She is very short and has a masculine build.", "She is very short and has a slender build.", "She is very short and has a thin build.", "She is very short and has a wide-chested build.", "She is very short and has an athletic build.", "She is very short and has an elegant build.", "She is very short and has an overmuscled build.", "She is very tall and has a boyish build.", "She is very tall and has a broad-shouldered build.", "She is very tall and has a feminine build.", "She is very tall and has a graceful build.", "She is very tall and has a lean build.", "She is very tall and has a litShe build.", "She is very tall and has a masculine build.", "She is very tall and has a narrow build.", "She is very tall and has a slender build.", "She is very tall and has a thin build.", "She is very tall and has a wide-chested build.", "She is very tall and has an athletic build.", "She is very tall and has an elegant build.", "She is very tall and has an overmuscled build."]
    skinListFem = ["Her skin is tanned.", "Her skin is light-colored.", "Her skin is nut-brown.", "Her skin is china-white.", "Her skin is tan.", "Her skin is pale.", "Her skin is deeply-tanned.", "Her skin is cream-colored.", "Her skin is white.", "Her skin is ruddy.", "Her skin is dark.", "Her skin is brown.", "Her skin is black.", "Her skin is chocolate-brown."]
    hairListFem = ["Her fine, curly, yellow hair is worn in a style that reminds you of an overused mop.", "Her thick, wavy, brown hair is worn in a style that reminds you of a horse's mane.", "She is bald, but used to have luxurious, straight, brown hair.", "Her silky, straight, very long hair is the color of charcoal, and is worn in a simple, precise style.", "Her fine, straight, gunmetal-gray hair is worn in a style that reminds you of a bale of hay.", "Her thick, straight, brown hair is worn in a style that reminds you of a crown.", "Her thick, straight, medium-length hair is the color of ripe lemons, and is worn in an artistic style.", "Her silky, wavy, black hair is long and is worn in a practical, precise style.", "Her fine, curly, black hair is worn in a style that reminds you of a porcupine's quills.", "Her luxurious, curly, red hair is worn in a style that reminds you of a helmet.", "Her fine, wavy, medium-length hair is the color of chestnuts, and is worn in a bizarre style.", "Her silky, straight, brown hair is worn in a style that reminds you of a flowing stream.", "Her silky, straight, ebony hair is very short and is worn in an attractive, exotic style.", "Her thick, straight, shoulder-length hair is the color of dark chocolate, and is worn in an exotic style.", "Her thick, straight, ebony hair is medium-length and is worn in an uncomplicated style.", "Her silky, straight, sand-colored hair is worn in a style that reminds you of a wave of water.", "She is bald, but used to have silky, straight, soot-black hair.", "Her thick, straight, brown hair is worn in a style that reminds you of a comet's trail.", "Her thick, curly, brown hair is worn in a style that reminds you of a flowing cape.", "Her thick, curly, chestnut hair is worn in a style that reminds you of a devil's horns.", "Her luxurious, curly, medium-length hair is the color of charcoal, and is worn in an utilitarian style.", "Her silky, curly, midnight black hair is worn in a style that reminds you of a horse's mane.", "Her fine, straight, lemon-yellow hair is worn in a style that reminds you of a waterfall.", "She is bald, but used to have luxurious, straight, yellow hair.", "She is bald, but used to have silky, straight, ivory hair.", "Her thick, straight, red hair is worn in a style that reminds you of a flowing cape.", "Her silky, straight, short hair is the color of burnished iron, and is worn in a simple, dignified style.", "Her fine, wavy, ebony hair is medium-length and is worn in an attractive, precise style.", "Her silky, straight, black hair is very long and is worn in a businesslike style.", "Her luxurious, curly, obsidian hair is worn in a style that reminds you of a tangled bush.", "Her silky, curly, amber hair is worn in a style that reminds you of a helmet.", "Her thick, curly, yellow hair is worn in a style that reminds you of a mysterious hood.", "Her thick, curly, brown hair is worn in a style that reminds you of a mysterious mask.", "Her silky, straight, brown hair is worn in a style that reminds you of a dragon's scales.", "Her fine, wavy, very short hair is the color of valuable rubies, and is worn in a precise style.", "Her thick, straight, jet black hair is waist-length and is worn in an impractacal style.", "Her luxurious, wavy, ebony hair is worn in a style that reminds you of a lionfish's spines.", "Her silky, wavy, brick-red hair is very long and is worn in a dignified, simple style.", "Her thick, curly, gray hair is worn in a style that reminds you of a gush of water.", "Her thick, wavy, sand-colored hair is worn in a style that reminds you of a helmet.", "Her luxurious, straight, very short hair is the color of obsidian, and is worn in an impractacal style.", "Her thick, straight, beige hair is waist-length and is worn in an uncomplicated, businesslike style.", "She is bald, but used to have luxurious, straight, red hair.", "Her thick, straight, brown hair is worn in a style that reminds you of an elaborate sculpture.", "Her luxurious, curly, beige hair is worn in a style that reminds you of a crown.", "Her silky, straight, bone-white hair is shoulder-length and is worn in an uncomplicated, dignified style.", "Her thick, wavy, midnight black hair is short and is worn in an utilitarian, severe style.", "Her luxurious, straight, gold hair is worn in a style that reminds you of the rays of the sun.", "Her silky, curly, chestnut hair is worn in a style that reminds you of a mysterious mask.", "Her luxurious, curly, black hair is worn in a style that reminds you of a mysterious hood.", "Her silky, straight, white hair is neck-length and is worn in a businesslike style.", "Her silky, straight, black hair is worn in a style that reminds you of a lionfish's spines.", "Her luxurious, straight, charcoal-colored hair is worn in a style that reminds you of a burning fire.", "Her silky, straight, gunmetal-gray hair is neck-length and is worn in an uncomplicated style.", "She is bald, but used to have luxurious, wavy hair the color of varnished wood She is very tall and has a wide-chested build.", "Her silky, straight, beige hair is very short and is worn in an impractacal style.", "Her thick, straight, beige hair is medium-length and is worn in a practical style.", "She is bald, but used to have fine, straight, white hair.", "Her fine, wavy, sand-colored hair is worn in a style that reminds you of a sea urchin.", "Her thick, curly, yellow hair is worn in a style that reminds you of a lionfish's spines.", "Her silky, straight, milky-white hair is worn in a style that reminds you of a crown.", "Her luxurious, wavy, shoulder-length hair is the color of dark chocolate, and is worn in a precise style.", "Her luxurious, straight, gray hair is worn in a style that reminds you of a bird's wing.", "Her fine, curly, ebony hair is worn in a style that reminds you of a drifting cloud.", "Her silky, curly, iron-gray hair is neck-length and is worn in an artistic style.", "Her silky, straight, ash-gray hair is medium-length and is worn in a dignified style.", "Her luxurious, straight, amber hair is worn in a style that reminds you of a flame.", "She is bald, but used to have fine, wavy, charcoal-colored hair.", "Her fine, straight, beige hair is worn in a style that reminds you of the rays of the sun.", "Her luxurious, curly, white hair is medium-length and is worn in an impractacal style.", "Her silky, curly, beige hair is neck-length and is worn in an exotic style.", "Her fine, straight, gunmetal-gray hair is worn in a style that reminds you of a cascading waterfall.", "Her silky, straight, chocolate-colored hair is worn in a style that reminds you of a puffy dandelion.", "She is bald, but used to have luxurious, straight, black hair.", "Her silky, straight, yellow hair is medium-length and is worn in an uncomplicated style.", "Her luxurious, straight, brown hair is worn in a style that reminds you of a sea urchin.", "Her silky, wavy, brown hair is medium-length and is worn in a businesslike, simple style.", "Her silky, straight, medium-length hair is the color of yellowed ivory, and is worn in a bizarre style.", "Her silky, curly, chestnut hair is worn in a style that reminds you of a burning fire.", "She is bald, but used to have fine, straight hair the color of desert sand She has a graceful build.", "Her thick, wavy, short hair is the color of black coffee, and is worn in an utilitarian, severe style.", "Her silky, wavy, brown hair is long and is worn in a weird, carefully-crafted style.", "Her luxurious, wavy, sand-colored hair is waist-length and is worn in an impractacal, artistic style.", "She is bald, but used to have silky, straight hair the color of bleached bone She is very tall and has a thin build.", "Her fine, curly, midnight black hair is worn in a style that reminds you of a dustball.", "Her silky, wavy, yellow hair is shoulder-length and is worn in a severe style.", "Her luxurious, wavy, white hair is worn in a style that reminds you of a bale of hay.", "Her luxurious, wavy, midnight black hair is very short and is worn in a complex style.", "Her silky, straight, red hair is neck-length and is worn in a carefully-crafted style.", "Her silky, straight, night-black hair is very short and is worn in a carefully-crafted, exotic style.", "Her fine, straight, obsidian hair is worn in a style that reminds you of a waterfall.", "Her luxurious, wavy, red hair is very long and is worn in an exotic, artistic style.", "Her silky, curly, milky-white hair is very short and is worn in an attractive style.", "Her silky, wavy, black hair is worn in a style that reminds you of a comet's trail.", "Her luxurious, curly, midnight black hair is medium-length and is worn in an attractive style.", "Her fine, straight, beige hair is short and is worn in a severe, uncomplicated style.", "She is bald, but used to have luxurious, curly, night-black hair.", "Her silky, straight, silver hair is worn in a style that reminds you of a tangled bush.", "Her luxurious, wavy, very short hair is the color of charcoal, and is worn in a bizarre style.", "Her silky, straight, brown hair is worn in a style that reminds you of a rooster's crest.", "Her fine, wavy, white hair is worn in a style that reminds you of a flowing cape.", "Her fine, straight, red hair is worn in a style that reminds you of a tangled bush.", "Her silky, straight, ebony hair is neck-length and is worn in a severe, simple style.", "Her luxurious, curly, waist-length hair is the color of fresh roses, and is worn in an uncomplicated, dignified style.", "Her fine, wavy, chocolate-colored hair is worn in a style that reminds you of a pair of horns.", "Her silky, straight, yellow hair is medium-length and is worn in a carefully-crafted style.", "She is bald, but used to have luxurious, curly hair the color of coffee with cream She is short and has a lean build.", "Her thick, curly, iron-gray hair is medium-length and is worn in a bizarre style.", "She is bald, but used to have luxurious, wavy hair the color of dark chocolate He's got a beard.", "Her silky, curly, brown hair is short and is worn in a dignified style.", "Her fine, straight, chestnut hair is very short and is worn in an impractacal, artistic style.", "Her silky, straight, short hair is the color of black coffee, and is worn in an exotic style.", "Her thick, straight, coffee-colored hair is worn in a style that reminds you of a peacock's tail.", "Her fine, wavy, brown hair is worn in a style that reminds you of a crown.", "Her silky, straight, black hair is worn in a style that reminds you of a complex device.", "Her thick, straight, jet black hair is worn in a style that reminds you of an animal's ears.", "Her luxurious, wavy, gold hair is medium-length and is worn in an attractive, precise style.", "Her thick, straight, yellow hair is worn in a style that reminds you of a dragon's scales.", "Her luxurious, wavy, coffee-colored hair is worn in a style that reminds you of a turtle's shell.", "Her fine, straight, yellow hair is short and is worn in a carefully-crafted, precise style.", "She is bald, but used to have fine, straight, lemon-yellow hair.", "Her luxurious, curly, chocolate-colored hair is long and is worn in a bizarre, elegant style.", "Her luxurious, straight, lemon-yellow hair is very short and is worn in a practical style.", "Her silky, curly, chestnut hair is short and is worn in an attractive style.", "She is bald, but used to have luxurious, wavy hair the color of desert sand She has an elegant build.", "Her silky, wavy, neck-length hair is the color of milk chocolate, and is worn in a weird, elegant style.", "Her thick, curly, cream-colored hair is shoulder-length and is worn in a weird, artistic style.", "Her fine, straight, gold hair is short and is worn in a complex, attractive style.", "Her thick, wavy, brown hair is medium-length and is worn in a dignified, utilitarian style.", "Her thick, straight, slate-gray hair is worn in a style that reminds you of the aurora borealis.", "Her thick, straight, brown hair is short and is worn in an elegant style.", "Her luxurious, curly, white hair is worn in a style that reminds you of a mysterious mask.", "Her thick, straight, ash-gray hair is worn in a style that reminds you of a bale of hay.", "Her luxurious, straight, very short hair is the color of charcoal, and is worn in a precise style.", "Her luxurious, wavy, night-black hair is worn in a style that reminds you of a devil's horns.", "Her silky, straight, sand-colored hair is medium-length and is worn in a carefully-crafted style.", "Her fine, straight, cream-colored hair is worn in a style that reminds you of a strange headdress.", "She is bald, but used to have fine, straight, chocolate-colored hair.", "Her silky, curly, obsidian hair is worn in a style that reminds you of a mysterious hood.", "She is bald, but used to have luxurious, straight, chestnut hair.", "Her thick, wavy, neck-length hair is the color of fine gold, and is worn in a handsome style.", "Her luxurious, straight, yellow hair is worn in a style that reminds you of a shark's fin.", "Her silky, wavy, brown hair is worn in a style that reminds you of the rays of the sun.", "Her fine, curly, jet black hair is worn in a style that reminds you of a lionfish's spines.", "Her fine, straight, beige hair is short and is worn in a carefully-crafted, weird style.", "Her fine, straight, brown hair is worn in a style that reminds you of a complex device.", "Her thick, straight, medium-length hair is the color of fine gold, and is worn in a severe style.", "Her fine, straight, smoke-gray hair is worn in a style that reminds you of a cobra's hood.", "Her luxurious, curly, chalk-white hair is worn in a style that reminds you of a mysterious hood.", "Her fine, curly, yellow hair is worn in a style that reminds you of a drifting cloud.", "Her fine, straight, black hair is short and is worn in an exotic, artistic style.", "Her luxurious, curly, long hair is the color of fine china, and is worn in an uncomplicated style.", "Her luxurious, curly, gray hair is worn in a style that reminds you of a dustball.", "Her thick, straight, cream-colored hair is worn in a style that reminds you of a plume of smoke.", "Her thick, curly, neck-length hair is the color of milk chocolate, and is worn in an artistic style.", "Her fine, straight, milky-white hair is worn in a style that reminds you of a devil's horns.", "Her thick, straight, coffee-colored hair is worn in a style that reminds you of a helmet.", "Her fine, wavy, brown hair is short and is worn in a precise style.", "Her thick, curly, gray hair is worn in a style that reminds you of a fluttering flag.", "Her silky, straight, brown hair is worn in a style that reminds you of a crown.", "Her fine, wavy, brown hair is worn in a style that reminds you of a waterfall.", "Her silky, curly, brown hair is worn in a style that reminds you of a fluttering flag.", "Her luxurious, curly, black hair is worn in a style that reminds you of a lionfish's spines.", "Her silky, curly, black hair is worn in a style that reminds you of the rays of the sun.", "Her luxurious, curly, ebony hair is worn in a style that reminds you of a lionfish's spines.", "Her thick, curly, gray hair is worn in a style that reminds you of a puffy dandelion.", "Her fine, wavy, white hair is very short and is worn in a handsome style.", "Her luxurious, straight, medium-length hair is the color of the midnight sky, and is worn in a weird, elegant style.", "Her fine, straight, yellow hair is neck-length and is worn in an exotic style.", "Her silky, curly, obsidian hair is worn in a style that reminds you of a cascading waterfall.", "Her luxurious, curly, obsidian hair is worn in a style that reminds you of a gush of water.", "Her fine, straight, cream-colored hair is neck-length and is worn in an uncomplicated, businesslike style.", "Her fine, straight, brown hair is worn in a style that reminds you of a pair of wings.", "Her fine, straight, brown hair is medium-length and is worn in an impractacal, handsome style.", "Her luxurious, curly, gray hair is worn in a style that reminds you of a tangled bush.", "Her silky, wavy, brown hair is worn in a style that reminds you of a helmet.", "Her luxurious, straight, iron-gray hair is worn in a style that reminds you of a rocky outcropping.", "She is bald, but used to have silky, straight, black hair.", "Her luxurious, straight, black hair is medium-length and is worn in an uncomplicated style.", "Her thick, straight, coffee-colored hair is worn in a style that reminds you of a mysterious mask.", "Her thick, straight, coffee-colored hair is very short and is worn in an utilitarian style.", "She is bald, but used to have luxurious, straight, coffee-colored hair.", "Her thick, straight, brown hair is very short and is worn in an artistic style.", "Her fine, straight, beige hair is very long and is worn in an artistic, complex style.", "Her luxurious, wavy, neck-length hair is the color of red bricks, and is worn in an uncomplicated style.", "Her luxurious, curly, medium-length hair is the color of milk chocolate, and is worn in an impractacal, carefully-crafted style.", "Her luxurious, straight, gray hair is worn in a style that reminds you of a bird's wing.", "Her fine, wavy, medium-length hair is the color of dark chocolate, and is worn in a simple, businesslike style.", "Her thick, wavy, chestnut hair is neck-length and is worn in a precise style.", "Her fine, curly, coffee-colored hair is very short and is worn in a bizarre style.", "Her silky, straight, slate-gray hair is waist-length and is worn in a dignified, simple style.", "Her fine, wavy, chocolate-colored hair is shoulder-length and is worn in a complex style.", "Her thick, curly, white hair is very long and is worn in an attractive, weird style.", "Her thick, straight, neck-length hair is the color of burnished iron, and is worn in a dignified style.", "Her fine, straight, brown hair is worn in a style that reminds you of a porcupine's quills.", "She is bald, but used to have thick, curly hair the color of dark chocolate She is short and has a feminine build.", "Her fine, wavy, yellow hair is worn in a style that reminds you of a pile of leaves.", "Her silky, straight, black hair is very short and is worn in a handsome, weird style.", "Her thick, wavy, chocolate-colored hair is worn in a style that reminds you of a peacock's tail."]
    eyeListFem = ["She has round gray eyes that are like two pools of mercury.", "She has deep-set chestnut eyes.", "This aloof guy has large gunmetal-gray eyes.", "She has beady eyes the color of burnished iron.", "She has almond-shaped purple eyes that are like two windows on the evening sky.", "She has deep-set blue eyes that are like two lagoons.", "She has slitted blue eyes that are like two chunks of lapis lazuli.", "She has large eyes the color of an overcast sky.", "This harried guy has droopy chocolate-colored eyes.", "This innocent woman has slitted coffee-colored eyes.", "This greedy woman has round eyes the color of blooming violets.", "This clever guy has beady gray eyes that are like two silver coins.", "She has beady eyes the color of varnished wood.", "She has hooded aquamarine eyes.", "She has almond-shaped blue eyes that are like two pools of water.", "She has narrow eyes the color of the afternoon sky.", "This personable lady has round lavender eyes.", "This brave lady has slanted turquoise eyes.", "This tense woman has hooded gray eyes that are like two windows looking out on an overcast sky.", "This seductive lady has deep-set blue eyes.", "She has hooded brown eyes that are like two acorns.", "This thoughtful woman has almond-shaped eyes the color of cold ashes.", "This wild guy has large purple eyes that are like two amethysts.", "She has almond-shaped blue eyes.", "She has slanted eyes the color of coffee with cream.", "She has deep-set brown eyes that are like two tiger-eye gems.", "This peaceful lady has hooded brown eyes.", "This enthusiastic woman has droopy gray eyes.", "She has slanted sky-blue eyes.", "She has almond-shaped gray eyes that are like two silver coins.", "She has wide brown eyes that are like two acorns.", "This cruel guy has large gray eyes that are like two pools of mercury.", "She has slanted chocolate-colored eyes.", "This mysterious woman has beady gray eyes that are like two pools of mercury.", "She has deep-set brown eyes that are like two drops of chocolate.", "This studious lady has large blue eyes.", "This aloof lady has almond-shaped eyes the color of burnished iron.", "She has almond-shaped gray eyes that are like two pieces of steel.", "This humorous lady has droopy brown eyes that are like two bronze coins.", "She has large gray eyes that are like two pools of mercury.", "She has round brown eyes that are like two drops of chocolate.", "This aristocratic lady has narrow black eyes.", "She has slanted purple eyes that are like two amethysts.", "This spiritual woman has beady eyes the color of fine silver.", "She has wide brown eyes.", "She has slanted blue eyes that are like two sapphires.", "This seductive lady has slitted brown eyes that are like two bronze coins.", "She has beady gunmetal-gray eyes.", "This cunning guy has droopy eyes the color of milk chocolate.", "This sinful guy has wide eyes the color of black coffee.", "This harried woman has almond-shaped green eyes that are like two clumps of moss.", "This trusting woman has wide brown eyes that are like two bronze coins.", "She has slanted gray eyes.", "This intimidating guy has slanted blue eyes that are like two turquoises.", "She has droopy eyes the color of chestnuts.", "She has large eyes the color of amethysts.", "This noble lady has wide green eyes that are like two pools of stangant water.", "She has large eyes the color of an overcast sky.", "She has slitted chestnut eyes.", "This noble lady has large blue eyes that are like two chunks of lapis lazuli.", "She has beady black eyes that are like two dark pits.", "This serene guy has beady brown eyes that are like two tiger-eye gems.", "This cruel guy has slanted emerald eyes.", "This courageous guy has round brown eyes that are like two drops of chocolate.", "This thoughtful guy has deep-set ash-gray eyes.", "She has round blue eyes that are like two pools of water.", "This personable woman has droopy blue eyes that are like two sapphires.", "She has large eyes the color of the midnight sky.", "This clever lady has wide gray eyes that are like two pieces of steel.", "This misguided guy has droopy blue eyes.", "She has narrow gray eyes that are like two pools of mercury.", "She has beady eyes the color of dark chocolate.", "She has slanted brown eyes that are like two bronze coins.", "This clever guy has round gray eyes that are like two windows looking out on an overcast sky.", "She has droopy amethyst eyes.", "She has slanted eyes the color of blueberries.", "This intimidating guy has wide chestnut eyes.", "She has narrow brown eyes that are like two discs of wood.", "She has slitted black eyes.", "She has beady brown eyes.", "She has slitted coffee-colored eyes.", "This courageous guy has slitted purple eyes.", "She has round gray eyes that are like two pieces of steel.", "She has wide eyes the color of burnished iron.", "This wily lady has slanted gray eyes that are like two silver coins.", "This boorish lady has large eyes the color of turquoises.", "She has droopy brown eyes that are like two bronze coins.", "This witty woman has almond-shaped eyes the color of burnished iron.", "She has almond-shaped brown eyes that are like two drops of chocolate.", "She has slitted eyes the color of fresh green apples.", "She has slanted eyes the color of chestnuts.", "She has beady brown eyes that are like two splotches of mud.", "This trusting guy has hooded gray eyes.", "This solem woman has almond-shaped brown eyes.", "She has droopy chocolate-colored eyes.", "This serious guy has hooded blue eyes.", "She has almond-shaped purple eyes that are like two amethysts.", "She has narrow brown eyes that are like two acorns.", "This vain guy has large brown eyes that are like two patches of dried blood.", "She has deep-set chestnut eyes.", "She has large gray eyes that are like two pieces of steel.", "This foul-mouthed guy has wide blue eyes that are like two sapphires.", "This confused lady has slitted gray eyes.", "She has round violet eyes that are like two drops of wine.", "She has hooded brown eyes that are like two drops of chocolate.", "She has beady gray eyes that are like two pools of mercury.", "She has beady purple eyes.", "She has narrow gray eyes.", "She has beady brown eyes that are like two bronze coins.", "She has wide brown eyes that are like two acorns.", "This antisocial lady has round chocolate-colored eyes.", "This sensitive lady has droopy purple eyes that are like two windows on the evening sky.", "This arrogant lady has slanted blue eyes that are like two chunks of lapis lazuli.", "This confident lady has slitted eyes the color of valuable emeralds.", "She has hooded brown eyes.", "This romantic woman has round brown eyes that are like two patches of dried blood.", "She has slanted eyes the color of ripe plums.", "This vain lady has beady brown eyes that are like two acorns.", "This curious lady has round green eyes.", "She has droopy plum-colored eyes.", "She has deep-set blue eyes that are like two turquoises.", "She has beady eyes the color of chestnuts.", "This energetic lady has slitted slate-gray eyes.", "She has beady turquoise eyes.", "She has slitted gray eyes that are like two silver coins.", "She has slitted brown eyes that are like two discs of wood.", "This willfull guy has large gray eyes that are like two windows looking out on an overcast sky.", "This romantic woman has droopy brown eyes that are like two acorns.", "This angry lady has round brown eyes.", "This mistrustful woman has large eyes the color of blue tropical waters.", "She has hooded gray eyes that are like two silver coins.", "This energetic woman has hooded brown eyes that are like two discs of wood.", "This silly lady has beady soot-black eyes.", "This antisocial lady has hooded blue eyes that are like two windows on the afternoon sky.", "This misguided guy has slitted brown eyes that are like two tiger-eye gems.", "This silly guy has narrow eyes the color of the evening sky.", "She has almond-shaped blue eyes that are like two windows on the afternoon sky.", "She has round blue eyes that are like two pools of water.", "This contemplative woman has beady black eyes that are like two lumps of coal.", "This generous lady has deep-set blue eyes that are like two pools of water.", "This sneaky woman has narrow gray eyes that are like two silver coins.", "She has beady brown eyes that are like two patches of dried blood.", "This angry guy has narrow black eyes.", "She has beady gray eyes that are like two pieces of steel.", "This studious guy has large brown eyes that are like two tiger-eye gems.", "She has slanted gray eyes that are like two pools of mercury.", "She has slitted eyes the color of an overcast sky.", "She has hooded green eyes.", "She has round gray eyes that are like two silver coins.", "This serious woman has slitted sky-blue eyes.", "She has round blue eyes that are like two chunks of lapis lazuli.", "This cunning woman has beady eyes the color of the midnight sky.", "She has narrow brown eyes that are like two splotches of mud.", "She has deep-set brown eyes that are like two bronze coins.", "She has deep-set black eyes.", "This sensual woman has droopy eyes the color of varnished wood.", "This generous lady has hooded brown eyes that are like two discs of wood.", "She has wide blue eyes that are like two pools of water.", "This noble woman has droopy brown eyes that are like two discs of wood.", "This laid-back guy has slitted beige eyes.", "She has hooded violet eyes that are like two amethysts.", "This noble woman has large eyes the color of the afternoon sky.", "She has beady gray eyes that are like two pieces of steel.", "This angry guy has beady green eyes that are like two clumps of moss.", "She has deep-set blue eyes that are like two pools of water.", "This sinful lady has deep-set royal purple eyes.", "This brave guy has deep-set beige eyes.", "She has deep-set brown eyes.", "This determined guy has narrow violet eyes that are like two amethysts.", "This lazy guy has round brown eyes.", "This wordy lady has round brown eyes.", "This noble woman has slanted gray eyes.", "This aloof lady has narrow cobalt-blue eyes.", "She has round purple eyes that are like two amethysts.", "She has slitted gray eyes that are like two pieces of steel.", "She has wide brown eyes.", "She has almond-shaped brown eyes that are like two drops of chocolate.", "This lonely guy has large brown eyes that are like two tiger-eye gems.", "She has large brown eyes.", "She has slitted blue eyes that are like two turquoises.", "This laid-back guy has large eyes the color of the midnight sky.", "This willfull woman has narrow beige eyes.", "This energetic guy has droopy gray eyes that are like two silver coins.", "She has wide smoke-gray eyes.", "This silly guy has slitted eyes the color of ripe plums.", "She has narrow blue eyes that are like two chunks of lapis lazuli.", "She has slitted eyes the color of amethysts.", "She has round blue eyes that are like two chunks of lapis lazuli.", "She has large brown eyes.", "She has slitted green eyes that are like two clumps of moss.", "This spiritual woman has almond-shaped brown eyes that are like two bronze coins.", "She has almond-shaped coffee-colored eyes.", "This wise lady has large chestnut eyes.", "She has beady blue eyes that are like two sapphires.", "She has large eyes the color of dark chocolate.", "She has hooded brown eyes.", "She has round blue eyes.", "This harried woman has almond-shaped gray eyes that are like two windows looking out on an overcast sky.", "This wordy lady has hooded eyes the color of obsidian.", "This wise woman has slanted gray eyes that are like two pools of mercury."]
    wardrobeListFem = ["Her wardrobe is severe, and is completely orange.", "Her wardrobe is revealing.", "Her wardrobe is attractive and mysterious, with a lot of purple.", "Her wardrobe is professional.", "Her wardrobe is elegant.", "Her wardrobe is sexy, with a lot of black.", "Her wardrobe is strange.", "Her wardrobe is mysterious.", "Her wardrobe is impractacal.", "Her wardrobe is flattering, with a lot of purple.", "Her wardrobe is businesslike.", "Her wardrobe is dignified.", "Her wardrobe is tight.", "Her wardrobe is practical.", "Her wardrobe is bizarre.", "Her wardrobe is strange and risque, with a lot of green and white.", "Her wardrobe is uncomplicated, with a lot of white and gray.", "Her wardrobe is classy.", "Her wardrobe is strange, with a lot of blue and white.", "Her wardrobe is elaborate.", "Her wardrobe is flattering.", "Her wardrobe is risque, with a lot of green.", "Her wardrobe is severe and attractive, with a completely red color scheme.", "Her wardrobe is weird and risque, with a lot of black.", "Her wardrobe is flattering, and is completely violet.", "Her wardrobe is elegant and impractacal, with a lot of orange and white.", "Her wardrobe is tight, with a lot of green and gray.", "Her wardrobe is strange and sexy, with a lot of gray and red.", "Her wardrobe is elegant and complicated, with a lot of white.", "Her wardrobe is dignified, with a lot of blue.", "Her wardrobe is plain, with a lot of green and violet.", "Her wardrobe is uncomplicated and businesslike, with a lot of blue and white.", "Her wardrobe is tight.", "Her wardrobe is attractive, and is completely green and gray.", "Her wardrobe is classy and sexy, with a mostly white and black color scheme.", "Her wardrobe is no-nonsense and severe, with a lot of blue.", "Her wardrobe is sexy and simple, with a lot of red.", "Her wardrobe is sexy and simple, with a mostly violet color scheme.", "Her wardrobe is strange.", "Her wardrobe is professional and practical, with a lot of blue and white.", "Her wardrobe is severe.", "Her wardrobe is strange.", "Her wardrobe is sexy, with a lot of blue and black.", "Her wardrobe is unconventional.", "Her wardrobe is practical and severe, with a mostly green and black color scheme.", "Her wardrobe is classy and mysterious, with a lot of blue and white.", "Her wardrobe is elaborate, with a lot of orange.", "Her wardrobe is dignified.", "Her wardrobe is risque.", "Her wardrobe is severe.", "Her wardrobe is unusual.", "Her wardrobe is unusual.", "Her wardrobe is severe, with a lot of red and brown.", "Her wardrobe is flattering and strange, with a lot of green.", "Her wardrobe is flattering, and is mostly white.", "Her wardrobe is mysterious, and is mostly yellow and blue.", "Her wardrobe is attractive.", "Her wardrobe is unusual and revealing, with a mostly green and blue color scheme.", "Her wardrobe is severe.", "Her wardrobe is impractacal and revealing, with a completely black color scheme.", "Her wardrobe is sexy, with a lot of orange.", "Her wardrobe is classy.", "Her wardrobe is unconventional.", "Her wardrobe is classy.", "Her wardrobe is classy and unusual, with a lot of orange.", "Her wardrobe is impractacal, and is mostly black and purple.", "Her wardrobe is risque.", "Her wardrobe is risque and weird, with a lot of blue.", "Her wardrobe is classy, and is completely green and black.", "Her wardrobe is elegant, and is completely orange.", "Her wardrobe is attractive and bizarre, with a lot of blue.", "Her wardrobe is complicated and mysterious, with a lot of purple and gray.", "Her wardrobe is elaborate and sexy, with a mostly purple color scheme.", "Her wardrobe is businesslike, and is mostly brown.", "Her wardrobe is utilitarian, with a lot of blue and yellow.", "Her wardrobe is tight.", "Her wardrobe is classy, and is completely black.", "Her wardrobe is strange.", "Her wardrobe is utilitarian and businesslike, with a completely red and orange color scheme.", "Her wardrobe is complicated and risque, with a lot of blue.", "Her wardrobe is classy and strange, with a mostly yellow color scheme.", "Her wardrobe is practical and dignified, with a lot of blue.", "Her wardrobe is strange and businesslike, with a mostly green color scheme.", "Her wardrobe is classy and odd, with a mostly green and yellow color scheme.", "Her wardrobe is elegant.", "Her wardrobe is odd and tight, with a lot of black.", "Her wardrobe is severe.", "Her wardrobe is classy and mysterious, with a lot of white and orange.", "Her wardrobe is odd.", "Her wardrobe is tight, and is mostly white and green.", "Her wardrobe is severe.", "Her wardrobe is classy, with a lot of orange.", "Her wardrobe is strange.", "Her wardrobe is artistic and complicated, with a lot of yellow and red.", "Her wardrobe is classy and elaborate, with a lot of brown.", "Her wardrobe is artistic.", "Her wardrobe is unusual.", "Her wardrobe is weird.", "Her wardrobe is no-nonsense and dignified, with a mostly white and violet color scheme.", "Her wardrobe is unconventional and artistic, with a completely purple color scheme.", "Her wardrobe is utilitarian, and is completely blue.", "Her wardrobe is uncomplicated.", "Her wardrobe is dignified.", "Her wardrobe is artistic.", "Her wardrobe is severe and plain, with a lot of black.", "Her wardrobe is impractacal, and is completely green.", "Her wardrobe is unusual.", "Her wardrobe is flattering, and is completely blue and gray.", "Her wardrobe is practical, and is mostly purple.", "Her wardrobe is mysterious, with a lot of green.", "Her wardrobe is flattering, and is completely green and yellow.", "Her wardrobe is strange, with a lot of brown and red.", "Her wardrobe is practical and severe, with a mostly yellow and blue color scheme.", "Her wardrobe is complicated and artistic, with a lot of red and gray.", "Her wardrobe is risque and utilitarian, with a lot of red and violet.", "Her wardrobe is bizarre.", "Her wardrobe is weird, with a lot of black and blue.", "Her wardrobe is elaborate, with a lot of green.", "Her wardrobe is businesslike and strange, with a lot of yellow.", "Her wardrobe is revealing.", "Her wardrobe is attractive, with a lot of green and gray.", "Her wardrobe is elegant.", "Her wardrobe is sexy.", "Her wardrobe is sexy, with a lot of white and red.", "Her wardrobe is professional and classy, with a completely black and gray color scheme.", "Her wardrobe is plain and severe, with a lot of red and blue.", "Her wardrobe is utilitarian, and is mostly orange.", "Her wardrobe is sexy and weird, with a mostly green color scheme.", "Her wardrobe is bizarre and flattering, with a lot of yellow.", "Her wardrobe is revealing, with a lot of yellow.", "Her wardrobe is bizarre and revealing, with a lot of blue and gray.", "Her wardrobe is dignified.", "Her wardrobe is uncomplicated and severe, with a lot of white and orange.", "Her wardrobe is mysterious, and is completely red and gray.", "Her wardrobe is mysterious and sexy, with a completely orange and brown color scheme.", "Her wardrobe is mysterious, with a lot of green and gray.", "Her wardrobe is elegant.", "Her wardrobe is weird and revealing, with a lot of white and black.", "Her wardrobe is risque, with a lot of violet and black.", "Her wardrobe is risque and unusual, with a lot of blue and yellow.", "Her wardrobe is revealing.", "Her wardrobe is attractive and strange, with a mostly green color scheme.", "Her wardrobe is elaborate and artistic, with a lot of gray and brown.", "Her wardrobe is plain.", "Her wardrobe is attractive and tight, with a lot of violet and blue.", "Her wardrobe is odd and elegant, with a lot of gray and orange.", "Her wardrobe is mysterious and artistic, with a lot of red and black.", "Her wardrobe is dignified.", "Her wardrobe is simple.", "Her wardrobe is risque, with a lot of red.", "Her wardrobe is utilitarian.", "Her wardrobe is simple, with a lot of gray.", "Her wardrobe is artistic and bizarre, with a completely red and purple color scheme.", "Her wardrobe is practical.", "Her wardrobe is elegant.", "Her wardrobe is unusual.", "Her wardrobe is severe.", "Her wardrobe is uncomplicated.", "Her wardrobe is risque and flattering, with a completely yellow color scheme.", "Her wardrobe is tight and no-nonsense, with a completely yellow and red color scheme.", "Her wardrobe is risque and simple, with a lot of red.", "Her wardrobe is complicated and tight, with a lot of gray.", "Her wardrobe is unconventional and artistic, with a lot of blue.", "Her wardrobe is plain.", "Her wardrobe is flattering, and is completely white and orange.", "Her wardrobe is flattering, and is completely green.", "Her wardrobe is tight.", "Her wardrobe is mysterious and tight, with a mostly gray color scheme.", "Her wardrobe is classy.", "Her wardrobe is sexy and practical, with a completely brown color scheme.", "Her wardrobe is sexy, and is completely white.", "Her wardrobe is elaborate.", "Her wardrobe is uncomplicated.", "Her wardrobe is professional.", "Her wardrobe is odd and unusual, with a lot of purple and black.", "Her wardrobe is revealing and elegant, with a mostly red and yellow color scheme.", "Her wardrobe is elegant and revealing, with a completely red and white color scheme.", "Her wardrobe is revealing and weird, with a lot of orange and red.", "Her wardrobe is professional and plain, with a completely green color scheme.", "Her wardrobe is sexy.", "Her wardrobe is strange.", "Her wardrobe is simple, and is completely blue and yellow.", "Her wardrobe is risque and unusual, with a mostly yellow color scheme.", "Her wardrobe is sexy.", "Her wardrobe is severe.", "Her wardrobe is artistic and tight, with a lot of blue.", "Her wardrobe is uncomplicated and businesslike, with a lot of black and white.", "Her wardrobe is uncomplicated.", "Her wardrobe is attractive and mysterious, with a lot of red.", "Her wardrobe is unusual, and is mostly blue and white.", "Her wardrobe is mysterious, and is mostly black and red.", "Her wardrobe is classy and tight, with a mostly blue and yellow color scheme.", "Her wardrobe is elaborate, with a lot of green.", "Her wardrobe is no-nonsense.", "Her wardrobe is mysterious and risque, with a lot of yellow and blue.", "Her wardrobe is sexy.", "Her wardrobe is severe.", "Her wardrobe is odd and risque, with a completely white color scheme.", "Her wardrobe is attractive and mysterious, with a mostly gray and brown color scheme.", "Her wardrobe is artistic, and is mostly green and gray."]

    if sex == "Male" :
        details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, wardrobeList[(random.randrange(0, wardrobeList.__len__(), 1))], "\n", eyeList[(random.randrange(0, eyeList.__len__(), 1))], "\n", hairList[(random.randrange(0, hairList.__len__(), 1))], "\n", skinList[(random.randrange(0, skinList.__len__(), 1))], "\n", buildList[(random.randrange(0, buildList.__len__(), 1))], "\n", facialHairList[(random.randrange(0, facialHairList.__len__(), 1))], "\n", noseList[(random.randrange(0, noseList.__len__(), 1))], "\n", otherList[(random.randrange(0, otherList.__len__(), 1))], "\n--------------------------------------------\n")
    else :
        details = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (details, wardrobeListFem[(random.randrange(0, wardrobeListFem.__len__(), 1))], "\n", eyeListFem[(random.randrange(0, eyeListFem.__len__(), 1))], "\n", hairListFem[(random.randrange(0, hairListFem.__len__(), 1))], "\n", skinListFem[(random.randrange(0, skinListFem.__len__(), 1))], "\n", buildListFem[(random.randrange(0, buildListFem.__len__(), 1))], "\n", noseListFem[(random.randrange(0, noseListFem.__len__(), 1))], "\n", otherListFem[(random.randrange(0, otherListFem.__len__(), 1))], "\n--------------------------------------------\n")

    details = "%s%s" % (details, TreasureGenerator.EncouterTreasure(cr, currency = cr, artObj = cr, specialMats = cr, normEquip = cr, magicEquip = cr, pots = cr, scroll = cr, wand = cr, staff = cr, rod = cr, ring = cr, wonderous = cr, artifact = cr, cursed = cr, intelligent = cr))

    fileName = "%s%s%s%s%s%s" % ("~", name, sex, subType, npcClass, ".txt")
    oFile = open(fileName, "w")
    oFile.write(details)
    oFile.close()

print("Number of NPCs\n")
countOf = ""
countOf = input()
countOf = int(countOf)
print("Generate Unique(Yes/No)")
unique = "No"
unique = input().lower()

while countOf > 0 and unique == "yes" :
    cr = random.randrange(1, 21, 1)
    print("Name?\n")
    name = ""
    name = input()
    print("Class?\n", '"Guard", "Professional", "Assassin", "Rogue", "Priest", "Fighter", "Noble", "Slave", "Mage", "Military", "Merchant"\n', 'Professional(uniqueProfession)"farmer", "hunter", "fisherman", "sailor", "Jeweller", "Mason", "Smith", "Musician", "Prostitute", "Sculptor", "Painter", "Skald", "Medicine"\n', 'Military(uniquePosition) "Infantry", "Archer", "Siege Engineer", "Infantry Commander", "Knight", "Siege Commander", "General"\n')
    classNames = ""
    classNames = input()
    Humanoid(cr, name = None, classNames = None)
    countOf -= 1

while countOf > 0 and unique == "no" :
    cr = random.randrange(1, 21, 1)
    Humanoid(cr)
    countOf -= 1