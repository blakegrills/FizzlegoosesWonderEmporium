def Population(cityType) :
	pass

def Relgion(alignment) :
	pass

def Military(strength) :
	pass

def Race() :
	pass

def Leader(alignment, cityType, religion) :
	pass

def NotableNPCs(alignment, cityType, religion) :
	pass

def Wealth(cityType) :
	pass

def NoteablePlaces(cityType, religion, alignment, race) :
	pass

def Inn(num) :
	pass

def Store(num) :
	pass

def Craftsman(num) :
	pass

def Guilds(num) :
	pass

print("What is the Cities Name?\n")
cityName << input()
print("\nWhat is the Cities Size?((V)illage, (T)own, (C)ity, (M)etropolis)\n")
cityType << input().tolower()
print("\nWhat is the Cities Alignment?(LG, NG, CG, LN, N, CN, LE, NE, CE)\n")
alignment << input()
print("\nWhat is the Military strength?(conscripts, low, medium, high, militant)\n")
strength << input().tolower()